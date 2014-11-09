__author__ = 'Abdulahad'
import math
print 123 + 345
print 2.0 * 3.1415
print 2.0 * math.pi
print math.pi

import random
print random.choice([1,2,3,4,5])

Str = 'Spam'
print len(Str)

print Str[1]

for a in Str:
    print a

print '****************************************************************************'
#print Str[0:len(Str)]
print Str[0: (len(Str) - 1)]
Str = 'z' + Str[:]
print Str

print Str.find('am')  #Find substring
print Str.replace('am', 'AM') #Replace
print Str
print 4/3
line = "it's spam do not open the message" # Difference between ' "
line = line.capitalize()
print line.split(',')
dir(line)
print help(line.capitalize())


lists = [123, 'spam', 9.67]
print lists
print lists[0]

lists = lists + [2,5,9]

print lists
print (7.0//3)   #Integer division
print (7.0/3)    # Real division
print (3%6)     #Division be module

my_list = ['Ahato', 'Jenny', 6, "Kevin's"]

print (my_list.pop(0))

print (sum(range(10)))

st_name = "Hello babies"
print (st_name.ljust(3))


my_tuple = ('You', 4, 4.5)
print (my_tuple)

my_set = {3,6,4,"Hello"}

print my_set

dict = {'Home':10, 'Uchi':'JP'}
print (dict)

#hi = raw_input("Input a string ")

#num = float(raw_input("Hi "))
age = 18
name = "Piter"
print ("%s is %d years old." %(name, age))  #FormATTING OUTPT
print ("%20d" %(math.pi))








