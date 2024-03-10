'''
https://projecteuler.net/problem=1
<p>If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$.
The sum of these multiples is $23$.</p>
<p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>
'''
from utils import get_input_from_user


def sum_of_multiples_3_and_5_below_given_number(x):
    suma = 0
    for i in range(x):
        if i % 3 == 0 or i % 5 == 0:
            suma += i
    return suma


if __name__ == '__main__':
    number = get_input_from_user(request="Podaj liczbę całkowitą.", input_type=int)
    result = sum_of_multiples_3_and_5_below_given_number(number)
    print(result)
