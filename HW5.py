# # #1
n = int(input("Enter number: "))
for i in range(n, 0, -1):
    print('*' * i)
# #2
n = int(input("Enter number: "))
for i in range(1, n+1):
   print('*' * i)
# #3
n = int(input("Enter number: "))
for i in range(0, n):
   print((' ' * i + '*' * (n - i)))
#4
n = int(input("Enter number: "))
for i in range(n, 0, -1):
    print((' ' * (i - 1) + '*' * (n + 1 - i)))
