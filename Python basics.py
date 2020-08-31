# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 19:14:46 2019

@author: Lenovo
"""


character_name = "pink pANTHER"
character_age = "35"
#########################Variables############
print("there was once a man named " + character_name + " ,")
print("he was "+character_age+ " years old")
print("he really liked the name george")
print("he didn't like being 70")

print("NMIT\nBengaluru")
print("NMIT\"Bengaluru")

########################strings#####################
phrase = "Nmit"
print(phrase +" is not cool")
print(phrase.lower())
print(phrase.upper())
phrase.islower()
print(phrase.upper().isupper())
len(phrase)
phrase[1]
phrase.index("i")
phrase.replace("i" , "a")

#########################numbers####################

print(2.907)
print(-6.89)
print(7/7+5-8)
print((81)**2)
print(10%3)
mynum = 5
print(str(mynum ) + " is my favorite number")

mynum2 = -9
print(abs(mynum2))
print(pow(3,2))
print(max(6,9,8.89))
print(round(5.8965))

from math import *
print(floor(5.8))
print(ceil(5.8))
print(sqrt(6))


############ getting input from users  ######################
name = input("enter your name:")
age = input("Please enter your age:")
print("Hello " + name + " you are " +age)

############ building a basic calculator #############
num1 = input("Enter a number: ")
num2 = input("Enter another number:")

result = float(num1) + float(num2)

print(result)

############ MAD LIBS GAME  ############
color = input("Enter a color: ")
plural = input("Enter a plural:")
celebrity = input("Enter a celebrity:")
print("Roses are " + color)
print(plural + " are blue")
print("I love " + celebrity)


############## lists  ################

Friends = ["Anoop", "Gully", "Kp","Suhel", "Kiran"]
print(Friends)
print(Friends[0])
print(Friends[-1])
print(Friends[1:])
Friends[1:4]
print(Friends[1:4])
Friends[3] = "Varun"
Friends


############## LIST FUNCTIONS  ###############


lucky_numbers = [4,5,6,7,8,9]
friends = ["Anoop", "Gully", "Kp","Suhel", "Kiran", "varun"]
friends.extend(lucky_numbers)
friends.append("shishir")
friends.insert(1, "prajwal")
friends.remove("Kp")
friends.pop()   #########remove last item
friends.clear() #####clears all items
print(friends)
print(friends.index("varun"))
print(friends.count("Anoop")) ##### counts no. of times the item has repeated.
Friends.sort()
Friends.reverse()
friends

################ TUPLES ######################3

a = (   "asasa")

############### FUNCTIONS ########################


def sayhi(name, age):
    print("Hello " +name+ " you are " + str(age))
    

sayhi("vaibhav", 24)


####################### RETURN STATEMENT ################### 1:34:13

def cube(num):
    return num*num*num  ## return allows us to return a value back to the caller of the function# Also python will not accept any code after return statement#

cube(35) #or we could assignement the result say, result = cube(35) and then print (result) to get same answer


######################## IF STATEMENTS #############################

def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num3 and num2>=num1:
        return num2
    else:
        return num3
        
print(max_num(6,9,7))

#################### Guessing game using while loop and if else statements ####################

Secret_word = "python"
guess = ""
guess_count = 0
guess_limit =3
out_of_guesses = False

while guess != Secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
       guess = input("Enter a guess:")
       guess_count += 1
    else:
        out_of_guesses = True
    
if not(out_of_guesses):
    print(" BAM! You have won")
else:
    print("Out of guesses, YOu Lose")
    
    
####################### practise #############################
    
right_Answer = "Delhi" & "delhi" & "DELHI"
No_of_Guesses = 3
Answer = ""
Guess_count = 0

while Answer != right_Answer and Guess_count<(No_of_Guesses):
    if Guess_count < 3:
        print("what is the captial city of India?")
        Answer = input("Enter the Answer here: ")
        Guess_count +=1
    else:
        print("You are out of guesses")
if (Guess_count <3) and (Answer ==right_Answer):
    print("CONGRATS!!! You have WON!!")
else:
    print("Out of guesses, YOU LOSE")

######### End of Practise ############################
    
right_Answer

############### Raise to power using for loop and functions ###################
def raise_to_power (base_num, pow_num):
    result =1
    for i in range(pow_num):
        result = result*base_num
        return result

raise_to_power(6.9,3)

######################## TRY EXCEPT ##################3
count = 1
def power_raising (base_num, pow_num):
    for i in range(pow_num):
        result =1
        while i < pow_num:
            result = result*base_num
            i = 1+i
        return result
            
        


power_raising(5.6,2)
#########################################################################

import kivy
from kivy.app import App





























































































1



























