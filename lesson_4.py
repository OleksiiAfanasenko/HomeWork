"""
bool_val = True
if bool_val == True:
    number = 1
else:
    number = 0
print(number)


number =1 if bool_val == True else 0
print(number)
"""


"""
run_loop = True

while run_loop:
    name = input("Enter your name: ")
    if name == "quit":
        run_loop = False
    print(f"Hello {name}!")
"""
"""
#number = input("Enter  a number: ")
while (number := input("Enter  a number: ")) and not (number.isdigit() and len(number) == 3):
    print("Error number")
    number = input("Enter  a number: ")

print(f"End | number is {number}")
"""
"""
count = int(input("Enter you number: "))

i = 0

while i < count:
    i += 1
    print(f"начало итерации #{i}")
    if i % 2 != 0:
        print(f" {i} is odd")
        continue
    print(i)
"""

"""
range(10)  # 0 ... 10
print(list(range(10)))
print(list(range(5, 10))) # 5...10
"""


for i in range(5, 10):
    if i % 2 == 0:
        print(i)

print(f"End")
