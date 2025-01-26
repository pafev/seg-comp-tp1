def init_perm(text):
    return text[1] + text[5] + text[2] + text[0] + text[3] + text[7] + text[4] + text[6]


def xor(text1, text2, bits_qty):
    """
    Realiza a operação XOR entre dois textos binários.

    Args:
        text1 (str): Primeiro texto binário.
        text2 (str): Segundo texto binário.
        bits_qty (int): Quantidade de bits do resultado.

    Returns:
        str: Resultado da operação XOR com a quantidade de bits especificada.
    """
    result_num = int(text1, 2) ^ int(text2, 2)
    return bin(result_num)[2:].zfill(bits_qty)


def mapping_F(text, subkey):
    """
    Realiza a função de mapeamento F usando caixas S.

    Args:
        text (str): Texto de entrada.
        subkey (str): Subchave para a operação XOR.

    Returns:
        str: Resultado da função de mapeamento F.
    """
    s0_box = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]

    s1_box = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

    ep_result = (
        text[3] + text[0] + text[1] + text[2] + text[1] + text[2] + text[3] + text[0]
    )
    preceding_matrix = xor(ep_result, subkey, 8)
    s0_box_row = int(preceding_matrix[0] + preceding_matrix[3], 2)
    s0_box_column = int(preceding_matrix[1] + preceding_matrix[2], 2)
    s1_box_row = int(preceding_matrix[4] + preceding_matrix[7], 2)
    s1_box_column = int(preceding_matrix[5] + preceding_matrix[6], 2)
    output_s_boxes = bin(s0_box[s0_box_row][s0_box_column])[2:].zfill(2) + bin(
        s1_box[s1_box_row][s1_box_column]
    )[2:].zfill(2)
    return output_s_boxes[1] + output_s_boxes[3] + output_s_boxes[2] + output_s_boxes[0]


def func_k(text, subkey):
    """
    Aplica a função K ao texto usando a subchave fornecida.

    Args:
        text (str): Texto de entrada.
        subkey (str): Subchave para a função de mapeamento F.

    Returns:
        str: Resultado da função K.
    """
    half_size = len(text) // 2
    left_half = text[0:half_size]
    right_half = text[half_size:]
    result = xor(left_half, mapping_F(right_half, subkey), 4) + right_half
    return result


def switch(text):
    """
    Troca as metades do texto.

    Args:
        text (str): Texto de entrada.

    Returns:
        str: Texto com as metades trocadas.
    """
    half_size = len(text) // 2
    first_half = text[0:half_size]
    second_half = text[half_size:]
    return second_half + first_half


def inv_init_perm(text):
    """
    Realiza a permutação inicial inversa do texto.

    Args:
        text (str): Texto de entrada.

    Returns:
        str: Texto permutado inversamente.
    """
    return text[3] + text[0] + text[2] + text[4] + text[6] + text[1] + text[7] + text[5]


def perm10(key):
    """
    Realiza a permutação P10 na chave.

    Args:
        key (str): Chave de entrada.

    Returns:
        str: Chave permutada.
    """
    return (
        key[2]
        + key[4]
        + key[1]
        + key[6]
        + key[3]
        + key[9]
        + key[0]
        + key[8]
        + key[7]
        + key[5]
    )


def lshift(text, qty):
    """
    Realiza a rotação à esquerda no texto.

    Args:
        text (str): Texto de entrada.
        qty (int): Quantidade de posições para rotacionar.

    Returns:
        str: Texto rotacionado.
    """
    half_size = len(text) // 2
    first_half = text[0:half_size]
    second_half = text[half_size:]
    first_half_shifted = list(first_half)
    second_half_shifted = list(second_half)
    for i in range(half_size):
        first_half_shifted[i % half_size - qty] = first_half[i]
        second_half_shifted[i % half_size - qty] = second_half[i]
    return "".join(first_half_shifted + second_half_shifted)


def perm8(key):
    """
    Realiza a permutação P8 na chave.

    Args:
        key (str): Chave de entrada.

    Returns:
        str: Chave permutada.
    """
    return key[5] + key[2] + key[6] + key[3] + key[7] + key[4] + key[9] + key[8]
