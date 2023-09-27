"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def check_prime(num, prime_list) -> bool:
    """Checks if a given number is a prime by comparing against existing prime numbers"""
    is_prime = True
    prime_count = 0
    while is_prime and prime_count < len(prime_list):
        if num % prime_list[prime_count] == 0:
            is_prime = False
        else:
            prime_count += 1
    return is_prime

def get_next_prime(existing_prime_list) -> int:
    """generates the next prime number, accoriding to the given list"""

    # First prime in sequence
    num = 2
    while True:
        if check_prime(num, existing_prime_list):
            # yield halts generator until called again
            yield num
            num += 1
        else:
            num += 1


def primes(number_of_primes:int):
    """Generates a list of prime numbers up to a given size"""
    
    # Checks if parameter is less than 1
    if number_of_primes < 1:
        raise ValueError
    # Checks if parameter is an integer
    if number_of_primes.as_integer_ratio()[1] > 1:
        raise ValueError
    list = []
    for i in range(number_of_primes):
        gen = get_next_prime(list)
        list.append(next(gen))
    return list
