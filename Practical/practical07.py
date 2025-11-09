student = {
    "name": "Zaid",
    "age": 21,
    "course": "Computer Science",
    "grade": "A"
}

print("Original Dictionary:")
print(student)

student["grade"] = "A+"
print("\nAfter updating 'grade':")
print(student)

print("\nKeys in dictionary:")
print(student.keys())

print("Values in dictionary:")
print(student.values())

keys = ["name", "age", "city"]
values = ["Ali", 25, "Pune"]

merged_dict = {}
for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]

print("\nDictionary created by merging two lists:")
print(merged_dict)

text = "programming"
char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("\nCharacter count in string 'programming':")
print(char_count)