#2
# some_text = input("Enter some text: ")
# file = open("data.txt", "w")
# file.write(some_text)
# file.close()
#3
# numbers_3 = []
# for i in range(1):
#     number = int(input("Enter number: "))
#     numbers_3.append(number)
# numbers = int(input("Enter  numbers : "))
# for i in range(numbers):
#     numbers_2 = int(input("Enter number: "))
#     numbers_3.append(numbers_2)
# numbers_4 = str((numbers_3).replace(",", " "))
# file = open("numbers.txt", "w")
# file.write(numbers_4)
# file.close()

#4
# import random
# from random import randint
# numbers = []
# for number in range(100):
#     line = str(random.randint(0, 100))
#     numbers.append(line)
# numbers_2 = str(numbers).replace(",", "\n")
# file = open("random_numbers.txt", "w")
# file.write(numbers_2)

#5
# numbers_words = 0
# f = open("some_text.txt", "r")
# text = f.read()
# words = text.split()
# for word in words:
#     if not word.isnumeric():
#         numbers_words += 1
# print(numbers_words)

#6
# import re
# file = open("data_2.txt")
# summ = 0
# numbers = file.read()
# numbers = re.findall(r"[+-]?\d+", numbers)
# numbers = [int(x) for x in numbers]
# for x in numbers:
#     summ += x
# print(summ)

#7
dict = {}
with open("data_2.txt") as file:
    for line in file:
        key, *value = line.split()
        dict[key] = value
print(dict)
