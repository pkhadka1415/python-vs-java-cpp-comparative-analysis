# Group 5: Functions + Interpretation + Exception Handling(my choice)
print("\n---------Functions----------\n")
# Function defination
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))

# Function with default parameter
def power(number, exponent=2):
    return number ** exponent

print("Power of 3 (default exponent):", power(3))
print("Power of 3 to the 3rd:", power(3, 3))

#Multiple retun values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5, 9])
print("Min:", low, "Max:", high)

#Variable  arguments
def sum_all(*args):
    return sum(args)
print("Sum of 1, 2, 3:", sum_all(1, 2, 3))

#Lamda (anonymous) functions
square = lambda x: x ** 2
print("Square of 5:", square(5))


print("\n---------Interpretation----------\n")

x = 10
y = 5
print("x + y:", x + y)

# This would stop the program if not handled 
# print(Z)  # NameError: name 'Z' is not defined

# eval() shows Python interpreting code at runtime
expression = "10 + 5 * 2"
print("Eval Result:", eval(expression))


print("\n---------Exception Handling----------\n")

#Handling division by zero
try:
    result = 10 / 0
    print("Result:", result)
except ZeroDivisionError as e:
    print("Caught an exception:", e)

#Handling invalid conversion
try:
    number = int("abc")
    print("Number:", number)
except ValueError as e:
    print("Caught an exception:", e)

# Finally block - executes regardless of exception
try:
    print("Trying ...")
    result = 10 / 0
except ZeroDivisionError as e:
    print("Caught an exception:", e)
finally:
    print("This will always execute, even if an exception occurred.")   

# Raising your own exceptions
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
try:
    check_age(-1)
except ValueError as e:
    print("Caught an exception:", e)



