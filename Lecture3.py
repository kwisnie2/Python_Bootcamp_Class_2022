#############
##LECTURE 3##
#############

#################################################
#More File Manipulation

file_name="data.txt"
data_list=[]
with open(file_name) as f:
    next(f) #skip first line, in this case the header
    for line in f:
        line=line.replace('\n', '') #removes newline character
        line=line.split(',')        #split line into list
        
        #parse the line now
        num=line[0]
        name=line[1].strip()
        epoch=int(line[2])
        elements=list(map(float, line[3:9]))
        ref=line[9]
        data_list.append([num, name, epoch, elements, ref])

print(data_list)

#Wile E. Coyote broke in in JPL, rewrites history
for line in data_list:
    line[1] = 'Coyote'
print(data_list)

#################################################
#String formatting

#Covnerting Floats to strings
x=3.14159
print("{:4.2f}".format(x))

#signed formatting
print("{:+5.2f}".format(x))

#Zero Adding
print("{:06.2f}".format(x))

#more decimal places
print("{:7.5f}".format(x))

#more decimal places than actual demical places
y=2.71
print("{:7.5f}".format(y))
print("{:7.2f}".format(y))

#store formattign string
y_str = "{:7.5f}".format(y)
print(y_str)

#Integers
z=42
print("{:7d}".format(z)) #just spaces

#string
print("{:10}".format("Wile E."))

#align to the right
print("{:>10}".format("Wile E."))

#named arguments
print("{a} {b} {c}".format(a=5, b=8, c=10))
print("{:7.5f}, {:7.3f}, {:5.2f}".format(3.14, 2.71, 42))

#################################################
#Writing a file back
new_file_name='true_data.txt'
with open(new_file_name, 'w') as f:

    #Write the header
    f.write("Num,Name,Epoch,q,e,i,w,Node,Tp,Ref\n")
    for line in data_list:
        #composing a string
        str_line=["{:>3}".format(line[0]), line[1], "{:5d}".format(line[2])]

        #convert all elements using same format
        for element in line[3]:
            str_line.append("{:3f}".format(element))

        #Add reference
        str_line.append(line[-1])
        #print(str_line)

        #convert list to comma delimited string
        final_line=",".join(str_line)
        #print(final_line)

        #Write the line
        f.write(final_line + "\n")

#appending to the file
with open(new_file_name, 'a') as f:
    f.write("Wile E. Was here")

#################################################
#Python modules

from lib2to3.pgen2.token import CIRCUMFLEXEQUAL
import math
print(math.sqrt(2))
print(math.sin(math.pi)) #trig takes radians
print(math.log10(100)) #ln is just log

import random

#get random integer in the 1 to 100 range
print(random.randint(1,100))

#random float between 0,1
print(random.random())

#Shuffle a list
a=[1,2,3,4,5]
random.shuffle(a)
print(a)

#Sample 10 elements from a list
b=range(1,100)
print(random.sample(b, 10))

#Gaussian Distribution
gauss=[]
for i in range(10):
    print(random.gauss(0, 2)) #takes mean, std
    gauss.append(i)


#################################################
#Ways of importing modules

#module alias
import math as m
print(m.sqrt(2))

#can import individual functions 
from math import sqrt
print(sqrt(2))

#Importing all functions from a module, bad idea, names can clash with things you name, 
# other modules can have same name too
from math import *
print(sqrt(2))

#################################################
#File System management
r'''
import os

#list contents of directory
##print(os.listdir('.'))

#print current directory name
print(os.getcwd())

#change current directory one up
os.chdir("..")
print(os.getcwd())

#Directory seperator
print(os.sep)

#making a new directory 
#contruct new path to directory

new_dir_path=os.path.join(os.getcwd(), 'test')
print(new_dir_path)
os.mkdir(new_dir_path)


#make a file and delete it
file_name='top secret.txt'
file_path=os.path.join('.', file_name)
with open(file_path, 'w') as f:
    pass

#Delete the file
if os.path.isfile(file_path):
    os.remove(file_path)
else:
    print('The file does not exist!')

#################################################
#Copy and moving

import shutil

#Make example file 
with open(file_path, 'w') as f:
    pass

copy_path="unclassified.txt"
shutil.copy2(file_path, copy_path)

#move/rename
new_name='public release.txt'
shutil.move(copy_path, new_name)
'''
#QUIZ 3 Notes
x=2.718281828459
print("{:.3f}".format(x))

#question 3 Programming question

#pi Estimation
import math as mt
r=1 # Radius of the cirlce is one

x=random.random() #random x point between 0 to 1
y=random.random() #random x point between 0 to 1

circle_count=[]
circle=(x**2 + y**2)
if circle < 1:
    circle_count.append(circle)
    print(circle_count)
'''
circle_count=[]
N=0
while N < 100:
    N+=1
    for i in N:
        if ((x**2 + y**2) < 1):
            circle_count.append(i)
'''

    

