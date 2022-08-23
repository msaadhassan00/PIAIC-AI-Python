#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# PIAIC AI ASSIGNMENT
# Roll No:PIAIC178673
# M Saad Hassan


# In[2]:


# 1.Simple Message: Assign a message to a variable, and then print that message.

message = "Education is a key to success"
print(message)


# In[3]:


# 2.Find a quote from a famous person you admire. Print the quote and the name of its author.
# Your output should look something like the following, including the quotation marks:
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”

print('Quaid-e-Azam once said, "I do not believe in taking the right decision, I take a decision and make it right."')


# In[5]:


# Calculate Area of a Circle::
# Write a Python program which accepts the radius of a circle from the user and compute the area.
# Program Console Sample Output 1:
# Input Radius: 0.5
# Area of Circle with radius 0.5 is 0.7853981634

from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# In[9]:


# Check Number either positive, negative or zero::
# Write a Python program to check if a number is positive,
# negative or zero
# Program Console Sample Output 1:
# Enter Number: -1
# Negative Number Entered
# Program Console Sample Output 2:
# Integer: 3
# Positive Number Entered
# Program Console Sample Output 3:
# Integer: 0
# Zero Entered

num = int(input("Enter Number: "))
if num == 0:
    print("Zero Entered")
elif num > 0:
    print("Positive Number Entered")
else:
    print("Negative Number Entered")
    


# In[11]:


# Vowel Tester Write a Python program to test whether a passed letter is a vowel or not
# Program Console Output 1:
# Enter a character: A
# Letter A is Vowel
# Program Console Output 2:
# Enter a character: e
# Letter e is Vowel
# Program Console Output 2:
# Enter a character: N
# Letter N is not Vowel.

check = input("Enter a Character: ")

if(check=='A' or check=='a' or check=='E' or check =='e' or check=='I' or check=='i'
   or check=='O' or check=='o' or check=='U' or check=='u'):
    print(check, "is a Vowel")
else:
    print(check, "is a Consonant")


# In[12]:


# BMI Calculator
# Write a Python program to calculate body mass index Program Console Sample 1:
# Enter Height in Cm: 180
# Enter Weight in Kg: 75
# Your BMI is 23.15

hght=float(input("Input Height in Cm : "))
wght=float(input("Input Weight in Kg : "))
BMI = wght / (hght/100)**2
print("Your BMI is ",BMI)


# In[13]:


# List::
# Store the names of a few of your friends in a list called names
# Print each person’s name by accessing each element in the list, one at a time.

friends = ["Wasif" , "Shehroz" , "Saif" , "Shahmeer"]

print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

print(friends)


# In[14]:


# Start with the list you used in Question 4, but instead of just printing each person’s name,
# print a message to them. The text of each message should be the same,
# but each message should be personalized with the person’s name.

friends = ["Wasif" , "Shehroz" , "Saif" , "Shahmeer"]

print(friends[0],"Developer")
print(friends[1],"Doctor")
print(friends[2],"Builder")
print(friends[3],"Developer")


# In[15]:


# .Make a python program that conatains your nine favourite dishes in a list called foods.
# Print the message, The first three items in the list are:
# Then use a slice to print the first three items from that program’s list.
# Print the message, Three items from the middle of the list are:
# Use a slice to print three items from the middle of the list.
# Print the message, The last three items in the list are:
# Use a slice to print the last three items in the list.

foods_list=["Karahi","Zinger Burger","Biryani","Pizza","Pizza Fries","Rolls","Haleem","Nehari","Daal"]
print("The first three items in the food list are :",foods_list[:3] )
print("The first three items in the food list are :",foods_list[3:6] )
print("The first three items in the food list are :",foods_list[-3:] )


# In[19]:


# Start with your program from your last Question8. Make a copy of the list of foods,
# and call it friend_foods. Then, do the following:
# Add a new dish to the original list.
# Add a different dish to the list friend_foods.
# Prove that you have two separate lists.
# Print the message, My favorite pizzas are: and then use a for loop to print the first list.
# Print the message,
# My friend’s favorite foods are:, and then use a for loop to print the second list.
# NOTE: Make sure each new dish is stored in the appropriate list.

foods_list=["Karahi","Zinger Burger","Biryani","Pizza","Pizza Fries","Rolls","Haleem","Nehari","Daal"]
friend_foods_list=["biryani","zinger","chinese","pulao","fish","mandi","karahi","nehari","roll"]
foods_list.append("Puloa")
friend_foods_list.append("Beef Burger")
print("My Food List " + "\n")
for food in foods_list:
    print("My favorite foods are :",food ,"\n")
    
    
print("My friend List " + "\n")    
for friend_food in  friend_foods_list:
    print("My friend’s favorite foods are :",friend_food ,"\n")


# In[ ]:




