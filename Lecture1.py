#############
##LECTURE 1##
#############

#This is a comment, good to let you/people what your doing
print("Hello, World") #Print words

#Quick Maths

a=15.9
b=6

print('a = ', a)
print('b = ', b)

print('Addition:', a+b)
print('Subtraction:', a-b)
print('Multiplication:', a*b)
print('Division:',a/b)
print('Integer Division:', a//b) #Modulus, integer values
print('Modulo:',a%b) #Remainder
print('Powers, squared:', a**2)
print('Powers, cubed:', a**3)
print('Powers, any power:', a**9)
print('sqrt(2):', 2**0.5)
print('Powers, square root:', a**(1/2)) #or fractions

c=round(1.1/3, 4) #how to round
print('Rounding:', c)

#################################################

print('Before:', a, b)

#Now swap variables

a,b=b,a

print('After:', a,b)
#Fancy
#################################################
#Stringssss

name = 'Monty Python' #apostropy = DOES NOT MATTER
title = "Holy Grail" #quote

print(name)
print(title)

full_title=name+ " and the " + title
print(full_title)

#Slicing
print(name[0])

#Last Character
print(name[-1])

#Second Last Character
print(name[-2])

#Arange
print(name[0:5])
print(name[6:]) #Open to go to the end
print(title[:4])#Open from beginign to certain spot

#Every Other character
print(name[::2])
print(name[1::2]) #everyother character starting shifted 1
print(name[1:8:2]) 
#This helps if you have a lot of data thats slowing down, so you can get the gist 

#modifying strings
print(title[:-1]+'n')

#string Length
print("Length:", len(name))

print('First Line\nSecond line') #breaks into two seperate lines

print("Hello! "*10) #print multiple times

#counting occurances
print(name.count('n')) #careful, case sensitive

#replacing a substring
print(name.replace('o', 'a'))

#################################################
#Type Conversions

x="3.14" #understanding as text
y=float(x) #now is a float, can work with but get the numerical persion limit 0000000000001
z=int(y)

print(x,y,z)

print(y+1)

#################################################
#What will this code print out

a='rosemead'
b='new york'

print(a[2:5]+b[4:] + 'a') #guess what it prints

#################################################
#Lists - ultimate containers

apollo_moon=[11,12,14,15,16,17]
print(apollo_moon)

apollo_commanders=["Armstrong", "Condrad", "Shephard", "Scott", "Young", "Cernan"]
print("Post Apollo 13 Commanders:", apollo_commanders[2:])

apollo_commanders[0] = "Lovell"
print(apollo_commanders)

#Appending an entry
apollo_moon.append(18)
apollo_moon.append(19)
print("Added canceled missions:",apollo_moon)

#removing struff from lists
#Popping last entry
last_cancelled=apollo_moon.pop()
print(last_cancelled)
print(apollo_moon)

#Pretend Apollo 13 was successful 
apollo_moon.insert(2,13)
print(apollo_moon)

#but... that didn't happen
#removing by value, not index
apollo_moon.remove(13)
print(apollo_moon)

#removing by index
apollo_moon.pop(-1)
print(apollo_moon) #back to where we started

#asking the index of a value of a list
#index of apollo 11
print("Index of Apollo 11:", apollo_moon.index(11))

#reverse a list (in place)
apollo_moon.reverse()
print("Reverse:", apollo_moon)

#reversing a list without modifying it
print("Back to normal:", apollo_moon[::-1])

#################################################
#Denis' fav Apollo mission, Apollo 12

apollo12_crew=["Pete", "Rick", "Al"]

commander=apollo12_crew[0]
cm_pilot=apollo12_crew[1]
lm_pilot=apollo12_crew[2]

#or...

commander, cm_pilot, lm_pilot = apollo12_crew #much nicer, but if the list is longer, will throw an error

print(commander, cm_pilot, lm_pilot)

#2D list, list of lists
list2D=[[1,2], [3,4]]
print(list2D)

#access elements of multidimensional lists
print(list2D[0][1])

#Weird Lists
mission_details=[1969, 'Apollo 12', ['Condrad', 'Gordon', 'Bean'], 10.19194]
print(mission_details)

print(lm_pilot, mission_details[2][2])

#################################################

ww2=[1939, 1940, 1941, 1942, 1943, 1944, 1945]
ww2=map(str,ww2) #get <map object at 0x1005a3eb0>, trying to optimize

ww2=list(map(str,ww2)) #gets list elements
print(ww2)

#Joining list objects by delimiter
print(', '.join(ww2))

#################################################

a=[1,2,3,4]
b=['10','11','12','13']

print(int("5" +b[-1])+a[1]) #on quiz lol 

#################################################
#list operations

x=[1, 2, 20, 21, 22, 23, 1, 1]
print(sum(x))
print(max(x))
print(min(x))

print(x.count(1))

#sorting in place
x.sort()
print(x)

#reverse list in place
x.reverse()
print(x)

print(sorted(x).reverse())

#################################################

#Lists: shallow vs deep copy

a=[1,2,3,4]
#shallow copy, a is now b, only passes along a reference to a
b=a

print(a,b)
a[0]=100
print(a,b)

#deep copying - actually creates a new list

b=list(a)

a[0]=0
print(a,b)

#################################################
#QUIZ 1
#1: Math Operaters
#2: Indexing a string
#3: General List Question
#4: Indexing Harder (Multi-Layer)
#5: Apply Operators (last section)


a=3**3
print(a)

x='pizza'
print(x[0:2])

z=59+78
print(z)

a = [12, 78, 51, 2, 6, 47]
print(a[2:5])

x = [10, [3.14, 20, [30, 'cat', 2.718]], 'dog']

print(x[1][2][1][2])

#################################################
#Dictionaries 
'''
dictionary={'squat':260, 'bench':135, 'deadlift':310}

print(dictionary['bench'])

phonebook={}
phonebook['Holmes'] = {name:"Sherlock", address:"221B Baker Street", city:"London", country:"UK", tel:44168700973}
phonebook['Potter'] = ["Harry", "4 Privet Drive", "Surrey", "UK", 44168700975]
'''
#################################################
#Rock Paper Scissors

#rock beats scissors
#scissors beats paper
#paper beats rock

print("Welcome to Rock, Paper Scissors: enter 4 for rock, 5 for paper, 8 for scissors, player 1 go: ")

a=int(input())
print("Player 1:",a)
print("Player 2 go:")
b=int(input())
print("Player 2:",b)

if a > b:
    print("Player 1 Wins")


if a < b:
    print("Player 2 Wins")


if a==b:
    print("Draw")


