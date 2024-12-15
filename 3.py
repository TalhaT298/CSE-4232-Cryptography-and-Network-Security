# 3.Consider the plaintext "DEPARTMENT OF COMPUTER SCIENCE AND TECHNOLY UNIVERSITY OF RAJSHAHI BANGLADESH", find out the corresponding Transposition Cipher (Take width as input). Then perform the reverse operation to get original plaintext.

# Function to perform Transposition Cipher
def encrypt_transposition(plaintext, width):
    ciphertext = [''] * width
    for col in range(width):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += width
    return ''.join(ciphertext)

# Function to reverse the Transposition Cipher (decrypt)
def decrypt_transposition(ciphertext, width):
    rows = len(ciphertext) // width
    extra = len(ciphertext) % width
    total_rows = rows + 1 if extra != 0 else rows
    
    plaintext = [''] * len(ciphertext)
    
    col = 0
    row = 0
    for i, symbol in enumerate(ciphertext):
        if row == total_rows - 1 and col >= extra:
            row = 0
            col += 1
        plaintext[row * width + col] = symbol
        row += 1
        if row == total_rows:
            row = 0
            col += 1

    return ''.join(plaintext)

# Example usage
plaintext = "DEPARTMENT OF COMPUTER SCIENCE AND TECHNOLY UNIVERSITY OF RAJSHAHI BANGLADESH".replace(" ", "")
width = 8

# Encrypt and decrypt
encrypted = encrypt_transposition(plaintext, width)
decrypted = decrypt_transposition(encrypted, width)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

# ANS
# Encrypted: DNUNCIOHDETTCHVFIEPOEENERBSAFRAORAAHRCSNLSJNTOCDYISGMMITUTHLEPEENYAA
# Decrypted: DEPARTMENTOFCOMPUTERSCIENCEANDTECHNOLYUNIVERSITYOFRAJSHAHIBANGLADESH