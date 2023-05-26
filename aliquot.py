import math

def factorize(n):
    factors = {1}
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
            x = factorize(n // i)
            factors.update(x)
            factors.update({factor*i for factor in x})
            return factors
    return factors

def get_sequence(n):
    current_number = n
    sequence = [n]
    previous_number = n
    while True:
        current_number = sum(factorize(current_number))
        sequence.append(current_number)
        if current_number == 1 or current_number == n or previous_number == current_number:
            return sequence
        previous_number = current_number