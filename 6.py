# 6.Use the Lehmann algorithm to check whether the given number P is prime or not?
import random


def lehmann_primality_test(P, iterations=5):
    if P <= 1:
        return False
    if P == 2:
        return True

    # Perform the test 'iterations' times
    for _ in range(iterations):
        # Randomly choose 'a' in the range [2, P-2]
        a = random.randint(2, P - 2)

        # Compute r = a^((P-1)/2) % P
        r = pow(a, (P - 1) // 2, P)

        # If r is not 1 and not P-1, then P is composite
        if r != 1 and r != P - 1:
            return False

    # If all tests passed, P is probably prime
    return True


# Take input from the user
P = int(input("Enter a number to check if it is prime: "))

if lehmann_primality_test(P):
    print(f"{P} is probably prime.")
else:
    print(f"{P} is composite.")
