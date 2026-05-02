print("\n",'------ LISTS ------ ')
my_list = [1, "two", 3]
my_list.append(4)
print(my_list)
print("my_list[3]:", my_list[3])

# Mixed tyees not possible in C++ or jave array
mixed_list = [1, 'two', 3.0, [4, 5]]
print("Mixed list:",mixed_list)

print("\n",'------ TUPLES ------ ')
my_tuple = (1, 2, 3)
print(my_tuple)
print("my_tuple[2]:", my_tuple[2])

# Tuples are immutable, so we cannot modify them
# my_tuple[2] = 10  # This will raise an error

#unpacking tuples
a, b, c = my_tuple
print("Unpacked values:", a, b, c,)

print("\n",'------ DICTIONARIES ------ ')
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(my_dict)
print("my_dict['name']:", my_dict['name'])

# Addd and delete items in dictionary
my_dict['email'] = "alice@example.com"   
del my_dict['age']

print(my_dict, "\n\n Updated dictionary after adding email and deleting age")

#loops through dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

print("\n",'------ ARRAYS ------ ')
import array
my_array = array.array('i', [1, 2, 3,])
my_array.append(4)
# my_array.append("hello")  # This will raise an error because arrays are type-specific
print(my_array)
print("my_array[2]:", my_array[2])

# Arraya are type-specific, so we cannot mix types
# mixed_array = array.array('i', [1, 'two', 3.0])  # This will raise an error    