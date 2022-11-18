#1
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))
max = ""

if a > 10 and b > 10 and c > 10 and a % 3 == 0 and b % 3 == 0:
    print("yes")
else:
    print("no")


#2
if b < a > c:
    max = a
    print(max)
elif a < b > c:
    max = b
    print(max)
elif b < c > a:
    max = c
    print(max)

 #3
number = int(input("Enter number: "))
number_2 = ((number % 10) * 100) + ((number // 10 % 10) * 10) + (number // 100)
print(number_2)