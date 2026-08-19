# strip(), lstrip(), rstrip()
a = '   python is simple   '
print(a.strip())    # python is simple
print(a.lstrip())   # python is simple   
print(a.rstrip())   #    python is simple

# replace
a = 'python is simple, python is easy, python is allrounder'
b = a.replace('python', 'java')
print(a)  # python is simple, python is easy, python is allrounder
print(b)  # java is simple, java is easy, java is allrounder

# upper,lower,swapcase,title,capitalize
a = 'PYTHON is siMPle'
print(a.lower())      # python is simple
print(a.upper())      # PYTHON IS SIMPLE
print(a.swapcase())   # python IS SimPle
print(a.title())      # Python Is Simple
print(a.capitalize()) # Python is simple

#count,startswith,endswith
a = 'abacad'
b = a.startswith('a')   # True  -> starts with 'a'
c = a.startswith('ad')  # False -> doesn't start with 'ad'
d = a.endswith('d')     # True  -> ends with 'd'
e = a.endswith('de')    # False -> doesn't end with 'de'
f = a.count('a')        # 3     -> 'a' appears 3 times
g = a.count('ad')       # 1     -> 'ad' appears 1 time

print(b)  # True
print(c)  # False
print(d)  # True
print(e)  # False
print(f)  # 3
print(g)  # 1

#find,rfind,index,rindex
print(s.find('a'))        # 0   -> first 'a' from left
print(s.find('a', 3))     # 4   -> first 'a' starting from index 3
print(s.find('a', 4, 8))  # 4   -> first 'a' between index 4 to 7
print(s.rfind('a'))       # 6   -> last 'a' from right
print(s.rfind('a', 3))    # 6   -> last 'a' from index 3 to end
print(s.rfind('a', 4, 8)) # 6   -> last 'a' between index 4 to 7
print(s.index('a'))       # 0   -> same as find, but errors if not found
print(s.index('a', 3))    # 4   -> first 'a' from index 3
print(s.index('a', 4, 8)) # 4   -> first 'a' between 4 to 7
print(s.index('a'))       # 0   -> repeated
print(s.index('a', 3))    # 4   -> repeated
print(s.index('a', 4, 8)) # 4   -> repeated
print(s.index('z'))       # ValueError: substring not found -> crashes
print(s.find('z'))        # -1  -> returns -1 if not found

#ismethods
a = ' '
b = 'a'
print(a.isspace())  # True  -> only space
print(b.isspace())  # False -> has 'a'

a = 'aBcD'
print(a.isalpha())  # True  -> only letters A-Z a-z
b = 'aBcD1'
print(b.isalpha())  # False -> has number 1
c = 'aBc@D'
print(c.isalpha())  # False -> has symbol @
# Note: you wrote isapha() typo. It should be isalpha()

a = '13'
print(a.isdigit())  # True  -> only digits
b = '12a'
print(b.isdigit())  # False -> has 'a'

a = 'AbC123'
print(a.isalnum())  # True  -> letters + digits allowed
b = 'Ab#C2'
print(b.isalnum())  # False -> has symbol #

a = '23$U'
print(a.isupper())  # True  -> all letters are uppercase. $ and 23 are ignored
b = '23%Ua'
print(b.isupper())  # False -> has lowercase 'a'

a = '23$u'
print(a.islower())  # True  -> all letters are lowercase. $ and 23 are ignored
b = '23%uA'
print(b.islower())  # False -> has uppercase 'A'

#split
a = 'badac'
print(a.split('a'))    # ['b', 'd', 'c']  
# split wherever 'a' comes. 'b' + '' + 'd' + '' + 'c'

b = '   '  # 3 spaces
print(b.split(' '))    # ['', '', '']  
# 3 spaces makes 4 empty strings

c = 'abaca'
print(c.split('a'))    # ['', 'b', 'c', '']  
# starts and ends with 'a' so we get empty strings

d = 'iam a good person'
print(d.split())       # ['iam', 'a', 'good', 'person']  
# split() with no argument splits by any whitespace

#join
a = '@'
l = [1,2,3]
t = (1,2,3)
s = {1,2,3}
d = {3:1, 2:3, 3:1}  # keys are 3,2

print(a.join(l))  # TypeError: sequence item 0: expected str instance, int found
print(a.join(t))  # TypeError: same error
print(a.join(s))  # TypeError: same error
print(a.join(d))  # TypeError: same error