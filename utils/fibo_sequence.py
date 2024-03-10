def generate_fib_sequence(n: int) -> []:
    '''
    Generating Fibonacci sequence up to a given n-th term.
    :param n: int
    :return: list with Fibonacci numbers
    '''
    fibo_numbers = [0, 1]
    if n == 1:
        return [fibo_numbers[0]]
    elif n == 2:
        return fibo_numbers
    else:
        for i in range(3, n + 1):
            fibo_numbers.append(fibo_numbers[-1] + fibo_numbers[-2])
    return fibo_numbers
