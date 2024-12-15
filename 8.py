# 8.Write a program to implement MD5 one way hash function.

import hashlib


def md5_hash(input_string):
    # Create an md5 hash object
    md5_hasher = hashlib.md5()

    # Convert the input string to bytes and update the hash object
    md5_hasher.update(input_string.encode('utf-8'))

    # Get the hexadecimal digest of the hash
    return md5_hasher.hexdigest()


# Take input from the user
input_string = input("Enter the string to hash using MD5: ")

# Compute and print the MD5 hash
hashed_value = md5_hash(input_string)
print(f"MD5 Hash of '{input_string}' is: {hashed_value}")

# ANS
# Enter the string to hash using MD5: HelloWorld
# MD5 Hash of 'HelloWorld' is: 68e109f0f40ca72a15e05cc22786f8e6