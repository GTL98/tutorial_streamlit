# --- Importar a biblioteca --- #
from random import choice


def gerardor_dna(quantidade: int):
    """
    Função responsável por criar uma sequência de DNA aleatória.
    :param quantidade: Quantidade de nucleotídeos.
    :return: String com o DNA completo.
    """
    # --- Lista com os nucleotídeos --- #
    nucleotideos = [
        'A',
        'C',
        'G',
        'T'
    ]

    # --- Variável para armazenar o DNA --- #
    dna = ''

    # --- Loop para adicionar o nucleotídeo ao DNA --- #
    while len(dna) < quantidade:
        nucleotideo = choice(nucleotideos)
        dna += nucleotideo

    return dna
