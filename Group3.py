# Group 3: If statement + Switch statement + For loop + While loop + Indentation

print("\n---------If Statement----------\n")
x = 5

if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")

print("\n---------Switch Statement----------\n")
#Python does not have a built-in switch statement, but we can use match-case (introduced in Python 3.10) to achieve similar functionality.
y = 2
if y == 1:
    print("One")
elif y == 2:
    print("Two")
else:
        print("Other")

print("\n---------For Loop----------\n")
for i in range(5):
    print("Iteration:", i)

for fruit in ["apple", "banana", "cherry"]:
    print("Fruit:", fruit)

print("\n---------While Loop----------\n")
count = 0
while count < 10:
    if count == 3:
        count += 1  # Increment count to avoid infinite loop
        continue # Skip the rest of the loop when count is 3
    if count == 6:
        break # Exit the loop when count is 6
    print("Count:", count)
    count += 1
         
print("\n---------Indentation----------\n")
number = 4;
if number % 2 == 0:
    print("Even number")
    if number > 2:
        print("Number is greater than 2")
else:
    print("Odd number")
