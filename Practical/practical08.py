def print_string(text):
    print("The entered string is:", text)

print_string("Hello, Python!")

def add_numbers(a, b):
    total = a + b
    print("\nThe sum of", a, "and", b, "is:", total)

add_numbers(10, 20)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero not allowed!"

print("\n--- Simple Calculator ---")
num1 = 15
num2 = 3

print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))

square = lambda x: x ** 2
print("\nSquare of 5 using lambda:", square(5))


multiply = lambda a, b: a * b
print("Multiplication of 4 and 6 using lambda:", multiply(4, 6))