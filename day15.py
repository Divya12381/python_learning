#Right angel traigle
n = 4

for i in range(1, n + 1):
    print(i * '*')

#inverted right angel traingle
for i in range(n, 0, -1):
    print(i * '*')

#pyramid
for i in range(1, n + 1):
    print((n - i) * ' ' + i * '* ')

#inverted pyramid
for i in range(n, 0, -1):
    print((n - i) * ' ' + i * '* ')

#Hello square
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print('*', end='')
        else:
            print(' ', end='')
    print()

#star pattern
for i in range(n):
    for j in range(n):
        if i == n // 2 or j == n // 2 or i == j or j == n - i - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

   #Number right traingle
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

  #Inverted number traingle
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()