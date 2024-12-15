# 11. Write a program to implement Diffie-Hellman Key Exchange.

import random

def diffie_hellman(prime, primitive_root):
    XA = random.randint(1, prime - 1) # Randomly generating A's private key
    YA = pow(primitive_root, XA, prime) # Calculating A's public key
    print(f"A's private key is {XA} & public key is {YA}")

    XB = random.randint(1, prime - 1) # Randomly generating B's private key
    YB = pow(primitive_root, XB, prime) # Calculating B's public key
    print(f"B's private key is {XB} & public key is {YB}")

    KA = pow(YB, XA, prime) # Computing the common key at A's end from B's public key
    KB = pow(YB, XA, prime) # Computing the common key at B's end from A's public key

    print(f"The common key generated at A's end is {KA} & B's end is {KB}")
prime = 253
primitive_root = 3
diffie_hellman(prime, primitive_root)

# ANS
# A's private key is 21 & public key is 146
# B's private key is 223 & public key is 27
# The common key generated at A's end is 236 & B's end is 236