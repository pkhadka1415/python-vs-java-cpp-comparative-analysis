# Group 4: Numeric types + Boolean expressions + Short circuit evaluation + Type binding + Type checking
print("\n---------Numeric Types----------\n")
# Python has 3 main numeric types: int, float, and complex
# int, float and complex
x = 10  # int
y = 3.14  # float
z = 2 + 3j  # complex
print("Integer:", x, "Type:", type(x))
print("Float:", y, "Type:", type(y))
print("Complex:", z, "Type:", type(z))

big_number = 123456789012345678901234567890
print("Big number:", big_number, "Type:", type(big_number))

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponentiation:", x ** 2)


print("\n---------Boolean Expressions----------\n")
a = True
b = False

print("a AND b:", a and b)
print("a OR b:", a or b)
print("NOT a:", not a)

print("10 > 5:", 10 > 5)
print("10 == 10:", 10 == 10)
print("10 != 5:", 10 != 5)

print("True + True:", True + True)  # Evaluates to 2
print("True * 5:", True * 5)  # Evaluates to 5  

print("\n---------Short Circuit Evaluation----------\n")
# And: stopes at first False,( second operand is not evaluated )
#  Or: stops at first True, (second operand is not evaluated )

def check_false():
    print("Checking false...")
    return False

def check_true():
    print("Checking true...")
    return True 

print("AND Short circuit:")
result = check_false() and check_true()  # check_true() is not called
print("Result of AND:", result)

print("\nOR Short circuit:")
result = check_true() or check_false()  # check_false() is not called
print("Result of OR:", result)  

print("\n---------Type Binding----------\n")
# Python is dynamically typed, meaning variable types are determined at runtime and can change
var = 10
print("Initial value:", var, "Type:", type(var))

var = "Hello"
print("New value:", var, "Type:", type(var))

var = 3.14
print("Another value:", var, "Type:", type(var))

# this flexibility allows for easy coding but can lead to runtime errors if not careful

print("\n---------Type Checking----------\n")
# Python is Dynamically typed but we can check types using isinstance() or type()

print("type(10):", type(10))
print("type('Hello'):", type('Hello'))
print("type(3.14):", type(3.14))

print("isinstance(10, int):", isinstance(10, int))
print("isinstance('Hello', str):", isinstance('Hello', str))    

# Python allows int + float (related types)
print("Int(10) + float(3.14):", 10 + 3.14)  # Results in a float (13.14)

# Python does not allow int + str (unrelated types)
try:
    print("Int(10) + str('Hello'):", 10 + 'Hello')  # This will raise a TypeError
except TypeError as e:
    print("TypeError:", e)
