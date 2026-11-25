"""Módulo com a finalidade de verificar se o movimento da peça específica é válido ou inválido.

Notes
-----
Esse modulo foi criado pelo Luiz Gustavo(Github: Surslide) 
O código prioriza legibilidade em vez de otimização, devido à natureza do projeto que não processa muitos dados.

See Also
--------
tabuleiro
    Módulo criado por Yuki, responsável pela execução do jogo de xadrez.
capturas
    Módulo criado por Danilo, responsável pela validação do movimento do rei e do cavalo
"""
from capturas import (movimento_rei, movimento_cavalo)
__all__ = ["caminho_livre"]

_PERMITIDOS = ["■", "□"] #constante global, hash set seria uma melhor pratica

def _movimento_torre(linha_origem : int, coluna_origem : int, linha_destino : int, coluna_destino : int, tabuleiro : list[list[str]]) -> bool:
    """Verifica se a torre mover da origem ao destino é um movimento válido.
    
    Parameters
    ----------
    linha_origem : int
        Linha onde a torre está atualmente.
    coluna_origem : int
        Coluna onde a torre está atualmente.
    linha_destino : int
        Linha onde a torre quer chegar.
    coluna_destino : int
        Coluna onde a torre quer chegar.
    tabuleiro : list[list[str]]
        Tabuleiro onde será verificado se movimento é válido.
    
    Returns
    -------
    bool
        Retorna True se o movimento for válido, False se for inválido.
    """
    moveu_esquerda = coluna_origem > coluna_destino
    moveu_direita = coluna_origem < coluna_destino
    moveu_cima = linha_origem > linha_destino
    moveu_baixo = linha_origem < linha_destino
    if moveu_esquerda + moveu_direita + moveu_cima + moveu_baixo != 1:
        return False
    if moveu_esquerda:
        for elemento in tabuleiro[linha_destino][coluna_origem - 1:coluna_destino:-1]:
            if elemento not in _PERMITIDOS:
                return False
    elif moveu_direita:
        for elemento in tabuleiro[linha_destino][coluna_origem + 1:coluna_destino:1]:
            if elemento not in _PERMITIDOS:
                return False
    elif moveu_cima:
        for linha in tabuleiro[linha_origem - 1:linha_destino:-1]:
            if linha[coluna_destino] not in _PERMITIDOS:
                return False
    elif moveu_baixo:
        for linha in tabuleiro[linha_origem + 1:linha_destino:1]:
            if linha[coluna_destino] not in _PERMITIDOS:
                return False      
    return True

def _movimento_bispo(linha_origem : int, coluna_origem : int, linha_destino : int, coluna_destino : int, tabuleiro : list[list[str]]) -> bool:
    """Verifica se o bispo mover da origem ao destino é um movimento válido.
    
    Parameters
    ----------
    linha_origem : int
        Linha onde o bispo está atualmente.
    coluna_origem : int
        Coluna onde o bispo está atualmente.
    linha_destino : int
        Linha onde o bispo quer chegar.
    coluna_destino : int
        Coluna onde o bispo quer chegar.
    tabuleiro : list[list[str]]
        Tabuleiro onde será verificado se movimento é válido.
    
    Returns
    -------
    bool
        Retorna True se o movimento for válido, False se for inválido.
    """
    dif_linha = abs(linha_destino - linha_origem)
    dif_coluna = abs(coluna_destino - coluna_origem)
    if dif_linha != dif_coluna or dif_linha == 0:
        return False
    moveu_noroeste = linha_origem > linha_destino and coluna_origem > coluna_destino
    moveu_nordeste = linha_origem > linha_destino and coluna_origem < coluna_destino
    moveu_sudoeste = linha_origem < linha_destino and coluna_origem > coluna_destino
    moveu_sudeste = linha_origem < linha_destino and coluna_origem < coluna_destino
    if moveu_noroeste:
        for i in range(1, dif_linha):
            if tabuleiro[linha_origem - i][coluna_origem - i] not in _PERMITIDOS:
                return False
    elif moveu_nordeste:
        for i in range(1, dif_linha):
            if tabuleiro[linha_origem - i][coluna_origem + i] not in _PERMITIDOS:
                return False
    elif moveu_sudoeste:
        for i in range(1, dif_linha):
            if tabuleiro[linha_origem + i][coluna_origem - i] not in _PERMITIDOS:
                return False
    elif moveu_sudeste:
        for i in range(1, dif_linha):
            if tabuleiro[linha_origem + i][coluna_origem + i] not in _PERMITIDOS:
                return False
    return True

