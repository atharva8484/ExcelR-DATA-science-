#!/usr/bin/env python
# coding: utf-8

# # Variables in Python

# In[1]:


#Variables act s a container to sstore data in mamory space
#variables are pointer towards object in python
#variables can start with letters or underscore
#you cannit include special characters while a creating a variable

#Important pointd to remenber while creatinga variable
#1.Python is case sensitive
#2. If variable name involves more than 2 words, join those words with underscore.
#3. Give meningfull names


# In[2]:


#variables
10


# In[3]:


a=10


# In[4]:


id(a)


# In[5]:


nanme2='Thunder'


# In[6]:


nanme2


# In[7]:


#single line comment


# In[8]:


age=60# age is 60
age


# In[9]:


#Multiline comment
'''This is a multiline comment'''


# In[10]:


age


# In[11]:


print('Atharva')#Print 


# ## Operators in python

# 
# Comparison operators (==,!=,<,>, <=,>=)
# Logical operators (and, or)
# Identity operators (is, is not)
# Membership Operators (in, not in)

# In[12]:


num1=222
num2=12


# In[13]:


print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)


# ## Comparision Operators

# In[14]:


a=2
b=3


# In[15]:


a==b#return boolen value


# In[16]:


a!=b#a not equal to b


# In[17]:


a < b#'a' is less than the value of variable 'b'.


# In[18]:


a<=b#less than equal to


# In[19]:


b>a


# ## Logical Operator

# In[20]:


x=10
y=11


# In[21]:


x>y and x>4


# In[22]:


x<y or x>4


# ## Identity Operator

# In[23]:


x,y


# In[24]:


x is y


# In[25]:


x is not y


# ## Membership Opeators

# In[26]:


course='Data_Science'


# In[27]:


's' in course


# In[28]:


' 'in course


# In[29]:


'Data'in course


# ## Data types in python

# ### 1. Integer 2.float 3. String 4.Boolen
# 

# In[30]:


#Integer
pin_code=2222
pin_code
type((pin_code))


# In[31]:


type(pin_code)


# In[32]:


temp=23.2
type(temp)


# In[33]:


logical=True
type(logical)


# In[34]:


#String Creation


# In[35]:


s = 'We are learning python'
s1 = "We are learning python"
s2 = '''We are learning python'''


# In[36]:


s==s1


# In[37]:


s==s2


# In[38]:


st = "It's a laptop"


# In[39]:


st


# ## Type casting
# 

# Typecasting is use to change the data type 

# In[40]:


age
type(age)


# In[41]:


x = str(age)
type(x)


# In[42]:


int(x)


# In[43]:


float(age)


# In[44]:


age


# In[45]:


bool(-3)


# In[46]:


zero=0
bool(zero)


# In[47]:


#We can convert any type of values to bool type, and the output for all values will be True , 
#Except 0, which is False


# # String methods

# In[48]:


#Creating a string
s


# In[49]:


#Capitalize function


# In[50]:


s1 = 'we are learning python'
s1.capitalize()


# In[51]:


s.capitalize()


# In[52]:


#counting


# In[53]:


s.count('a')


# In[54]:


# Starts with and endswith function


# In[55]:


s


# In[58]:


s.startswith('We')


# In[59]:


s.endswith('python')


# In[60]:


s.find('learning')


# In[61]:


s.find('We')


# In[62]:


#replacing


# In[64]:


s.replace('We','They')# changes the string Temporary


# In[65]:


s


# In[66]:


s=s.replace('We','They')#By declearing it into a veriable it becomes permanent


# In[67]:


#Split


# In[68]:


s


# In[73]:


s[0:4]='We'


# In[74]:


len(s)#length of the string


# In[75]:


s


# In[78]:


s.split(' ')


# In[81]:


s2 = 'They are learning python'
s2


# In[83]:


s2.split()#Return a list of the substrings 
#in the string, using sep as the separator string.


# In[84]:


#Basic function


# In[85]:


s.upper()


# In[86]:


s.lower()


# In[87]:


s.swapcase()


# In[88]:


s1='Atharva'
s2='Thunder'
s1


# In[93]:


s
'*'.join(s)


# ## Data Structures
# 

# 
# 1.List
# 2.Tuple
# 3.Dictionary
# 4.Sets

# Lists
# 1.Lists are the built in data structures in python.
# 2.Lists are heterogenous data structure.
# 3.Lists are mutable

# In[94]:


#Creating Lists


# In[95]:


lst=[]
type(lst)


# In[98]:


lst=[10,12.2,'Thunder',True]
lst


# In[99]:


#append


# In[100]:


lst.append(False)


# In[101]:


lst


# In[102]:


#Count


# In[105]:


lst.count('Thunder')#Just count the occerance


# In[106]:


#Indexing


# In[109]:


lst.index('Thunder')


# In[110]:


lst


# In[111]:


#pop


# In[112]:


lst.pop()#Remove and return item at index (default last).


# In[113]:


lst


# In[114]:


#reverse


# In[115]:


lst.reverse()


# In[116]:


lst


# In[117]:


#remove


# In[118]:


lst.remove(True)


# In[119]:


lst


# In[120]:


#Replaceing elements in lists


# In[121]:


lst


# In[123]:


lst[2]


# In[124]:


lst[2]=5.5


# In[125]:


lst


# ### Tuples 

# 1.Tuple are ordered and heterogenous data structure
# 2.Tuples are immutable

# In[126]:


t=()
type(t)


# In[127]:


t=(10,5.5,True,'Thunder')


# In[128]:


t


# In[129]:


t.count(5.5)


# In[130]:


#Accessing elements from Tuple


# In[131]:


t[3]


# ### Dictionary

# Python dictonaries are ordered collection of items
# Dictonary is mutable data data structure.
# It has key and value pairs.

# In[132]:


#Creatn an  empty dictonary


# In[133]:


dictionary={}
type(dictionary)


# In[134]:


#Adding elements


# In[138]:


dict={
    'Name': "Atharva",
    'ID':3350,
    'Location':'Pune',
    'Course':'DS'

}


# In[139]:


dict


# In[140]:


#get


# In[141]:


dict.get('Name')


# In[142]:


#items


# In[143]:


dict.items()


# In[145]:


dict.keys()# prints only keys


# In[146]:


#Adding values in dictionary(update)


# In[147]:


dict.update({'Data':2300})


# In[148]:


dict


# In[149]:


dict.pop('Location')


# In[150]:


dict


# In[151]:


dict.values()


# ### Set
# 

# Set is a collection which is unordered,unindexed.
# Set is immutable.
# Sets are unordered, so you cannot be sure in which order the items will appear.
# Sets do not allow duplicate values.
# Once a set is created, you cannot change its items, but you can remove items and add new items.
# As sets are unordered, they do not support indexing and slicing operations.
# 

# In[152]:


#Creating Set


# In[153]:


s={10,20,755,5.55,'Hello'}


# In[154]:


type(s)


# In[156]:


#Set does not allows dublicate values


# In[157]:


s1={10,10.3,10.3,55}


# In[158]:


s1


# In[161]:


s1[1]#Does not support indexing


# In[162]:


#Adding


# In[164]:


s1.add(60)


# In[165]:


s1


# In[166]:


#Pop


# In[167]:


s1.pop()


# In[168]:


s1 = {'blue','red','green'}
s2 = {'yellow','orange','blue'}


# In[170]:


s1.intersection(s2)# shows the interaction between the sets


# In[171]:


s1.union(s2)


# In[173]:


s1.difference(s2)


# In[174]:


s2.difference(s1)


# In[175]:


s1,s2


# In[ ]:


s

