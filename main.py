from lib import func_k, init_perm, inv_init_perm, lshift, perm10, perm8, switch


def gen_subkeys(key):
    print("---- subkeys gen ----")
    perm10_result = perm10(key)
    print("P10 result: " + perm10_result)
    lshift1_result = lshift(perm10_result, 1)
    print("LS1 result: " + lshift1_result)
    lshift2_result = lshift(lshift1_result, 2)
    print("LS2 result: " + lshift2_result)

    subkey1 = perm8(lshift1_result)
    print("Subkey1 (P8 in LS1) result: " + subkey1)
    subkey2 = perm8(lshift2_result)
    print("Subkey2 (P8 in LS2) result: " + subkey2)

    print("---------------------")
    return subkey1, subkey2


def encrypt(plaintext, key):
    subkey1, subkey2 = gen_subkeys(key)

    init_perm_result = init_perm(plaintext)
    print("IP result: " + init_perm_result)
    func_k1_result = func_k(init_perm_result, subkey1)
    print("fk1 result: " + func_k1_result)
    sw_result = switch(func_k1_result)
    print("SW result: " + sw_result)
    func_k2_result = func_k(sw_result, subkey2)
    print("fk2 result: " + func_k2_result)
    ciphertext = inv_init_perm(func_k2_result)
    print("IP^-1 result: " + ciphertext)

    return ciphertext


def decrypt(ciphertext, key):
    subkey1, subkey2 = gen_subkeys(key)

    init_perm_result = init_perm(ciphertext)
    print("IP result: " + init_perm_result)
    func_k2_result = func_k(init_perm_result, subkey2)
    print("fk2 result: " + func_k2_result)
    sw_result = switch(func_k2_result)
    print("SW result: " + sw_result)
    func_k1_result = func_k(sw_result, subkey1)
    print("fk1 result: " + func_k1_result)
    plaintext = inv_init_perm(func_k1_result)
    print("IP^-1 result: " + plaintext)

    return plaintext


key = "1010000010"
plaintext = "11010111"

print()
print("key: " + key)
print("plaintext: " + plaintext)

print("\n-------- encryption --------")
ciphertext = encrypt(plaintext, key)
print("\n> ciphertext: " + ciphertext)

print("\n-------- decryption --------")
plaintext_decrypted = decrypt(ciphertext, key)
print("\n> plaintext decrypted: " + plaintext_decrypted)
print()
