# 7.Use the Robin-Miller algorithm to check whether the given number P is prime or not?
import random

def miller_rabin_test(P, k=5):
    # Handle edge cases
    if P == 2 or P == 3:
        return True
    if P <= 1 or P % 2 == 0:
        return False

    # Step 1: Write P-1 as 2^s * d
    s = 0
    d = P - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    # Step 2: Perform the test 'k' times to improve accuracy
    for _ in range(k):
        # Choose a random integer 'a' in the range [2, P-2]
        a = random.randint(2, P - 2)
        
        # Compute x = a^d % P
        x = pow(a, d, P)
        
        # If x is 1 or P-1, P is a probable prime for this round
        if x == 1 or x == P - 1:
            continue
        
        # Step 5: Repeatedly square x up to s-1 times
        for _ in range(s - 1):
            x = pow(x, 2, P)
            if x == P - 1:
                break
        else:
            # If none of the conditions are met, P is composite
            return False

    # If P passed all rounds, it's probably prime
    return True

# Take input from the user
P = int(input("Enter a number to check if it is prime: "))

if miller_rabin_test(P):
    print(f"{P} is probably prime.")
else:
    print(f"{P} is composite.")
