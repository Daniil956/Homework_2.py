from random import randint
n = int(input("Enter number: "))
a = 0
b = 0
i = 0
x = [randint(0, 1) for i in range(n)]
print(x)

for i in x:
    if i == 1:
        a += 1
    else:
        b += 1
    i += 1
print(a)
print(b)

if a > b:
    print("need flip: ", 0)
else:
    print("need flip: ", 1)
