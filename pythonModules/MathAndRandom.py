import math

num = 4
print("f Factorila of number is {num}", math.factorial(num))
print(round(1.59))
print(math.ceil(1.59))
# Numby
print(math.pi)
print(math.e)
print(math.sin(0))
print(math.cos(0))
# RANDOM
import random

print(random.randint(0, 10))
print(random.seed(11))
print(
    random.randint(0, 10)
)  # used to generate random number with specified time period
# The value 101 is completely arbitrary, you can pass in any number you want
print(random.seed(101))
# You can run this cell as many times as you want, it will always return the same number
print(random.randint(0, 100))
