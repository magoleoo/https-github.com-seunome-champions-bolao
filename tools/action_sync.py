import json
import sqlite3
import urllib.request
from datetime import datetime
from pathlib import Path
from tempfile import NamedTemporaryFile

import sys
import os

# Adds the backend module to path so we can import from it
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.config import load_settings
from backend.db import connect, initialize_schema
from backend.scoring_engine import persist_leaderboard
from backend.sync_api_football import sync_matches

def main():
    settings = load_settings()
    connection = connect(settings.database_path)
    SCHEMA_PATH = Path(settings.project_root) / "backend" / "schema.sql"
    initialize_schema(connection, SCHEMA_PATH)

    print("=== INICIANDO SINCRONIZAÇÃO AUTOMÁTICA ===")

    # 1. (Opcional) Puxar CSV do Forms e inserir no banco SQLite
    # Aqui você pode adicionar lógica para baixar a URL do CSV público do Forms 
    # e popular a tabela `participant_match_predictions` automaticamente.
    print("[1/4] Lendo respostas do Forms (a implementar conforme estrutura do CSV)...")

    # 2. Sincronizar API-Football (Resultados Reais)
    if settings.api_football_key:
        print("[2/4] Buscando resultados oficiais na API-Football...")
        try:
            result = sync_matches(connection, settings, settings.default_season)
            print(f"      -> {result['fixtures_synced']} jogos sincronizados.")
        except Exception as e:
            print(f"      -> Erro na API: {e}")
    else:
        print("[2/4] API_FOOTBALL_KEY não configurada. Pulando sync online.")

    # 3. Recalcular o Ranking Geral
    print("[3/4] Recalculando o Ranking Oficial...")
    ranking = persist_leaderboard(connection, settings.default_season)
    print(f"      -> Ranking gerado para {len(ranking)} participantes.")

    # 4. Exportar JSONs estáticos para o GitHub Pages (Pasta raiz ou api/)
    print("[4/4] Gerando JSONs estáticos para o frontend...")
    api_dir = settings.project_root / "api"
    api_dir.mkdir(exist_ok=True)

    # Export Ranking
    with open(api_dir / "ranking.json", "w", encoding="utf-8") as f:
        json.dump({"season": settings.default_season, "ranking": ranking}, f, ensure_ascii=False, indent=2)

    # Export Matches
    rows = connection.execute("SELECT m.*, ht.name as home_team_name, at.name as away_team_name FROM matches m JOIN teams ht ON ht.id = m.home_team_id JOIN teams at ON at.id = m.away_team_id").fetchall()
    with open(api_dir / "matches.json", "w", encoding="utf-8") as f:
        json.dump({"matches": [dict(r) for r in rows]}, f, ensure_ascii=False, indent=2)
    
    # Export Participants
    rows = connection.execute("SELECT id, slug, name, is_active FROM participants ORDER BY name").fetchall()
    with open(api_dir / "participants.json", "w", encoding="utf-8") as f:
        json.dump({"participants": [dict(r) for r in rows]}, f, ensure_ascii=False, indent=2)

    print("=== SUCESSO! O GitHub Pages está pronto para ser atualizado ===")
    connection.close()

if __name__ == "__main__":
    main()
