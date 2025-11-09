my_list = [10, 20, 30, 40, 50]
my_tuple = tuple(my_list)
print("List converted into tuple:")
print(my_tuple)

mixed_tuple = (25, "Python", 3.14, True, "AI", 99)
print("\nTuple with multiple data types:")
print(mixed_tuple)

tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
combined_tuple = tuple1 + tuple2
print("\nConcatenated tuple:")
print(combined_tuple)

print("\nAccessing value at first index of mixed_tuple:")
print("Value at index 0:", mixed_tuple[0])