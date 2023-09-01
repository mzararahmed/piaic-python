#!/usr/bin/env python
# coding: utf-8

# ## List Functions

# In[12]:


names = ["start", "end", "step"]


# In[10]:


dir(names)


# In[8]:


print(names)


# In[13]:


names.append("chal bay")
print(names)


# In[11]:


names.clear()
print(names)


# In[23]:


names1 = names              #shallow-copy
print("Original List: "+str(names))
print("Shallow-copied List: "+str(names1))


# In[15]:


new_list = names.copy()     #deep-copy
print(new_list)


# In[30]:


names = ['a', 'b', 'c', 'd', 'a', 'f']
print(names.count("a"))


# In[32]:


name2 = ['w', 'x', 'y', 'z']
miss = names.extend(name2)
print(miss)
print(name2)
print(names)


# In[42]:


print("-"+str(len(names) - names.index('a', 1)))
print(names.index('a', 1))


# In[45]:


names.clear()
names.insert(0, 'A')
names.insert(0, 'B')
names.insert(0, 'C')
print(names)
names.insert(1, 'D')
print(names)


# In[46]:


l1 = ['A', 'B', 'C']
print(l1)
a = l1.pop()
print(a)
print(l1)


# In[49]:


l1 = ['A', 'B', 'C']
a = del l1[0]
print(a)
print(l1)


# In[52]:


l1 = ['A', 'B', 'C']
a = l1.pop(1)
print(a)
print(l1)


# In[54]:


names = ['a', 'b', 'c', 'd', 'a', 'f']
names.remove('a')
print(names)


# In[57]:


names = ['a', 'b', 'c', 'd', 'a', 'f']
l1 = names.reverse()
print(l1)
print(names)


# In[61]:


names = ['a', 'b', 'c', 'd', 'a', 'f']
names.sort(reverse = True)
print(names)


# In[65]:


l1 = ['A', 'B', 'C']
print(['A'] + ['C', 'D'])
print(l1.__add__(['F','E']))
print(l1)


# In[67]:


l1.__class__


# In[68]:


print(l1.__contains__('A'))


# In[70]:


l1 = ['A', 'B', 'C']
l2 = ['A', 'B', 'C']
l3 = ['A', 'E', 'C']
print(l1.__eq__(l2))
print(l1.__eq__(l3))


# In[81]:


l1 = [5, 4, 3]
l2 = [1, 2, 3]
l3 = [7, 9, 18]
print(l1.__ge__(l2))
print(l1.__ge__(l3))
print(l1.__le__(l2))
print(l1.__le__(l3))


# In[83]:


["pakistan"] * 10


# # Loop

# #### counter
# #### Login
# #### increment / decrement

# ###### 1.while
# ###### 2. for

# In[91]:


counter = 1
while counter <= 10:
    print("Pakistan", counter)
    counter += 1


# In[99]:


counter = 100
while counter >= 90:
    print("Pakistan", counter)
    counter -= 1


# #### for (count: logic: increment)  // Old methods of "for" looping

# In[96]:


for i in range(1, 11):
    print("Pakistan", i)


# In[97]:


primes = [2, 3, 5,7, 11, 13, 17, 23]
for prime in primes:
    print(prime)


# ##### List Comprehensive

# In[103]:


["Pakistan: " + str(x) for x in primes]


# # Tuple

# In[105]:


for i in range(1, 11):
    print(2, " X ", i , " = ", 2*i)


# In[107]:


for i in range(1, 11):
    print("2 X " + str(i) + " = " + str(2*i))


# In[109]:


["2 X " + str(i) + " = " + str(2*i) for i in range(1, 11)]


# In[111]:


a = (1,2,3,2,1)
a.count(1)


# In[113]:


a.index(3)


# ## gather name, fathername, contact,  add it to list.....ask if you want to add more values until prompted to do so.

# In[120]:


prompt = "Y"
print("Welcome, Enter First user's name")
l1 = []
while prompt == "Y":
    a = input("Name: ")
    b = input("Father's name: ")
    c = input("Contact no: ")
    current_info = [a, b, c]
    l1.append(current_info)
    prompt = input("Continue or end Y/N: ")
print(l1)


# ## 990-1000 in reverse using for and while loop

# In[133]:


for i in range(1000, 989, -1):
    print(i)


# In[127]:


counter = 1000
while counter >= 990:
    print(counter)
    counter -= 1


# In[6]:


[str(chr(x)) + "    " + str(chr(x + 24)) + "    " + str(chr(x + 48)) for x in range(48, 57)]


# ### print tables ( from 1 to given number ) in a tabular format

# In[4]:


lastrange = input("enter your range: ")
lastrange = int(lastrange)
for i in range(1, 11):
    for j in range(1, lastrange +1):
        print(str(i) + " X " + str(j) + " = " + str(i*j), end = "\t\t ")
    print()


# ### return row and column number of every element that is divisible by 5

# In[162]:


a = [[2,5,9], [8,9,10], [20,30,27], [35,9,20]]
for ri, r in enumerate(a):
    for ci, c in enumerate(r):
        if(c % 5 == 0):
            print((ri,ci),c, end =" ")
    print()


# ## in 1 - 1000... print all number all numbers divisible by 5, 7 or 20

# In[1]:


for i in range(1, 1001):
    if(i%5== 0 or i%7 == 0 or i%20 == 0):
        print(i)


# In[3]:


initiator = input("Initiator was(boy, friend or girl): ")
if(initiator == 'boy'):
    slap = input("slapped? y/n: ")
    if(slap == "y" or slap == "Y"):
        print("That's customer Feedback")
    else:
        husband = input("Introduced to husband y/n: ")
        if(husband == "y" or husband == "Y"):
            print("That's demand and supply gap")
        else:
            print("That's direct marketing")
elif(initiator == 'friend'):
    print("That's advertising")
elif(initiator == "girl"):
    print("That's brand recognition")
else:
    print("Not allowed to enter other markets")


# In[ ]:




