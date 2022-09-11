#we need to generate a powerfull password included letters,digits,punctuations
#and need to specify 60% for letters and 40% for digits and pncutuation .


import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

characters_number = input("How many characters for the password")

while True:
    try:
        characters_number = int(characters_number)
        if characters_number < 6:
            print("you need at least 6 characters")
            characters_number = input("please try again")
        else:
            break
    except:
        print("please enter number only")
        characters_number = input("How many characters for the password")


random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))



password = []

for i in range(part1):
    password.append(s1[i]) #30%
    password.append(s2[i]) #30%

for i in range(part2):
    password.append(s3[i]) #20%
    password.append(s4[i]) #20%

random.shuffle(password) #more security and randomly
password = "".join(password[0:])
print(password)



