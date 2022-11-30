#1
n = 12
for i in range(12, 0, -1):
    print('*' * i)
#2
n = 10
for i in range(0, 10):
   print('*' * i)
#3
n = 10
for i in range(0, 10):
   print((' ' * i + '*' * (n - i)))
#4
n = 12
for i in range(12, 0, -1):
    print((' ' * i + '*' * (n - i)))
