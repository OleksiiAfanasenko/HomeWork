#1
file = open("data_2.txt")
numbers = file.read()
numbers_1 = numbers.split()
file.close()
numbers_2 = list()
for i in numbers_1:
      if i.isnumeric():
         numbers_2.append(int(i))
print(numbers_2)


#2
some_text = input("Enter some text: ")
file = open("data.txt", "w")
file.write(some_text)
file.close()
#3
n = int(input("введите n: "))
numbers = list()
for _ in range(n):
    numbers.append(input())
with open("numbers.txt", "w") as opened_file:
    opened_file.write(", ".join(numbers))

#4
import random
from random import randint
numbers = []
for number in range(100):
    line = random.randint(0, 100)
    numbers.append(str(line))
numbers_2 ="\n".join(numbers)
file = open("random_numbers.txt", "w")
file.write(numbers_2)
file.close()

#5
numbers_words = 0
f = open("some_text.txt", "r")
text = f.read()
words = text.split()
for word in words:
    if not word.isnumeric():
        numbers_words += 1
print(numbers_words)

#6
import re
file = open("data_2.txt")
summ = 0
numbers = file.read()
numbers = re.findall(r"[+-]?\d+", numbers)
numbers = [int(x) for x in numbers]
for x in numbers:
    summ += x
print(summ)

#7
dict = {}
with open("data_2.txt") as file:
    for line in file:
        if line.strip() in dict.keys():
            dict[line.strip()] += 1
        else:
            dict[line.strip()] = 1

print(dict)