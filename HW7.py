# 1
numbers = []
for i in range(5):
    number = input(f'Enter number: #{i}')
    numbers.append(number)

print(numbers)

# 2
A = [1, 2, 3, 4, 5]
A.pop()
print(A)

# 3
A = []
for i in range(10):
     number = input(f'Enter number: #{i}')
     A.append(number)
n = input(f'Enter number: ')
A.append(n)
print(A.count(n))

# 4
n = input(f'Enter number: ')
A = []
for i in range(4):
     number = input(f'Enter number: {i}')
     A.append(number)
A.append(n)
A.reverse()
print(A)

# 5
A = []
C = []
for number in range(5):
    number = int(input(f'Enter : '))
    A.append(number)
    if number > 5:
        C.append(number)
print(C)

# 6
A = []
for i in range(4):
    number = int(input(f'Enter : '))
    A.append(number)
b = A[0]
c = b
for number in A:
    if b > number:
        b = number
    if c < number:
        c = number
print(b)
print(c)

#7
text = input(f"Enter text: ")
i = 0
for w in text:
    if w.isdigit():
        i += 1
print(i)
