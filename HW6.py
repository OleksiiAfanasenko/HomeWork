#1
word_1 = input("Enter word: ")
word_2 = word_1.lower()
palindrom = word_2[::-1]

if palindrom == word_2:
    print("+")
else:
    print("-")

#2
text = input("Enter text: ")
word = input("Enter word: ")
if word in text:
    print("YES")
else:
    print("NO")

#3
text = input("Enter text: ")
if text.startswith("abc"):
    print(text.replace("abc", "www", 1))
else:
    print(text + "zzz")

#4
import re
text = input("Enter text: ")
res = re.sub(r"\d", "", text)
print(res)

#5
email = input("Enter you email: ")
if "@" in email and "." in email:
    print("YES")
else:
    print("NO")