"""Módulo responsável pelo controle de turnos e pelas regras do peão.

Notes
-----
Brancas ocupam as linhas inferiores do tabuleiro e pretas as superiores.
O turno é sempre representado pelas strings "brancas" e "pretas".

See Also
--------
tabuleiro
    Módulo responsável pela criação e exibição do tabuleiro.
pecas_linha
    Módulo responsável pelos movimentos das peças.
"""

__all__ = ["controlar_turno", "trocar_turno"]

_CASAS_VAZIAS = ["■", "□"]

def controlar_turno(tabuleiro : list[list[str]],linha_origem : int, coluna_origem : int,turno : str) -> bool:
    """Verifica se a peça da casa de origem pertence ao jogador da vez.

    Parameters
    ----------
    tabuleiro : list[list[str]]
        Tabuleiro onde a peça será verificada.
    linha_origem : int
        Linha onde a peça está atualmente.
    coluna_origem : int
        Coluna onde a peça está atualmente.
    turno : str
        Jogador da vez, "brancas" ou "pretas".

    Returns
    -------
    bool
        Retorna True se a peça for do jogador da vez, False se for do
        adversário ou se a casa estiver vazia.

    Notes
    -----
    Casa vazia e peça do adversário retornam False. Se for preciso
    distinguir os dois casos, a checagem da casa vazia deve ser feita
    por quem chama a função.
    """
    peca = tabuleiro[linha_origem][coluna_origem]
    if (peca not in _CASAS_VAZIAS):
        if (peca in ["♙","♖","♘","♗","♕","♔"] and turno == "brancas") or (peca in ["♟","♜","♞","♝","♛","♚"] and turno == "pretas"):
            return True
        else:
            return False
    else:
        return False
      
def trocar_turno(turno : str) -> str:
    """Devolve o turno do jogador seguinte.

    Parameters
    ----------
    turno : str
        Turno atual, "brancas" ou "pretas".

    Returns
    -------
    str
        "pretas" se o turno atual for "brancas", e vice-versa.

    Raises
    ------
    ValueError
        Se o turno recebido não for "brancas" nem "pretas".
    """
    if turno == "brancas":
        return "pretas"
    elif turno == "pretas":
        return "brancas"
    else:
        raise ValueError("Turno inválido")