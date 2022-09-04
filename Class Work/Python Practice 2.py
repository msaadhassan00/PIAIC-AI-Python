#!/usr/bin/env python
# coding: utf-8

# Functions: Local vs Global Variables

# Global Variable

# In[1]:


what_to_say = "Hi"

def say_something():
    print(what_to_say)
    
say_something()


# Local Variable

# In[7]:


def greeting():
    greet = "Hello"
    print(greet)
    
# this code will not run because "greet" in not a global variable
print(greet)


# In[10]:


def numbers():
    x = 1
    print(x)
    y = 2
    print(y)
    z = 3  
    print(z)
    
numbers()


# Functions within Functions

# In[14]:


def say_something():
    what_to_say = "Hello World"
    now_say_it()
    
    
def now_say_it():
    print(what_to_say)
    

now_say_it()


# Functions withing Functions (Argunment)

# In[16]:


def say():
    greet = "Hello"
    now_say(greet)
    
def now_say(content):
    print(content)
    
say()


# For Loop:

# In[21]:


cities = ['Karachi','Peshawar','Lahore','Islamabad','Faisalabad']

city = input("Enter City:")

for cit in cities:
    if city == cit:
        print("Found")


# While Loop:

# In[25]:


user_input = ""
while user_input != 'q':
    user_input = input("Enter 'q' to stop / Enter Anything to Continue: ")
    if user_input == 'q':
        print("Stopped")


# While Loop: Setting a Flag

# In[26]:


Keep_loop = True
while Keep_loop == True:
    user_input = input("Enter 'q' to stop / Enter Anything to Continue:")
    if user_input != 'q':
        print(user_input)
    else:
        Keep_loop = False


# Class & Object:

# In[27]:


class Name:
    first_name = "Ali"
    
#creating object 
obj = Name()
print(obj.first_name)


# The __init__() Function:
#     
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
# 
# To understand the meaning of classes we have to understand the built-in __init__() function.
# 
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# 
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# In[29]:


class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        

obj = Person("Ali",19)
print(obj.name)
print(obj.age)


# Assignment - 04

# In[60]:


def bill_main(monthly_units):
    elec_chrg = electricity(monthly_units)
    print("Electric Charges For", monthly_units, " = ", elec_chrg)
    
    uniform_chrg = uniform(monthly_units)
    print("Uniform Charges For", monthly_units, " = ", uniform_chrg)
    
    fuel_chrg = fuel(monthly_units)
    print("Fuel Charges For", monthly_units, " = ", fuel_chrg)
    
    sales_tax = tax(monthly_units)
    print("Sales Tax For", monthly_units, " = ", sales_tax)

    advance_tax = advance(monthly_units)
    print("Advance Tax Charges For", monthly_units, " = ", advance_tax)
    
    tv_fee = tv(monthly_units)
    print("Tv Fee For", monthly_units, " = ", tv_fee)
    
    tot = total(elec_chrg,uniform_chrg,fuel_chrg,sales_tax,advance_tax,tv_fee)
    print("Total Bill is:", tot)
    
def electricity(a):
    if a <= 100:
        payAmnt = a* 500
        return payAmnt
    if a <= 200:
        payAmnt= a* 1000
        return payAmnt
    if a <= 300:
        payAmnt= a* 1500
        return payAmnt
    
def uniform(b):
    if b <= 100:
        unif = b * 100
        return unif
    if b <= 150:
        unif = b * 56
        return unif
    if b <= 200:
        unif = b * 23
        return unif

def fuel(c):
    if c <= 100:
        f = c * 130.5
        return f
    if c <= 200:
        f = c * 140.5
        return f
    if c <= 300:
        f = c * 150.5
        return f
    
    
def tax(d):
    if d <= 50:
        t = d * 30
        return t
    if d <= 100:
        t = d * 60
        return t
    if d <= 150:
        t = d * 90
        return t
    


def advance(e):
    if e <= 100:
        a = e * 10
        return a
    if e <= 200:
        a = e * 20
        return a
    if e <= 300:
        a = e * 30
        return a
    
def tv(f):
    if f <= 100:
        tv = f * 10
        return tv
    if f <= 200:
        tv = f * 20
        return tv
    if f <= 300:
        tv = f * 30
        return tv
    
    
def total(a,b,c,d,e,f):
    tot = a + b + c + d + e + f
    return tot


bill_main(45)
    


# In[ ]:




