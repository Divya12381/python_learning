#arithmetic operatores
print(10 + 5 * 2)        #20
print(2 ** 3 ** 2)       #512  
print(10 // 3)           #3
print(10 % 3)            #1
print(5 / 2)               #2.5
print([1,2,3] + [4,5,6])    #[1, 2, 3, 4, 5, 6]
print((1,2,3)+ (4,5,6))    # (1, 2, 3, 4, 5,6)

print([1,2,3] * 4)       #[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
print(*[1,2,43])         # 1 2 43
print([1,2,3] + (1,2,3))  #type error
print([1,2,3] + 'dog')     #trype error

#relational and logical operators
print(10 > 5 and 20 < 30 )  #True
print(10 > 20 and 5 < 10)    #False
print(not 1 == 1)            #False
print(1 < 2 < 3)            #true
print(1 > 2 > 3)            #false
print('abc' > 'def')       #false
print([1,2,3] < [1,3,4])    #true

# assignment and walrus operator
print(a=10)
a = 10
print(a)

# identity vs equality
a = [1,2,3]
b = [1,2,3]
print(a == b)
print(a is b)
a = 'abc'
b = 'abc'
print(a==b)
print(a is b)
a = (1,2,3)
b = (1,2,3)
print(a==b)
print( a is b)

# membership operator
a = [1,2,3,4,5]
print(6 in a)
print(6 not in a)
print('abc' in 'abcde')

