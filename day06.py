#SET METHODS
#create a empty dict and print its type
d = {}
print(type(d))
#create a empty set and print its type
s = set()
print(type(s))
#add 5 non-sequences and 5 sequences to that set with add method
s.add(5)
s.add(3.4)
s.add(True)
s.add((3+5j))
s.sdd(None)
s.add('abc')
s.add(range(1,4))
s.add([1,2,3])
s.add((1,2,3))
s.add({1,2,3})
s.add({1:2,2:4})
#add 5 non-sequences and 5 sequences with update method
s = set()

# 5 non-sequences
s.update({10, 20.5, True, None, 3 + 4j})

# 5 sequences
s.update([
    (1, 2),       # tuple
    [3, 4],       # list
    "abc",        # string
    range(5, 7),  # range
    b"xy"         # bytes
])

print(s)

#print a set and remove first element from that set
s = {10, 20, 30, 40, 50}

print(s)

s.pop()

print(s)
s = {10, 20, 30, 40, 50}

# Remove an existing element
s.remove(30)
print(s)

# Remove a non-existing element
s.remove(100)
print(s)

#DICT METHODS
#create a empty dict
d = {}
print(d)
print(type(d))
 #Extend dictionary with another dictionary
 d = {1: 'a'}

d.update({2: 'b', 3: 'c'})

print(d)
#extend dict with another list
d = {1: 'a'}

d.update([(2, 'b'), (3, 'c')])

print(d)
#extend dict with another tuple
d = {1: 'a'}

d.update(((2, 'b'), (3, 'c')))

print(d)
#extend dict with another set
d = {1: 'a'}

d.update({(2, 'b'), (3, 'c')})

print(d)
#create a dict with {1:'a', 2:'b', 3:'c', 4:'d'}

d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
print(d)
    