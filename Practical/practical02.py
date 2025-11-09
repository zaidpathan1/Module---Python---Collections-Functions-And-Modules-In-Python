my_list = [10, 20, 30, 40]
print("Original List:", my_list)

my_list.append(50)
print("\nAfter append(50):", my_list)

my_list.insert(2, 25)  
print("After insert(2, 25):", my_list)

my_list.remove(25)
print("\nAfter remove(25):", my_list)

popped_element = my_list.pop()  
print("After pop():", my_list)
print("Popped element:", popped_element)

popped_element2 = my_list.pop(1)  
print("After pop(1):", my_list)
print("Popped element from index 1:", popped_element2)