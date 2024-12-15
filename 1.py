# 1. Suppose you are given a line of text as a plaintext, find out the corresponding Caesar Cipher (i.e. character three to the right modulo 26). Then perform the reverse operation to get original plaintext.

def encrypt(plain_text):
    cipher_text = ""

    for ch in plain_text:
        if ch.isalpha():
            ch = chr(ord(ch) + 3)
            if ch.isalpha() != True:
                ch = chr(ord(ch) - 26)
        cipher_text += ch
    
    return cipher_text


def decrypt(cipher_text):
    plain_text = ""

    for ch in cipher_text:
        if ch.isalpha():
            ch = chr(ord(ch) - 3)
            if ch.isalpha() != True:
                ch = chr(ord(ch) + 26)
        plain_text += ch
    
    return plain_text


plain_text = "RuCse27 x @101"
cipher_text = encrypt(plain_text)
decrypted_text = decrypt(cipher_text)

print(f"Plain Text: {plain_text}")
print(f"Encrypted Text: {cipher_text}")
print(f"Decrypted Text: {decrypted_text}")

# ANS
# Plain Text: RuCse27 x @101
# Encrypted Text: UxFvh27 a @101
# Decrypted Text: RuCse27 x @101
