#!/usr/bin/env python
# coding: utf-8

# In[2]:


a= "Twinkle , twinkle, little star\n       How I wonder whats you are!"
b= "\n        Up above the world, so high,\n         like a diamod in the sky."
c= "\nTwinkle, twinkle, little star,\n      How I wonder wehat you are"
print(a + b + c)


# In[4]:


from datetime import date
today = date.today()
print ("Today's date:",today)


# In[6]:


from datetime import date
today = date.today()
#dd/mm/yy
a1=today.strftime("%d/%m/%y")
print("a1=",a1)
#Texual month, day and year
a2=today.strftime("%B/%m/%y")
print("a2=",a2)
# mm/dd/yy
a3=today.strftime("%m/%m/%y")
print("a3=",a3)
# Mont observation day and year
a4=today.strftime("%b-%m-%y")
print("a4=",a4)


# In[8]:


from datetime import datetime
# datetime object containing curent date and time
now = datetime.now()

print("now=", now)
# dd/mm/yy  H:M:S
dt_string = now.strftime("%d/%m/%y  %H:%M:%S")
print("date and time=", dt_string)


# In[9]:


import platform
print ("python version is given below:")
print(platform.python_version())


# In[13]:


r= int(input("Please Enter RADIUS BELOW\n"))
A= 3.14*r**2
print(A)


# In[16]:


I1 =input("please Enter first name\n")
I2 =input("please Enter first name\n")

print (I1[::-1] + " " +I2[::-1])


# In[21]:


I1 = int(input("please enter first number\n"))
I2 = int(input("please enter second number\n"))
result= I1+I2
print ("Result:")
print(result)


# In[ ]:




