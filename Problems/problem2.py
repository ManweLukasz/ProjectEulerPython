'''
https://projecteuler.net/problem=2
TODO Zbuduj funkcję, która dla zadanej maksymalnej wartości elementu ciągu Fibonacciego obliczy sumę jego parzystych elementów
'''
from utils import get_input_from_user
from utils import generate_fib_sequence

'''
generuj kolejne liczby fibonacciego...
rob to do czasu az wyraz będzie wynosił > 4000
sumuj parzyste..

'''


def sum_of_even_values_terms_fibo_sequence_below_given_value(v):
    suma = 0
    fibo_term_minus_2, fibo_term_minus_1 = 0, 1
    while True:
        fibo_term = fibo_term_minus_1 + fibo_term_minus_2
        if fibo_term > v:
            return suma
        if fibo_term % 2 == 0:
            suma += fibo_term
        fibo_term_minus_2, fibo_term_minus_1 = fibo_term_minus_1, fibo_term


if __name__ == '__main__':
    number = get_input_from_user("Podaj dowolną liczbę większą od zera", float, 0)
    result = sum_of_even_values_terms_fibo_sequence_below_given_value(number)
    print(result)


