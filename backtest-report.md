# Backtest playoff + oitavas

Base analisada: `/Users/leopicca/Downloads/06_Projetos_e_Criacao/champions-bolao/data/Bolao_UEFA_25_26_OFICIAL.xlsx`

## Resultado geral

- Playoff: `21/21` participantes batem exatamente com a planilha.
- Oitavas: `21/21` participantes batem exatamente com a planilha.
- Oitavas vs aba `Acertos`: `21/21` participantes batem nos contadores de tendência, placar e classificados.
- Fallback automático de acertos aplicado em `3` participante(s) com célula vazia na aba `Acertos`.

## Participante por participante

| Participante | Playoff calc | Playoff planilha | Delta | Oitavas calc | Oitavas planilha | Delta | Hope Solo | Acertos 8as |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Biel | 10.50 | 10.50 | 0.00 | 46.00 | 46.00 | 0.00 | 0 | T 10/10 • P 3/3 • C 7/7 |
| Celsinho | 12.50 | 12.50 | 0.00 | 24.00 | 24.00 | 0.00 | 1 | T 7/7 • P 1/1 • C 4/4 |
| Dan | 16.00 | 16.00 | 0.00 | 33.00 | 33.00 | 0.00 | 0 | T 10/10 • P 1/1 • C 6/6 |
| Deco | 15.00 | 15.00 | 0.00 | 33.00 | 33.00 | 0.00 | 0 | T 9/9 • P 0/0 • C 8/8 |
| Enrico | 13.00 | 13.00 | 0.00 | 39.00 | 39.00 | 0.00 | 0 | T 10/10 • P 1/1 • C 8/8 |
| Faber | 11.00 | 11.00 | 0.00 | 35.00 | 35.00 | 0.00 | 0 | T 10/10 • P 2/2 • C 5/5 |
| Feijão | 15.50 | 15.50 | 0.00 | 31.00 | 31.00 | 0.00 | 0 | T 8/8 • P 1/1 • C 6/6 |
| Felippe Leite | 14.00 | 14.00 | 0.00 | 39.00 | 39.00 | 0.00 | 0 | T 10/10 • P 1/1 • C 8/8 |
| Gui Giron | 11.00 | 11.00 | 0.00 | 35.00 | 35.00 | 0.00 | 0 | T 9/9 • P 1/1 • C 7/7 |
| Ivan | 17.00 | 17.00 | 0.00 | 35.00 | 35.00 | 0.00 | 1 | T 8/8 • P 3/3 • C 4/4 |
| Leo Picca | 12.50 | 12.50 | 0.00 | 34.00 | 34.00 | 0.00 | 0 | T 10/10 • P 0/0 • C 8/8 |
| Leo Raposo | 11.50 | 11.50 | 0.00 | 31.00 | 31.00 | 0.00 | 0 | T 8/8 • P 1/1 • C 6/6 |
| Marcel | 12.00 | 12.00 | 0.00 | 31.00 | 31.00 | 0.00 | 0 | T 10/10 • P 0/0 • C 7/7 |
| Michel | 16.00 | 16.00 | 0.00 | 39.00 | 39.00 | 0.00 | 0 | T 8/8 • P 2/2 • C 7/7 |
| Muca | 12.00 | 12.00 | 0.00 | 26.00 | 26.00 | 0.00 | 0 | T 8/8 • P 0/0 • C 6/6 |
| Nanel | 13.50 | 13.50 | 0.00 | 20.00 | 20.00 | 0.00 | 0 | T 8/8 • P 0/0 • C 4/4 |
| Rafinha | 13.00 | 13.00 | 0.00 | 39.00 | 39.00 | 0.00 | 0 | T 11/11 • P 2/2 • C 6/6 |
| Ranieri | 12.00 | 12.00 | 0.00 | 35.00 | 35.00 | 0.00 | 0 | T 9/9 • P 1/1 • C 7/7 |
| Scarpa | 12.00 | 12.00 | 0.00 | 35.00 | 35.00 | 0.00 | 0 | T 10/10 • P 2/2 • C 5/5 |
| Serginho | 20.50 | 20.50 | 0.00 | 40.00 | 40.00 | 0.00 | 0 | T 9/9 • P 2/2 • C 7/7 |
| Victor | 10.50 | 10.50 | 0.00 | 28.00 | 28.00 | 0.00 | 0 | T 8/8 • P 1/1 • C 5/5 |

## Observações

- Neste workbook, o placar exato substitui a pontuação de tendência no mata-mata. Exemplo: oitavas usam `6` para exato ou `1` para tendência, não `7` acumulado.
- O relatório reconstrói apenas `PLAYOFF_1aFASE` e `OITAVAS`, porque foram as abas pedidas.
- Contagem de `Hope Solo` considera jogos em que exatamente um participante foi o único a acertar o jogo, seja por `placar exato` ou por `tendência`.
