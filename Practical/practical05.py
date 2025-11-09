numbers = (10, 20, 30, 40, 50, 60, 70)

print("Original tuple:")
print(numbers)

subset = numbers[1:6] 
print("\nValues between index 1 and 5:")
print(subset)

alternate_values = numbers[1:6:2]  
print("\nAlternate values between index 1 and 5:")
print(alternate_values)

last_value = numbers[-1]
print("\nValue at the last index:")
print(last_value)