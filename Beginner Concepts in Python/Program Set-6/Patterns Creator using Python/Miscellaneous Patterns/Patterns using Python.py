#!/usr/bin/env python
# coding: utf-8

# # Program to print different patterns using python loop

# ## 1. Star-Pattern:

# In[1]:


'''
SIMPLE HALF-PYRAMID PATTERN:
*
* *
* * *
* * * *
* * * * *
'''

n = int(input('Enter the number of rows: '))    

# outer loop to handle number of rows
for row in range(1,n+1):          
    
    # outer loop to handle number of columns and values is changing according to outer loop
    for column in range(1,row+1):     
        
        # printing stars
        print('*',end=' ')
        
    # ending line after each row
    print()


# In[2]:


'''
DOWNWARD HALF-PYRAMID PATTERN:
* * * * *
* * * *
* * *
* *
*
'''

n = int(input('Enter the number of rows: '))  

for row in range(n,0,-1):
    for column in range(1,row+1):
        print('*',end=' ')
    print()


# In[3]:



'''
Half-TRIANGLE PATTERN:
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

n = int(input('Enter the number of rows: '))

for row in range(1,n+1):
    for column in range(1,row+1):
        print('*',end=' ')
    print()

for row in range(n-1,0,-1):
    for column in range(1,row+1):
        print('*',end=' ')
    print()


# ## 2. Number-Pattern:

# In[4]:


'''
NUMBER PATTERN DISPLAYING NUMBER OF ROWS:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
n = int(input('Enter the number of rows: '))  

# outer loop will print number of rows
for row in range(1,n+1):
    # inner loop will print the value of rows after each iteration
    for column in range(1,row+1):
        print(row,end=' ')
    print()


# In[5]:


'''
NUMBER PATTERN DISPLAYING NUMBER OF COLUMNS:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

n = int(input('Enter the number of rows: '))

for row in range(1,n+1):
    for column in range(1,row+1):
        print(column, end=' ')
    print()


# In[6]:


'''
NUMBER PATTERN DISPLAYING NUMBER OF ROWS*COLUMNS:
11 
12 22 
13 23 33 
14 24 34 44 
15 25 35 45 55 
'''

n = int(input('Enter the number of rows: '))

for row in range(1,n+1):
    for column in range(1,row+1):
        print("{0}{1}".format(column,row),end=' ')
    print()


# In[7]:


'''
NUMBER PATTERN DISPLAYING NUMBER OF COLUMNS*ROWS:
11 
21 22 
31 32 33 
41 42 43 44 
51 52 53 54 55 
'''

n = int(input('Enter the number of rows: '))

for row in range(1,n+1):
    for column in range(1,row+1):
        print("{0}{1}".format(row,column),end=' ')
    print()


# In[8]:


'''
NUMBER PATTERN DISPLAYING NUMBER OF COLUMNS*ROWS AS HALF-TRIANGLE:
11 
21 22 
31 32 33 
41 42 43 44 
51 52 53 54 55 
41 42 43 44 
31 32 33 
21 22 
11 
'''

n = int(input('Enter the number of rows: '))

for row in range(1,n+1):
    for column in range(1,row+1):
        print("{0}{1}".format(row,column),end=' ')
    print()
    
for row in range(n-1,0,-1):
    for column in range(1,row+1):
        print("{0}{1}".format(row,column),end=' ')
    print()


# In[9]:


'''
NUMBER PATTERN DISPLAYING NUMBERS IN INCREASING ORDER:
01 
02 03 
04 05 06 
07 08 09 10 
11 12 13 14 15 
16 17 18 19 
20 21 22 
23 24 
25 
'''

n = int(input('Enter the number of rows: '))

sum = 0
for row in range(1,n+1):
    for column in range(1,row+1):
        sum = sum+1
        print("{:2d}".format(sum),end=' ')
    print()
    
for row in range(n-1,0,-1):
    for column in range(1,row+1):
        sum = sum+1
        print("{0}".format(sum),end=' ')
    print()


# In[10]:


'''
NUMBER PATTERN DISPLAYING NUMBER IN INCREASING ORDER AS TWO-DIGITS:
01 
02 03 
04 05 06 
07 08 09 10 
11 12 13 14 15 
16 17 18 19 
20 21 22 
23 24 
25 
'''

n = int(input('Enter the number of rows: '))

sum = 0
for row in range(1,n+1):
    for column in range(1,row+1):
        sum = sum+1
        print("{:02d}".format(sum),end=' ')
    print()
    
for row in range(n-1,0,-1):
    for column in range(1,row+1):
        sum = sum+1
        print("{0}".format(sum),end=' ')
    print()


# ## 3. Alphabet-Pattern:

# In[11]:


'''
A 
A A 
A A A 
A A A A 
A A A A A 
'''

n = int(input('Enter the number of rows: '))    

ch = 65
for row in range(1,n+1):
    for column in range(1,row+1):
        print("{0}".format(chr(ch)),end=' ')
    print()


# In[12]:


'''
A 
A B 
A B C 
A B C D 
A B C D E 
'''

n = int(input('Enter the number of rows: '))

ch = 64   
for row in range(1,n+1):
    for column in range(1,row+1):
        print("{0}".format(chr(ch+column)),end=' ')
    print()


# In[13]:


'''
A 
A B 
A B C 
A B C D 
A B C D E 
A B C D 
A B C 
A B 
A 
'''

n = int(input('Enter the number of rows: '))

ch = 64   
for row in range(1,n+1):
    for column in range(1,row+1):
        print("{0}".format(chr(ch+column)),end=' ')
    print()
    
for row in range(n-1,0,-1):
    for column in range(1,row+1):
        print("{0}".format(chr(ch+column)),end=' ')
    print()


# In[14]:


'''
A 
B B 
C C C 
D D D D 
E E E E E 
D D D D 
C C C 
B B 
A 
'''

n = int(input('Enter the number of rows: '))

ch = 64   
for row in range(1,n+1):
    for column in range(1,row+1):
        print("{0}".format(chr(ch+row)),end=' ')
    print()
    
for row in range(n-1,0,-1):
    for column in range(1,row+1):
        print("{0}".format(chr(ch+row)),end=' ')
    print()


# In[15]:


'''
A 
B C 
D E F 
G H I J 
K L M N O 
P Q R S 
T U V 
W X 
Y 
'''

n = int(input('Enter the number of rows: '))

ch = 64   
for row in range(1,n+1):
    for column in range(1,row+1):
        ch = ch+1
        print("{0}".format(chr(ch)),end=' ')
    print()
    
for row in range(n-1,0,-1):
    for column in range(1,row+1):
        ch = ch+1
        print("{0}".format(chr(ch)),end=' ')
    print()


# In[ ]:




