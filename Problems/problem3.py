'''
https://projecteuler.net/problem=3
Zbuduj funkcje, która poda najwyższy dzielnik wpisanej liczby całkowitej
'''
from utils import get_input_from_user, verify_if_prime_number

'''
Liczba pierwsza to taka liczba, która jest podzielna przez 1 i przez sama siebie...

1) jeśli liczba jest factorem.....
2) i do tego jest liczbą pierwszą, to ... wtedy jest prime factor

Należy zastosować tutaj "sito kwadratowe"
https://pl.wikipedia.org/wiki/Sito_kwadratowe

'''


def calculate_prime_factors(n):
    i = 1
    prime_factors = []
    while True:
        if n % i == 0 and verify_if_prime_number(i):
            prime_factors.append(i)
        if i >= n:
            return prime_factors
        else:
            i += 1


def calculate_largest_prime_factor(n):
    if n % 2 == 0:
        i = n / 2
        while True:
            if n % i == 0 and verify_if_prime_number(i):
                return i
            if n == 2:
                return 2
            else:
                i -= 1
    else:
        i = n // 3
        while True:
            if n % i == 0 and verify_if_prime_number(i):
                return i
            if n < 2:
                return 1
            else:
                i -= 2


user_answer = get_input_from_user("Provide a number", int)
r1 = calculate_prime_factors(user_answer)
print(r1)
r2 = calculate_largest_prime_factor(user_answer)
print(r2)

