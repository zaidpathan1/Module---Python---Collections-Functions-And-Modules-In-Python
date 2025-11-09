fruits = ["apple", "banana", "cherry", "mango"]
print("Iterating through the list:")
for fruit in fruits:
    print(fruit)

numbers = [45, 12, 89, 33, 67, 5]

print("\nOriginal list of numbers:", numbers)

numbers.sort()
print("After sort():", numbers)

numbers_unsorted = [45, 12, 89, 33, 67, 5]
sorted_numbers = sorted(numbers_unsorted)
print("After sorted():", sorted_numbers)
print("Original list remains unchanged:", numbers_unsorted)

empty_list = []
print("\nCreating a new list using append() inside a for loop:")
for i in range(1, 6):
    empty_list.append(i * 10)  

print("New list after appending elements:", empty_list)