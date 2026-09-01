#TASK 1
n = 9
if n % 3 == 0:     #9%3=0,true
    print('A')
print('Outside')   

#TASK 2:
n = 10
if n % 10 == 0:    #10 %10=0,true
    print('A')
if n % 5 == 0:     #10%5=0,true
    print('B')
print('Outside')

#TASK 3:
n = 10 
if n % 10 == 0:     #10%10=0,true
    print('A')
elif n % 5 == 0:     
    print('B')
print('Outside')


#TASK 4:
n = 10 
if n % 6 == 0:  #10%6=4,false
    print('A')
elif n % 3 == 0:  #10%3=1,false
    print('B')
else:
    print('C')
print('Outside')

#TASK 5:
marks = 89 
if marks > 40:     #89>40 true
    if marks > 75:  #89>75 true
        print('Dictinction') 
    else:
        print('Pass')
else:
    print('Fail')




