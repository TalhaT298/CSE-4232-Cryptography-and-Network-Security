# 10. Encrypt the plaintext message using RSA algorithm. Then perform the reverse operation to get original plaintext.

from sympy import mod_inverse
import random

# Helper function to check for prime numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate RSA keys (public and private)
def generate_rsa_keys():
    # Step 1: Choose two large prime numbers p and q
    primes = [i for i in range(100, 200) if is_prime(i)]
    p = random.choice(primes)
    q = random.choice(primes)
    
    # Step 2: Compute n = p * q
    n = p * q
    
    # Step 3: Compute phi(n) = (p-1)*(q-1)
    phi_n = (p - 1) * (q - 1)
    
    # Step 4: Choose e (public exponent), where 1 < e < phi(n) and gcd(e, phi_n) = 1
    e = random.choice([i for i in range(2, phi_n) if is_prime(i)])
    
    # Step 5: Compute the private key d (modular inverse of e mod phi(n))
    d = mod_inverse(e, phi_n)
    
    # Public key (e, n) and private key (d, n)
    return (e, n), (d, n)

# Function to encrypt the message using public key
def rsa_encrypt(plaintext, public_key):
    e, n = public_key
    # Convert each character to its ASCII value and encrypt
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

# Function to decrypt the message using private key
def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    # Decrypt each number and convert back to the character
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return decrypted_message

# Example usage
public_key, private_key = generate_rsa_keys()

# Input plaintext from the user
plaintext = input("Enter the message to encrypt: ")

# Encrypt the plaintext
ciphertext = rsa_encrypt(plaintext, public_key)
print(f"Encrypted message: {ciphertext}")

# Decrypt the ciphertext
decrypted_message = rsa_decrypt(ciphertext, private_key)
print(f"Decrypted message: {decrypted_message}")

# ANS
# Enter the message to encrypt: Hello
# Encrypted message: [<encrypted integers>]
# Decrypted message: Hello