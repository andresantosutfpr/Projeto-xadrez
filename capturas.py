def movimento_rei(origem, destino): 
    """
    Verifica se o movimento do rei se válido.
    Parämetros: origem (tuple), destino (tuple)
    retorna: bool
    """
    dif_linha = abs(destino[0] - origem[0])
    dif_coluna = abs(destino[1] - origem[1])

    if dif_linha <= 1 and dif_coluna <= 1 and origem != destino:
       return True
    else:
        return False


if __name__ == "__main__":
    print(movimento_rei((4,4), (5,5)))
    print(movimento_rei((4,4), (6,4)))
    print(movimento_rei((4,4), (4,4)))



def movimento_cavalo(origem, destino):
    """
    Verifica se o movimento do cavalo é válido.
    Parâmetros: origem (tuple), destino (tuple)
    Retorna: bool
    """
    dif_linha = abs(destino[0] - origem[0])
    dif_coluna = abs(destino[1] - origem[1])

    if (dif_linha == 2 and dif_coluna == 1) or (dif_linha == 1 and dif_coluna == 2):
        return True
    else:
        return False

if __name__ == "__main__":
    print(movimento_cavalo((4,4), (6,5)))
    print(movimento_cavalo((4,4), (5,6)))
    print(movimento_cavalo((4,4), (4,4)))
    print(movimento_cavalo((4,7), (4,8)))