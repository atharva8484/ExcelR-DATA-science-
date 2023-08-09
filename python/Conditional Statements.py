#!/usr/bin/env python
# coding: utf-8

# # User Input
# 

# 

# In[2]:


Name=input()# every thing inside a input function is a string by default


# In[3]:


Name


# In[4]:


Age=input('Enter your age')


# In[5]:


Age


# In[7]:


type(Age)


# In[9]:


num11=int(input('Enter the frist number'))
num2=int(input ('Enter the second number'))#Type casting
sum=num11+num2
sum


# # Condational Statements

# # If,else,eif

# In[11]:


userid='Atharva'
if userid=='Atharva':
    print('successfuly login')


# In[12]:


userid='Atharva11'
if userid=='Atharva':
    print('successfuly login')
else:
    print("Try again")


# In[13]:


#Check whether the name of the player is virat koli or not


# In[15]:


Playername=input('Enter the players name')
if Playername=="Virat Koli":
    print('Yes')
else:
    print('No')


# In[16]:


#Check wether the number is positive negative or zero


# In[18]:


num=int(input("Enter the number "))
if num>0:
    print("Number is positive")
elif num<0:
    print("Number is negative")
else:
    print('Number is zeros')


# In[20]:


name='Atharva'
print('Hi! How are you sayali?')
print('Hi How are you',name,'?')


# In[21]:


#Formatting 


# In[22]:


print(f"Hi ,how are you {name}?")


# ### Take input from user, name, age, location,designation
# Write this sentence: My name is 'name'. I am 'age' years old. I live in 'location'. I work as 'designation'

# In[26]:


Name=input("Enter the name")
age=int(input("Enter the age"))
location=input("Enter the location")
designation=input("Enter the designation")
# printing
print(f"My name is {Name}.I am {age} years old.i live in {location}.I work as {designation}.")


# In[ ]:


#Write a python program which tells wether the person is eligiable or not for a vote


# In[28]:


age=int(input("Enter your age in numbers"))
if age>=18:
    print("You are Eligible for voting")
else:
    print("You are not Eligible for voting")


# In[29]:


# Give grades based on percentages
#A : marks >85
#B : marks < 85 and >70
#C : marks <70 and > 60


# In[31]:


marks=int(input("Enter your marks"))
if marks>85:
    print("A grade")
elif (marks<85 and marks>70):
    print("b Grade")
elif( marks<70 and marks>60):
    print("C Grade")
else:
    print('Fail')
    


# #In-Class Exercise:
# Write a program which will print Century if the player has made more than 100 runs else it shold write how many more runs he needs to have to complete the century.
# Write a program to check the number is one digited, two digited and three digited.
# Write a program to check whether the user has entered number 99 or not.
# 

# In[32]:


#Write a program which will print Century if the player has made more than 100 runs else it shold write how many more runs he needs to have tocomplete the century.


# In[33]:


runs=int(input("Enter the runs scored by the player"))
if runs>100:
    print("Century")
else:
    print(f"player needs {100-runs}for a century")


# In[34]:


#Write a program to check the number is one digited, two digited and three digited.


# In[37]:


num=(int(input('Enter the number')))
if num<10:
    print('Number is one digit')
elif num>=10:
    print("Number is 2 digit")
elif num>=100:
    print("Number is 3 digit")
else:
    print("Invlaid")


# In[39]:


#Write a program to check whether the user has entered number 99 or not.


# In[40]:


user=(int(input('Enter the number')))
if user==99:
    print('yes')
else:
    print('No')


# In[ ]:




