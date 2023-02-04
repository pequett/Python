#  Finds the Primes from 0 to a number specified
#  9/27/2022 Malachi Campomizzi

def is_prime(n):
    if n > 1:
        for i in range(2, n - 1):
            if n % i != 0:
                continue
            else:
                return False
        return True
    else:
        return False

num = int(input("--> "))

for i in range(num):
    if is_prime(i) == True:
        print(i, True)
