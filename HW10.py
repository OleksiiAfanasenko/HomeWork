#1
# def change(lst):
#     if not isinstance(lst, list):
#         return 0
#     else:
#         lst_2 = list()
#         lst_2.append(lst[-1])
#         for i in range(1,len(lst) - 1):
#             lst_2.append(lst[i])
#         lst_2.append(lst[0])
#         return lst_2
# lst = [1, 2, 3, 4, 5]
# print(change(lst))

#2
# def to_dict(lst):
#     dictionary = {}
#     for char in lst:
#         dictionary.update({char: char})
#     print(dictionary)
# to_dict(["a", "b", "c"])
# to_dict(["1", "2", "3"])

#3
# def sum_range(start, end):
#   if start > end:
#     start, end = end, start
#   result = 0
#   for i in range(start, end+1):
#     result += i
#
#   print(result)
# sum_range(5, 2)
# sum_range(9, 21)

#4
# def read_last(lines, file):
#     f = open(file, "r")
#     if lines < 1:
#         print("Lines < 1")
#         return
#     lst = f.readlines()
#     lst_2 = lst[-lines:]
#     for i in lst_2:
#         print(i, end="")
#
#
# lst = ["1\n", "2\n", "3\n", "4\n", "5\n", "6\n", "7\n", "8\n", "9\n"]
# f = open("file.txt", "w")
# f.writelines(lst)
# f.close()
#
# read_last(2, "file.txt")
# read_last(1, "file.txt")

