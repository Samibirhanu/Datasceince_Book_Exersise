# If condition
if 1 > 2:
    message = "if only 1 were greater than two"
elif 1 > 3:
    message = "elif stands for 'else if' "
else:
    message = "when all else fails use else (if you want to)"
print(message)

# using ternary if-then-else 
x = 10
parity = "even" if x % 2 == 0 else "odd"   # statment , if condition , else with statment
print(parity)

# while loop
x = 0
while x < 10:
    print(f"{x} is less than 10")
    x += 1                          # increment by 1

# for loop
for x in range(10):             # range(10) is the numbers 0-9
    print(f"{x} is less than 10")

# continue and break 
for x in range(10):
    if x == 3:
        continue    # go immidiatly to the next iteration which is no 4
    if x == 5:
        break       # quit the loop entirely
    print(x)

