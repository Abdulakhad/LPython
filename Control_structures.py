counter = 1
while counter <= 3:
    print ("Hello")
    counter += 1

for item in [1,2,3,5,8,2,"Jammy"]:
    print (item)

for item in range(1,10):
    print item

word_list = ['Cat', 'dog', 'monkey']
letter_list = []
for a_word in word_list:
    for a_letter in a_word:
        letter_list.append(a_letter)
print(letter_list)

sq_list = []
for x in range(1,100):
    sq_list.append(x*x)
print(sq_list)

sq_list = [x * x for x in range(1,11)]
print(sq_list)

