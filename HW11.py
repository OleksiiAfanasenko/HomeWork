import os

def call_times(file_name):
  def outer (func):
    def inner():
      if os.path.exists(file_name) == False:
        f = open(file_name, "w")
        f.write(f'{func.__name__} была вызвана 1 раз.\n')
        f.close()
      else:
        f = open(file_name, "r")
        lines = f.readlines()
        f.close()
        flag = False
        for i, line in enumerate(lines):
          words = line.split()
          if words[0] == func.__name__:
            flag = True
            f = open(file_name, "w")
            count = int(words[3])
            lines[i] = f'{func.__name__} была вызвана {count+1} раз.\n'
            f.writelines(lines)
            f.close()
        if flag == False:
          f = open(file_name, "a")
          f.write(f'{func.__name__} была вызвана 1 раз.\n')
          f.close()
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