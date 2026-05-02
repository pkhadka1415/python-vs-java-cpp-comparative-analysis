
print("\n---------String----------\n") 
my_string = "Hello, World!"
print(my_string)
print("Length of the string:", len(my_string))

#string concatenation
greeting = "Hello, "+ "World!"
print("Concatenated string:", greeting)

#string  repetition
repeated_string = "Hello! " * 3
print("Repeated string:", repeated_string)

#string methods
print("Uppercase:", my_string.upper())
print("Lowercase:", my_string.lower())
print("Replace, 'World' with 'Python':", my_string.replace("World", "Python"))
print("Split the string:", my_string.split(","))

print("\n---------Slicing----------\n")
#Slicing syntax: string[start:end:step]
print("Original string:", my_string)
print("First 5 characters:", my_string[0:5])
print("Last 6 characters:", my_string[-6:])
print("Every second character:", my_string[::2])
print("Reverse the string:", my_string[::-1])
print("Middle part of the string:", my_string[2:8])

#slicing works on lists and tuples too
my_list = [1, 2, 3, 4, 5, 6]
print("List slice[1:4]:", my_list[1:4])
print("Reverse list:", my_list[::-1])

my_tuple = ('1', '2', '3', '4', '5')
print("Tuple slice[1:4]:", my_tuple[1:4])

print("\n---------Index Range Checking----------\n")
#Python raises IndexError for out of range access
try:
    print(my_string[100])  # This will raise an IndexError
except IndexError as e:
    print("IndexError:", e) 

#Negative indeing -- valid in Python
print("Last character:", my_string[-1])
print("Second to last character:", my_string[-2])

#Safe access using slicing - no error even out of range
print("Safe slicing (out of range):", my_string[0:100])

