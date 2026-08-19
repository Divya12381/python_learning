# create a list with 3 elements
l = [10, 20, 30]
print(l)

# INSERT OPERATIONS

# appending
# add 5 types of non-sequence elements to it with append

l = [10, 20, 30]

l.append(100)       # int
l.append(10.5)      # float
l.append(2 + 3j)    # complex
l.append(True)      # bool
l.append(None)      # NoneType

print(l)

# add 5 types of sequences to it with append

l = [10, 20, 30]

l.append("Python")          # string
l.append([1, 2, 3])          # list
l.append((4, 5, 6))          # tuple
l.append({7, 8, 9})          # set
l.append(range(1, 4))        # range

print(l)

# extending
# add 5 types of non-sequence elements to it with extend

l = [10, 20, 30]
l.extend([100])
l.extend([10.5])
l.extend([2 + 3j])
l.extend([True])
l.extend([None])

print(l)

# add 5 types of sequence elements to it with extend

l = [10, 20, 30]

l.extend("Python")       # string
l.extend([1, 2, 3])      # list
l.extend((4, 5, 6))      # tuple
l.extend({7, 8, 9})      # set
l.extend(range(10, 13))  # range

print(l)
# inserting

l = [10, 20, 30]

# insert an element at index 1 and print
l.insert(1, 100)
print(l)

# insert an element at index -1 and print
l.insert(-1, 200)
print(l)

# insert an element at index 10000 and print
l.insert(10000, 300)
print(l)

# insert an element at index -10000 and print
l.insert(-10000, 400)
print(l)

# DELETE OPERATIONS

# create a list with 1,2,1,3,4,1
l = [1, 2, 1, 3, 4, 1]

# pop element at index 3 and print element and list
element = l.pop(3)
print("Popped element:", element)
print("List:", l)

# pop last element and print element and list
element = l.pop()
print("Popped element:", element)
print("List:", l)

# remove first 1 from list and print element and list
l.remove(1)
print("Removed element: 1")
print("List:", l)

# clear all elements in the list
l.clear()
print("List after clear:", l)


# UPDATE OPERATIONS

# create a list with 3,2,1,5,4
l = [3, 2, 1, 5, 4]

# sort the list in ascending and print
l.sort()
print("Ascending:", l)

# create a list with 3,2,1,5,4
l = [3, 2, 1, 5, 4]

# sort the list in descending and print
l.sort(reverse=True)
print("Descending:", l)

# create a list with 3,2,1,5,4
l = [3, 2, 1, 5, 4]

# reverse the list and print
l.reverse()
print("Reverse:", l)

# READ OPERATIONS

# create a list with 1,2,1,3,1,2
l = [1, 2, 1, 3, 1, 2]
# find count of 1 and 2 in list
print("Count of 1:", l.count(1))
print("Count of 2:", l.count(2))

# find index of 1 from start
print("Index of 1 from start:", l.index(1))

# find index of 1 from 2nd index
print("Index of 1 from 2nd index:", l.index(1, 2))

# find index of 1 from 5th index
print("Index of 1 from 5th index:", l.index(1, 5))

# READ OPERATIONS

# create a list with 1,2,1,3,1,2
l = [1, 2, 1, 3, 1, 2]

# find count of 1 and 2 in list
print("Count of 1:", l.count(1))
print("Count of 2:", l.count(2))

# find index of 1 from start
print("Index of 1 from start:", l.index(1))

# find index of 1 from 2nd index
print("Index of 1 from 2nd index:", l.index(1, 2))

# find index of 1 from 5th index
print("Index of 1 from 5th index:", l.index(1, 5))

# TUPLE

# create a tuple with 1,2,1,3,1,2
t = (1, 2, 1, 3, 1, 2)

# find count of 1 and 2 in tuple
print("Count of 1:", t.count(1))
print("Count of 2:", t.count(2))

# find index of 1 from start
print("Index of 1 from start:", t.index(1))

# find index of 1 from 2nd index
print("Index of 1 from 2nd index:", t.index(1, 2))

# find index of 1 from 5th index
print("Index of 1 from 5th index:", t.index(1, 5))

l = [1, 2, 1, 3, 1, 2]

print("Count of 1:", l.count(1))
print("Count of 2:", l.count(2))

print("Index of 1 from start:", l.index(1))
print("Index of 1 from 2nd index:", l.index(1, 2))
print("Index of 1 from 4th index:", l.index(1, 4))