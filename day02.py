# 1. int
a = 10
print(type(a))

# 2. float
b = 10.5
print(type(b))

# 3. complex
c = 2 + 3j
print(type(c))

# 4. bool
d = True
print(type(d))

# 5. NoneType
e = None
print(type(e))

# 6. string
f = "Python"
print(type(f))

# 7. range
g = range(5)
print(type(g))

# 8. list
h = [1, 2, 3]
print(type(h))

# 9. tuple
i = (1, 2, 3)
print(type(i))

# 10. set
j = {1, 2, 3}
print(type(j))

# 11. dict
k = {"name": "Divya", "age": 25}
print(type(k))

# 1. int to float
a = 10
b = float(a)
print(b)
print(type(b))


# 2. float to int
a = 10.5
b = int(a)
print(b)
print(type(b))


# 3. int to str
a = 100
b = str(a)
print(b)
print(type(b))


# 4. str to int
a = "500"
b = int(a)
print(b)
print(type(b))


# 5. list to tuple
a = [1, 2, 3]
b = tuple(a)
print(b)
print(type(b))


# 6. tuple to list
a = (1, 2, 3)
b = list(a)
print(b)
print(type(b))


# 7. list to set
a = [1, 2, 2, 3, 3]
b = set(a)
print(b)
print(type(b))


# 8. range to list
a = range(1, 6)
b = list(a)
print(b)
print(type(b))