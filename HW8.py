#1
A = {"Sasha", "Maks", "Andrey", "Ivan"}
B = {"Ivan", "Petr", "Vasya", "Sasha"}
print(A.intersection(B))
print(B.difference(A))

#2

permissions = {}
n = int(input())
for _ in range(n):
    s = input().split()
    permissions[s[0]] = set(s[1:])
n = int(input())
for _ in range(n):
    perm, file = input().split()
    if perm == "read":
        perm = "R"
    if perm == "write":
        perm = "W"
    if perm == "execute":
        perm = "X"
    if perm in permissions[file]:
        print("Ok")
    else:
        print("Acces denied")