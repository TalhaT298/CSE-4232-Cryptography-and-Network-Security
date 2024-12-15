# 2.Find out the Polygram Substitution Cipher of a given plaintext (Consider the block size of 3). Then perform the reverse operation to get original plaintext.

encryption_rules, decryption_rules = {}, {}

# Read the Polygram Blocks from a file and generate encryption and decryption rules
with open("Polygram Blocks.txt", "r") as file:
    content = file.read()
    words = content.split()

# Populate the encryption and decryption dictionaries
for i in range(0, len(words), 2):
    word1, word2 = words[i], words[i + 1]
    encryption_rules[word1] = word2
    decryption_rules[word2] = word1

# Function to encrypt plain text
def encrypt(plain_text):
    cipher_text = ""
    block = ""

    for i in range(len(plain_text)):
        block += plain_text[i]
        if (i + 1) % 3 == 0:
            cipher_text += encryption_rules.get(block, block)  # Encrypt the block if possible
            block = ""

    if block:  # Add the remaining block if it's not empty
        cipher_text += encryption_rules.get(block, block)

    return cipher_text

# Function to decrypt cipher text
def decrypt(cipher_text):
    plain_text = ""
    block = ""

    for i in range(len(cipher_text)):
        block += cipher_text[i]
        if (i + 1) % 3 == 0:
            plain_text += decryption_rules.get(block, block)  # Decrypt the block if possible
            block = ""

    if block:  # Add the remaining block if it's not empty
        plain_text += decryption_rules.get(block, block)

    return plain_text

# Input from user
plain_text = input("Enter the text to encrypt: ")
cipher_text = encrypt(plain_text)
decrypted_text = decrypt(cipher_text)  # Call the decrypt function

# Display the results
print(f"Plain Text: {plain_text}")
print(f"Encrypted Text: {cipher_text}")
print(f"Decrypted Text: {decrypted_text}")
