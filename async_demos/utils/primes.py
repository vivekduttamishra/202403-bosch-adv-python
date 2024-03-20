from utils.decorators import performance

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

@performance
def find_primes(min,max=None):
    if max is None:
        min,max=0,min

    primes = []
    for i in range(min, max):
        if is_prime(i):
            primes.append(i)
    return primes


def prime_generator(min,max):
    if max is None:
        min,max=0,min

    for i in range(min,max):
        if is_prime(i):
            yield i