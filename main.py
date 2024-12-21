from lib import decrypt, encrypt

key = "1010000010"
plaintext = "11010111"

print("key: " + key)
print("plaintext: " + plaintext)

ciphertext = encrypt(plaintext, key)
print("ciphertext: " + ciphertext)

plaintext_decrypted = decrypt(ciphertext, key)
print("plaintext decrypted: " + plaintext_decrypted)
