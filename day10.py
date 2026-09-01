#important problems
#1. print numbers from 1 to 10 
for i in range(1, 11):
    print(i)

#2. print even numbers from 5 to 30 and above list
for i in range(5, 31):
    if i % 2 == 0:
        print(i)

#3. print odd numbers from 5 to 30 and above list
for i in range(5, 31):
    if i % 2 != 0:
        print(i)

#4. print numbers divisible by 5 from 1 to 30 and above list
for i in range(1, 31):
    if i % 5 == 0:
        print(i)

#5. print numbers divisible by both 5 and 7 from 1 to 100 and above list
for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(i)

#6. sum of numbers from 10 to 25 and above list
sum = 0
for i in range(10, 26):
    sum = sum + i
print(sum)

#7. multiplication table of a number 
n = int(input('Enter a number: '))
for i in range(1, 11):
    print(n, '*', i, '=', n * i)

#8. factorial 
n = int(input('Enter a number: '))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(fact)

#9. fibonacci 
n = int(input('Enter number of terms: '))
a = 0
b = 1
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c

#10. reverse a string
s = input('Enter a string: ')
reverse = ''
for i in range(len(s) - 1, -1, -1):
    reverse = reverse + s[i]
print(reverse)

#11. count vowels in a string
s = input('Enter a string: ')
count = 0
for x in s:
    if x in 'aeiouAEIOU':
        count = count + 1
print('Vowels:', count)

#12. count z's and y's in a string
s = input('Enter a string: ')

z_count = 0
y_count = 0

for x in s:
    if x == 'z' or x == 'Z':
        z_count = z_count + 1

    if x == 'y' or x == 'Y':
        y_count = y_count + 1

print('Z count:', z_count)
print('Y count:', y_count)

#13. check whether a number is prime number or not 
n = int(input('Enter a number: '))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print('Prime number')
else:
    print('Not a prime number')