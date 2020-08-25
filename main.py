# 1

# a)
i = 1

for i in range(1, 16):
    print(i)

# b)
i = 1

for i in range(20, 31):
    print(i)

# c)
i = 1

for i in range(0, 2001):
    print(i, end='')

for i in range(11, -10, -1):
    print(i)

# 2
i = 1

for i in reversed(range(1, 101)):
    print(i)

# 3
i = 1

for i in range(19, 0, -2):
    print(i)

# 4
i = 1

for i in range(10):
    if i % 2 != 0:
        print(i)

# 5
i = 1

sum = sum([i for i in range(1, 51)])
print(sum)

# 6
from tabulate import tabulate
from math import pow

i = 1

result = []

for i in range(0, 21):
    result.append([i, pow(i, 2), pow(i, 3)])

print(tabulate(result, headers=['i', 'i^2', 'i^3']))


# 7
# using tabulate

def c_to_f(c):
    return str((9 / 5) * c + 32) + ' F'


results = []

for i in range(40, -41, -1):
    results.append([str(i) + '°C'])

print(tabulate(result))

# 8
i = 41
while i < -41:
    results.append([str(i) + '°C'])

print(tabulate(result))

# 9
string = str(input("input a word: "))

print(' '.join(string))

# 10

password = "hejsan"

action = input("password: ")

result = ''

if action == password:
    print("Password OK")
    exit()
if action:
    print("wrong password")

# 11 - 12
i = 1

x = 0
while x < 5:
    x = x + 1

    for i in range(1, 9):
        print(i, end='')
    print()


# 13
x = ""

for i in range(10):
    x += "*"
    print(x)

print("<Nu var det slut på det roliga >")








