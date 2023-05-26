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

seq_limit = 30
search_until = 10000
cycles = []
cycle_sets = []

for n in range(2, search_until):
    sequence = [n]
    current_number = n

    for i in range(seq_limit):
        current_number = sum(factorize(current_number))
        
        if current_number == 1:
            break
        elif current_number == n:
            if set(sequence) not in cycle_sets:
                cycles.append(sequence)
                cycle_sets.append(set(sequence))
            break
        sequence.append(current_number)

print(cycles)