#!/usr/bin/env python
# coding: utf-8

# # Built-in functions for string operations// upper(),lower(),title(),isupper(),islower(),istitle(),isspace(),isalnum(),isalpha(),isdigit(),

# In[90]:


a = 'hello world!'
b = "            "
c = "Ibiza 101"


# In[91]:


len(a) #Returns the length of the string


# In[92]:


a.upper() #Converts the content of the string to UPPERCASE


# In[93]:


a.lower() #Converts the content of the string to LOWERCASE


# In[94]:


a.title() #Converts the content of the string to LOWERCASE


# In[95]:


#BOOLEAN OPERATORS applied to upper.lower.title!


# In[97]:


a.islower() #Checks if input IS LOWERCASE and returns TRUE or FALSE
#1.True- If all characters in the string are lower.
#2.False- If the string contains 1 or more non-lowercase characters.


# In[98]:


a.isupper() #Checks if input IS UPPERCASE and returns TRUE or FALSE.
# 1.True- If all characters in the string are upper.
#2.False- If the string contains 1 or more non-uppercase characters.


# In[99]:


a.istitle() #Checks if input HAS EACH CHARACTER CAPITALIZED  and returns TRUE or FALSE
#1.True- If all characters in the string are lower.
#2.False- If the string contains 1 or more non-lowercase characters.


# In[100]:


a.isspace() #Checks if input contains ONLY SPACES, in this case no, so FALSE


# In[101]:


b.isspace() #Checks if input contains ONLY SPACES, in this case yes, so TRUE


# In[102]:


a.isalnum() #Checks if input contains alphanumeric characters.


# In[103]:


b.isalnum() #Checks if input contains alphanumeric characters.


# In[104]:


c.isalnum() #Checks if input contains alphanumeric characters.


# In[105]:


a.isalpha()


# In[106]:


b.isalpha()


# In[107]:


c.isalpha()


# In[108]:


a.isdigit() #Checks whether the strings contains digits ONLY!


# In[109]:


b.isdigit() #Checks whether the strings contains digits ONLY!


# In[110]:


c.isdigit() #Checks whether the strings contains digits ONLY!


# In[ ]:




