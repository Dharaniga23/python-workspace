import random
import string

chars = " " + string.digits + string.ascii_letters + string.punctuation
chars = list(chars)
keys = chars.copy()

random.shuffle(keys)
#print(f"chars:{chars}")
#print(f"keys :{keys}")

plaintext = input("Enter the plain text:")
ciphertext = ""

for letter in plaintext:
    index =chars.index(letter)
    ciphertext += keys[index]

print(f"Original text: {plaintext}")
print(f"Encrypted text: {ciphertext}")

ciphertext = input("Enter the cipher text:")
plaintext = ""

for letter in ciphertext:
    index =keys.index(letter)
    plaintext += chars[index]

print(f"Encrypted text: {ciphertext}")
print(f"Original text: {plaintext}")
