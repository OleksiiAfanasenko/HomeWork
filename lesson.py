# def string_times(str, n):
#     for i in range(n):
#         print(str, end='')
# string_times("Hi", 5)
# x = "Code"
# print(len(x))
# def array_front9(nums):
#   for index, value in enumerate(nums):
#     if index > 3:
#       return False
#     if value == 9:
#        return(True)

#   return(False)


# print((array_front9([1, 2, 9, 3, 4])))
# #print(False)
# print(array_front9([1, 2, 3, 4, 9]))
# print(array_front9([1, 2, 3, 4, 5]))

# def front_times(str, n):
#     value = ''
#     for _ in range(n):
#         value += str[0:3]
#     return value
#
#
# print(front_times('Chocolate', 2))
# # 'ChoCho'
# print(front_times('Chocolate', 3))
# # 'ChoChoCho'
# print(front_times('Abc', 3))
# # 'AbcAbcAbc'


# def first_word(text):
#     result = ''
#     for char in text:
#         if char == " ":
#             return result
#         else:
#             result += char
#
#
# print(first_word("Hello world") == "Hello")
#
# def checkio(number):
#   if number % 3 == 0 and number % 5 == 0:
#     return "Fizz Buzz"
#   elif number % 5 == 0:
#     return "Buzz"
#   elif number % 3 == 0:
#     return "Fizz"
#   else:
#     return str(number)
#
#
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
#
# print(is_even(2) == True)
# print(is_even(5))
# print(is_even(5) == False)
# print(is_even(0) == True)
#
#
# def backward_string(val):
#     example = ""
#     for char in reversed(val):
#         example += char
#     return example
#
#
# def stars(fun):
#     def wrapper():
#         print("*****")
#         fun()
#         print("*****")
#
#     return wrapper
#
#
# @stars
# def funk1():
#     print("Hello word")
#
#
# @stars
# def funk2():
#     print("Hello")
#
#
# @stars
# def funk3():
#     print("word")
#
#
# funk1()
# funk2()
# funk3()
#
#
# def stars(char):
#     def decor(fun):
#         def inner():
#             print(char * 6)
#             print(fun)
#             fun()
#             print(char * 6)
#
#         return inner
#
#     return decor
#
#
# @stars("*")
# def funk1():
#     print("Hello word")
#
#
# @stars("#")
# def funk2():
#     print("Hello")
#
#
# @stars("%")
# def funk3():
#     print("word")
#
#
# funk1()
# funk2()
# funk3()
#
# import os
# def call_times(file_name):
#     def decor(fun):
#         def inner():
#           if os.path.exists(file_name) == True:
#             print("file exist")
#             print(f'{fun.__name__} была вызвана {1} раза\n')
#           else:
#             print("file not exist")
#             f = open(file_name, "w")
#             f.write("ok")
#             # print("ok", f'{fun} была вызвана {count} раза\n')
#           # print(fun)
#           # print(file_name)
#           fun()
#         return inner
#     return decor
#
# @call_times("foo.txt")
# def foo():
#     pass
#
# @call_times("foo.txt")
# def boo():
#     pass
#
# @call_times("call.txt")
# def doo():
#     pass
#
#
# foo()
# print("foo end")
# boo()
# print("boo end")
# doo()
# print("doo end")

# class Person:
#     def say_hello(self):
#         print(hex(id(self)))
#         print("Hello!")
#
#
# tom = Person()
# print('tom', hex(id(tom)))
# tom.say_hello()
#
# bob = Person()
# print('bob', hex(id(bob)))
# bob.say_hello()

#  # стандартний декоратор
# def decor(char):
#     def sumbol(func):
#         def inner():
#             print(char * 10)
#             func()
#             print(char * 10)
#
#         return inner
#
#     return sumbol
#
#
# @decor("@")
# def hello_word():
#     print("hello word")
#
#
# hello_word()
#
# # **********
import os

def call_times(file_name):
  def outer (func):
    def inner():
      if os.path.exists(file_name) == False:
        print(file_name)
        f = open(file_name, "w")
        f.write(f'{func.__name__} была вызвана 1 раз.\n')
        f.close()
      else:
        f = open(file_name, "r")
        lines = f.readlines()
        print(lines)
        f.close()
        flag = False
        for i, line in enumerate(lines):
          print(lines)
          words = line.split()
          if words[0] == func.__name__:
            flag = True
            print(func.__name__)
            f = open(file_name, "w")
            count = int(words[3])
            print(count)
            lines[i] = f'{func.__name__} была вызвана {count+1} раз.\n'
            f.writelines(lines)
            f.close()
          else:
            pass
        if flag == False:
          f = open(file_name, "a")
          f.write(f'{func.__name__} была вызвана 1 раз.\n')
          f.close()
          print(func.__name__," !!!")
      func()
    return inner
  return outer

def delete (file_name):
   if os.path.exists(file_name) == True:
     os.remove(file_name)



@call_times("foo.txt")
def foo():
  pass

@call_times("foo.txt")
def boo():
  pass

@call_times("call.txt")
def doo():
  pass

foo()
boo()
doo()
foo()
boo()
boo()
boo()
doo()