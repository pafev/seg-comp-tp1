def init_perm(text):
    return text[1] + text[5] + text[2] + text[0] + text[3] + text[7] + text[4] + text[6]


def xor(text1, text2, bits_qty):
    result_num = int(text1, 2) ^ int(text2, 2)
    return bin(result_num)[2:].zfill(bits_qty)


def mapping_F(text, subkey):
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
    half_size = len(text) // 2
    left_half = text[0:half_size]
    right_half = text[half_size:]
    result = xor(left_half, mapping_F(right_half, subkey), 4) + right_half
    return result


def switch(text):
    half_size = len(text) // 2
    first_half = text[0:half_size]
    second_half = text[half_size:]
    return second_half + first_half


def inv_init_perm(text):
    return text[3] + text[0] + text[2] + text[4] + text[6] + text[1] + text[7] + text[5]


def perm10(key):
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
    return key[5] + key[2] + key[6] + key[3] + key[7] + key[4] + key[9] + key[8]
