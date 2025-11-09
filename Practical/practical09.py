import math

number = 16.78

print("--- Math Module Functions ---")
print("Number:", number)

print("Square root of 16:", math.sqrt(16))

print("Ceiling value of", number, "is:", math.ceil(number))

print("Floor value of", number, "is:", math.floor(number))


import random

print("\n--- Random Module Functions ---")


random_num = random.randint(1, 100)
print("Random number between 1 and 100:", random_num)

random_float = random.random()
print("Random float between 0 and 1:", random_float)

choices = ["Apple", "Banana", "Cherry", "Mango"]
random_choice = random.choice(choices)
print("Random fruit choice:", random_choice)