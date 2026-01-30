'''
Quick rough work to understand problem and develop any possible patterns:

k = 1:
First prime: 2
Numbers: 3, 5, 7, 9
n: 9 (divisible by 2nd prime: 3)

k = 2:
First 2 primes: 2, 3
Numbers: 5, 7, 11, 13, 17, 19, 23, 25
n: 25 (divisible by 3rd prime: 5)

k = 3:
First 3 primes: 2, 3, 5
Numbers: 7, 11, 13, 17, 19, 23, 31, 37, 41, 47, 49
n: 49 (divisible by 4th prime: 7)

k = 4:
First 4 primes: 2, 3, 5, 7
Numbers: 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 121
n: 121 (divisible by 5th prime: 11)



Is n always ((k+1)th prime)^2?

'''
import math

k = int(input())
k_primes = [2]
m = 3

while len(k_primes) < (k+1):
    prime = True
    n = 2
    while n <= (math.ceil(m/2)):
        if (m % n) == 0:
            prime = False
            break

        # Increment n to odd numbers only as all prime numbers (except 2) are odd and odd numbers, if co-prime, have odd divisors
        if (n % 2) == 0:
            n += 1
        else:
            n += 2
    
    if prime == True:
        k_primes.append(m)

    # Increment m to odd numbers only as all prime numbers (except 2) are odd
    if (m % 2) == 0:
        m += 1
    else:
        m += 2

kPlusOneThPrime = k_primes[-1]
print(kPlusOneThPrime ** 2)
