# 5.You are supplied a file of large nonrepeating set of truly random key letter. Your job is to encrypt the plaintext using ONE TIME PAD technique. Then perform the reverse operation to get original plaintext.

key = ""

with open("One Time Pad Key.txt", "r") as file:
    key = file.read()


def encrypt(plain_text):
    cipher_text = ""
    idx = 0

    for ch in plain_text:
        x = (ord(ch) + ord(key[idx])) % 26
        idx += 1
        cipher_text += chr(ord('A') + x)

    return cipher_text


def decrypt(cipher_text):
    plain_text = ""
    idx = 0

    for ch in cipher_text:
        x = (ord(ch) - ord(key[idx])) % 26
        idx += 1
        plain_text += chr(ord('A') + x)

    return plain_text
plain_text = input("Enter the text to encrypt: ")
cipher_text = encrypt(plain_text)
decrypted_text = decrypt(cipher_text)

print(f"Plain Text: {plain_text}")
print(f"Encrypted Text: {cipher_text}")
print(f"Decrypted Text: {decrypted_text}")

# ANS
# Plain Text: ONETIMEPAD
# Encrypted Text: RSLDIVWSHI
# Decrypted Text: ONETIMEPAD