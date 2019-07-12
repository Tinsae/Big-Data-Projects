from random import randint, choice
rand_numbers = []
divisible = [n for n in range(1, 1001) if n % 35 == 0]
# repetition is possible
print([choice(divisible) for i in range(5)])