#!/usr/bin/env python
# coding: utf-8

# # Functions

# `In python, there are two types of function.
# Built-in funtions
# User defined function
# We can create our own customized functions in python for code reusability.

# In[1]:


#Basic function


# In[2]:


def simple_function():
    print('This is a function')


# In[4]:


simple_function()


# In[5]:


#Docstring


# In[6]:


def function1():
    '''This function will print 2 sentences.'''
    print('This is first sentence')
    print('This is second sentence')


# In[7]:


function1()


# In[8]:


#Write a python function which will return me the maximum number


# In[15]:


def max_num(num1,num2):
    returnmax(77,5)


# In[20]:


def max_number(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2


# In[21]:


max_number(5,5)


# In[2]:


def max_num1(*numbers):
    return max(numbers)#function to return max number 


# In[3]:


max_num1(100,12,144,11,2,1,1,2,5555,54)


# In[4]:


def combine(text1,text2):
    print(text1+' '+text2)


# In[5]:


combine('Atharva','Thunder')


# In[6]:


s='Atharva'
s[::-1]#reverses the string


# In[7]:


def reverse(text):
    return text[::-1]


# In[8]:


reverse('Thunder')

Create a python function which will take 4 arguments(Id,name, age and department) of employee and it should print the below sentence:
Employee ID is 'Id'.The name of employee is 'name'.He is 'age' years old and he is from 'department' department.
# In[19]:


def employee(ID,Name,AGE,Departments):
    print(f"Employeeid{ID}\n.The name of the employee is {Name}.\n He is {AGE} years old and he is from {Departments}departments ")


# In[20]:


employee(201,'Thunder',21,'IT')


# # Loops

# ## While Loop,For loop
# 

# In[21]:


#while Loops


# In[23]:


python=10
while python>0:
    print('Learning python',python)
    python= python-1
print('Python Completed')    


# In[25]:


age=0
while age<18:
    print("you are under age")
    age =age+1
print('you are eligible')    


# In[26]:


#Range Function
list(range(1,20))


# In[27]:


list(range(1,20,5 ))


# In[28]:


lst=[1,2,3,4,5,6
    ]


# In[29]:


for i in range(1,100):
    print(i)


# In[30]:


lst


# In[32]:


lst.append(55)


# In[33]:


lst


# In[34]:


lst1=[]
for i in range(1,100,2):
    lst.append(i)


# In[36]:


lst1


# In[37]:


for x in range (1,10):
    print(x**2)


# In[38]:


#Company list
company=['Flipkart','Amazon','IBM']
company


# In[39]:


for i in company:
    print(i)


# In[43]:


for i in company:
    print('www.' +i+".Com")


# # In-Class Activity:

# Write a program to store all names which starts with 'A' in a list.
# Take a list of numbers and add 5 to each number.
# Create a list of marks and print only marks > 75.## 

# In[44]:


name=['Atharva','Thunder']


# In[45]:


name


# In[46]:


for i in name:
    if i.startswith("A"):
        print(i)


# In[51]:


num=(1,2,3,4,5,6,7)


# In[52]:


num


# In[54]:


for i in (num):
    print(i+5)


# In[55]:


marks=[66,85,74,96,85,86,84]


# In[56]:


marks


# In[57]:


for i in (marks):
    if i>74:
        print(i)


# In[ ]:




