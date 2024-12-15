# Function to encrypt text using Caesar Cipher
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text


# Function to decrypt text using Caesar Cipher
def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)


# Function to encrypt text using Transposition Cipher
def transposition_cipher_encrypt(text, width):
    ciphertext = [''] * width
    for column in range(width):
        pointer = column
        while pointer < len(text):
            ciphertext[column] += text[pointer]
            pointer += width
    return ''.join(ciphertext)


# Function to decrypt text using Transposition Cipher
def transposition_cipher_decrypt(text, width):
    num_of_columns = len(text) // width
    num_of_rows = width
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(text)

    plaintext = [''] * num_of_columns
    column = 0
    row = 0

    for symbol in text:
        plaintext[column] += symbol
        column += 1

        if (column == num_of_columns) or (column == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            column = 0
            row += 1

    return ''.join(plaintext)


# Example usage
plaintext = "Computer Science"
shift = 3
width = 5

# Encryption
caesar_encrypted = caesar_cipher_encrypt(plaintext, shift)
transposition_encrypted = transposition_cipher_encrypt(caesar_encrypted, width)
print(f"Plaintext: {plaintext}")
print(f"Caesar Cipher: {caesar_encrypted}")
print(f"Transposition Cipher: {transposition_encrypted}")

# Decryption
transposition_decrypted = transposition_cipher_decrypt(transposition_encrypted, width)
caesar_decrypted = caesar_cipher_decrypt(transposition_decrypted, shift)
print(f"Decrypted Text: {caesar_decrypted}")


# ANS:
# Plaintext: Computer Science
# Caesar Cipher: Frpsxwhu Vflhqfh
# Transposition Cipher: Fwfhrhlpuhs qxVf
# Decrypted Text: Ceienctompucer S
