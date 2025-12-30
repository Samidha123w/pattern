#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num1 = 2
num2 = 5

for num in [num1, num2]:
    print(f"\nTable of {num}")
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

