# Projeto-Xadrez
Projeto Integrador de Lógica de Programação:um sistema completo de xadrez em Python, feito em equipe, usando funções, matrizes e validação de regras.

# Como o tabuleiro é represntado
O tabuleiro é uma matriz 8x8 (lista de ,istas de string). As casas vazias guardam □ ou ■, que são as cores das casas, enão existe um valor None.

| Peças  | Brancas | Pretas |
| ------------- | ------------- |
| Peão  | ♙ | ♟ |
| Torre  | ♖  | ♜ |
| Cavalo  | ♘  | ♞ |
| Bispo  | ♗  | ♝ |
| Dama  | ♕  | ♛ |
| Rei  | ♔  | ♚ |

-As pretas começam nas linhas 0 e 1, e as brancas nas linhas 6 e 7.
-As posições são tuplas (linha,coluna) com índices de 0 a 7. A linha 0
