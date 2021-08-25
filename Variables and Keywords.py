#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Variables : Place holder for texts and numbers that is used to store a value
var1 = 40
var2 = 78.45
var3 = 'This is Python'
var4 = True
print(var1)
print(type(var1))
print(var2)
print(type(var2))
print(var3)
print(type(var3))
print(var4)
print(type(var4))
var1+var2          #addition of two numbers
print(var1+var2)
var1-var2          #subtraction of two numbers
print(var1-var2)


# In[5]:


#Identifiers represent the name of variables, functions, arrays ,labels etc
element1 = 'Hydrogen'
print(element1)
element_1 = 'H'           #only underscore is used from special symbols
print(element_1)
#3element : identifiers cannot start with numbers 
total = 56
print(total)
var = 10
VAR = 20
Var = 30
print(f'var={var}\t VAR={VAR}\t Var={Var}\t')


# In[9]:


#Keywords are the reserved words which couldn't be replaced by identifiers 
import keyword
keyword.kwlist


# In[10]:


#Comments
#this is a single line comment
'''multiple
         line 
             statement'''
var1 = 56          #assignment statement
var2 = (70+56+
              78)  #multilpe line assignment statement
lis = ["lion","tiger","cheeta","deer",
                                       "Bear","Rhino"]
print(var1)
print(var2)
print(lis)


# In[12]:


#Python Indentation
for a in range(0,9):
    print(a)
b=3
if b==3:
    print("The Value of b is 3")
    print("The process is correct")
    if b==3:
        print("the value of b is only 3")
        b=5
        if b==5:
            print("Ohh The Value of b Changed")
            b=7
            if b==7:
                print("This is python Indentation")
                
            else :
                print("Just stop now")
                print("Finished")
    if a==5:
        a=7
        if a==7:
            print(a)


# In[ ]:




