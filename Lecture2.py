#############
##LECTURE 2##
#############

#################################################
#Loopy loop loop loops
#While loop

#Fibonacci Series
a,b=0,1
while b < 50:
    print(b, end=',')
    a,b=b, a+b
print()
#infinite loop never ends, so end loop

#if statement 
a=10
if a%2 == 0:  #percent % is modulus, remainder
    print("Even number")
else:
    print("Odd number")

if a <= 10:
    print("less than or equal to 10")
else:
    print("greater than 10")

#Booleans: True or False, 0 or 1 
print(8==8)
print(1==2)
print(True==1)
print(False==0) #true and false more obvious

var=None
if var is None:
    print("The variable is None!")

#Combining all conditions - airplane edition

age=2
if age < 2:
    print("Free Fare!")
elif (age >= 2) and (age < 12):
    print("50% off!")
else:
    print("Full Fare!")

#Logical operators
#not, and, or, ^ (xor, one or the other but not both)

#################################################
#Testing strings

test_str="It is not safe to go alone. Take this!"
if "safe" in test_str:
    print("We do!")

test_list=[1,2,3.14,4]
if 3.14 in test_list:
    print(test_list)

#List as condition
test_list=['abc', 1, 87.254]  #can also use len, if len is 0 it's empty, else it's not
if test_list:
    print("The list is not empty")
else:
    print("The list is empty")

#################################################
#Find the smallest number divisibe by 2,3,7

x=7
while x<100:
    if (x%2==0) and (x%3==0) and (x%7==0):
        print(x)
        break #found smallest, yer done
    x += 1 #increminting

#################################################
#Find leap years for a set of years
#A leep year is evenly divisible by 4
#but if divisible by 100, it is NOT a leap year
#if is also divisble by 400, then IS a leep year

x=1990
while x < 2030:
    x+=1 
    if ((x%4 ==0) and (x%100 != 0)) or (x%400 == 0):
        print(x, 'Leap Year')
        continue
    print(x)

#################################################
#FOR LOOPS!!!!!

#First 50 numbers in the Fib series
a,b=0,1
for _ in range(50): #can use _ instead of i
    print(b,end=',')
    a,b=b,a+b
print()

cities=['New York', 'Paris', 'Peckham']
for city in cities:
    print(city)

for i,city in enumerate(cities):
    print(i, city)

countries=['USA', 'France', 'UK']

for country, city in zip(countries, cities):
    print(country, city)

#################################################
#Reading Files

file_name='data.txt'
with open(file_name, 'r') as f:
    #the file is opened
    print(f.closed)
    print(f.readline())
print(f.closed) #the file is closed 

#reading line by line
with open(file_name) as f:
    for line in f:
        print(line)

#Splitting a string by a demlimiter
a='one,two,three,four'
print(a.split(','))

#stripping white space
b='     center            '
print(b.strip())

#print content of a file to a list

with open(file_name) as f:
    for line in f:

        #remove new line character

        line = line.replace('\n', '')
        
        #convert to list

        line=line.split(',')

        print(line)
        
#################################################
#QUIZ 2
#Q1 two loops, reading list, order in which something is printed
#Q2 if else with conditions
#Q3 use a list and an if
#Q4 files
#Q5 for loops
#Q5 review leap year question

number=[10,20]
item=['a','b']
for x in number:
    for y in item:
        print(x,y)

x=5
if x <5:
    x+=2
else:
    x+=4
if x >=8:
    x = x+1
print(x)

list=[1,10,20]
if 11 in list:
    print(True)
else:
    print(False)

#file_name='numbers.txt'
with open("numbers.txt") as f:
    line = f.readline()
    line=line.split()
    print(line)

n=0
for x in range(1,100):
    n+=x
print(n)

############QUESTION 6###################
#last two digits of my student number are 99

N=0 
while N < 99:
    N+=1
    if (N%3 == 0) and (N%5 == 0):
        print("FizzBuzz")
    elif (N%3 == 0):
        print("Fizz")
    elif (N%5 == 0):
        print( "Buzz")
    else:
        print(N)
