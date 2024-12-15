# 9. Write a program to implement Secured Hash Algorithm (SHA) one way hash function.
import hashlib

def sha_hash(input_string, algorithm="sha256"):
    # Select the appropriate hash function based on the given algorithm
    if algorithm.lower() == "sha1":
        hasher = hashlib.sha1()
    elif algorithm.lower() == "sha224":
        hasher = hashlib.sha224()
    elif algorithm.lower() == "sha256":
        hasher = hashlib.sha256()
    elif algorithm.lower() == "sha384":
        hasher = hashlib.sha384()
    elif algorithm.lower() == "sha512":
        hasher = hashlib.sha512()
    else:
        raise ValueError("Unsupported SHA algorithm. Choose from 'sha1', 'sha224', 'sha256', 'sha384', or 'sha512'.")
    
    # Encode the input string and update the hash object
    hasher.update(input_string.encode('utf-8'))
    
    # Return the hexadecimal digest of the hash
    return hasher.hexdigest()

# Take input from the user
input_string = input("Enter the string to hash: ")
algorithm = input("Choose SHA algorithm (sha1, sha224, sha256, sha384, sha512): ")

# Compute and print the hash
try:
    hashed_value = sha_hash(input_string, algorithm)
    print(f"{algorithm.upper()} Hash of '{input_string}' is: {hashed_value}")
except ValueError as e:
    print(e)


# ANS
# Enter the string to hash: HelloWorld
# Choose SHA algorithm (sha1, sha224, sha256, sha384, sha512): sha256
# SHA256 Hash of 'HelloWorld' is: 872e4e50ce9990d8b041330c47c9ddd11bec6b503ae9386a99da8584e9bb12c4