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

print line.upper()