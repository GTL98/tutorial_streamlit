def contador_dna(sequencia: str):
    """
    Função responsável por contar quantos nucletídeos há na string de DNA.
    :param sequencia: String com a sequência de DNA.
    :return: Dicionário com a chave sendo o nucleotídeos e o valor a quantidade.
    """
    # --- Dicionário com as informações --- #
    dic_dna = {
        'A': sequencia.count('A'),
        'C': sequencia.count('C'),
        'G': sequencia.count('G'),
        'T': sequencia.count('T')
    }

    return dic_dna
