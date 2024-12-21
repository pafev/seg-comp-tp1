from lib import func_k, init_perm, inv_init_perm, lshift, perm10, perm8, switch


def gen_subkeys(key):
    key1 = perm8(lshift(perm10(key), 1))
    key2 = perm8(lshift(lshift(perm10(key), 1), 2))
    return key1, key2


def encrypt(plaintext, key):
    key1, key2 = gen_subkeys(key)
    ciphertext = inv_init_perm(func_k(switch(func_k(init_perm(plaintext), key1)), key2))
    return "".join(ciphertext)


def decrypt(ciphertext, key):
    key1, key2 = gen_subkeys(key)
    plaintext = inv_init_perm(func_k(switch(func_k(init_perm(ciphertext), key2)), key1))
    return "".join(plaintext)


key = "1010000010"
plaintext = "11010111"

print("key: " + key)
print("plaintext: " + plaintext)

ciphertext = encrypt(plaintext, key)
print("ciphertext: " + ciphertext)

plaintext_decrypted = decrypt(ciphertext, key)
print("plaintext decrypted: " + plaintext_decrypted)
