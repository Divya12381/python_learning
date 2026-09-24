# 1. Palindrome Number
def is_palindrome_number(num):
    original = num
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return original == rev

# 2. Palindrome String
def is_palindrome_string(s):
    s = s.lower().replace(" ", "") # ignore case and space
    return s == s[::-1]

# 3. Prime Number
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 4. Reverse a String
def reverse_string(s):
    return s[::-1]  # or use loop for logic
    # rev = ""
    # for ch in s:
    #     rev = ch + rev
    # return rev

# 5. Factorial
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

# 6. Fibonacci - returns series up to n terms
def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# 7. Count Number of Digits
def count_digits(num):
    return len(str(abs(num))) # easy way
    # logic way:
    # count = 0
    # num = abs(num)
    # if num == 0: return 1
    # while num > 0:
    #     count += 1
    #     num //= 10
    # return count

# 8. Armstrong Number
# e.g. 153 = 1^3 + 5^3 + 3^3 = 153
def is_armstrong(num):
    original = num
    power = len(str(num))
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10
    return total == original

# --- Testing ---
print(is_palindrome_number(121))  # True
print(is_palindrome_string("Madam")) # True
print(is_prime(17)) # True
print(reverse_string("python")) # nohtyp
print(factorial(5)) # 120
print(fibonacci(7)) # [0, 1, 1, 2, 3, 5, 8]
print(count_digits(12345)) # 5
print(is_armstrong(153)) # True
