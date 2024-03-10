from math import sqrt


def verify_if_prime_number(n):
    """
    The function verifies whether a given number is a prime number.
    It uses the math property that we have to check only numbers up to sqrt(n) to know all prime numbers up to n.
    If we have a * b == n, and b is larger than the square root of n, the a must be smaller than the square root!
    So by checking only divisors up to the square root we are guaranteed to find a divisor, if any exist.
    :param n: number that should be verified
    :return: True or False
    """
    if n <= 1:
        return False
    else:
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return False
    return True


def verify_if_prime_number_basic(n):
    """
    The function verifies whether a given number is a prime number. Omits even numbers.
    :param n: number that should be verified
    :return: True or False
    """
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n > 2 and n % 2 == 0:
        return False
    else:
        for i in range(3, n, 2):
            if n % i == 0:
                return False
    return True