def _movimento_dama(linha_origem : int, coluna_origem : int, linha_destino : int, coluna_destino : int, tabuleiro : list[list[str]]) -> bool:
    """Verifica se a dama mover da origem ao destino é um movimento válido.
    
    Parameters
    ----------
    linha_origem : int
        Linha onde a dama está atualmente.
    coluna_origem : int
        Coluna onde a dama está atualmente.
    linha_destino : int
        Linha onde a dama quer chegar.
    coluna_destino : int
        Coluna onde a dama quer chegar.
    tabuleiro : list[list[str]]
        Tabuleiro onde será verificado se movimento é válido.
    
    Returns
    -------
    bool
        Retorna True se o movimento for válido, False se for inválido.
    
    Notes
    -----
    Foi reutilizado a função de torres e bispos para verificar o movimento da dama.

    See Also
    --------
    _movimento_bispo
        Verifica se o bispo mover da origem ao destino é um movimento válido.
    _movimento_torre
        Verifica se a torre mover da origem ao destino é um movimento válido.
    """ 
    if _movimento_bispo(linha_origem, coluna_origem, linha_destino, coluna_destino, tabuleiro):
        return True
    return _movimento_torre(linha_origem, coluna_origem, linha_destino, coluna_destino, tabuleiro)

def caminho_livre(linha_origem : int, coluna_origem : int, linha_destino : int, coluna_destino : int, peca : str, tabuleiro : list[list[str]]) -> bool:
    """Verifica se a peça mover da origem ao destino é um movimento válido.
    
    Essa função deve impedir que Torres, Bispos e Damas atravessem peças.

    Parameters
    ----------
    linha_origem : int
        Linha onde a peça está atualmente.
    coluna_origem : int
        Coluna onde a peça está atualmente.
    linha_destino : int
        Linha onde a peça quer chegar.
    coluna_destino : int
        Coluna onde a peça quer chegar.
    peca : str
        Peça que será verificada se o movimento é válido.
    tabuleiro : list[list[str]]
        Tabuleiro onde será verificado se movimento é válido.
    
    Returns
    -------
    bool
        Retorna True se o movimento for válido, False se for inválido.
    
    See Also
    --------
    _movimento_torre
        Verifica se a torre mover da origem ao destino é um movimento válido.
    _movimento_bispo
        Verifica se o bispo mover da origem ao destino é um movimento válido.
    _movimento_dama
        Verifica se a dama mover da origem ao destino é um movimento válido.
    """
    if peca in ["♜", "♖"]:
        return _movimento_torre(linha_origem, coluna_origem, linha_destino, coluna_destino, tabuleiro)
    elif peca in ["♝", "♗"]:
        return _movimento_bispo(linha_origem, coluna_origem, linha_destino, coluna_destino, tabuleiro)
    elif peca in ["♛", "♕"]:
        return _movimento_dama(linha_origem, coluna_origem, linha_destino, coluna_destino, tabuleiro)
    elif peca in ["♞", "♘"]:
        return movimento_cavalo((linha_origem, coluna_origem), (linha_destino, coluna_destino))
    elif peca in ["♚", "♔"]:
        return movimento_rei((linha_origem, coluna_origem), (linha_destino, coluna_destino))
    return False
