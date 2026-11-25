#!/usr/bin/env python
# coding: utf-8

# In[19]:


numbers = list(range(10000))

def using_list_comprehension():
    return [x * 2 for x in numbers]

def using_for_loop():
    result = []
    for x in numbers:
        result.append(x * 2)
    return result


# In[20]:


get_ipython().run_line_magic('timeit', 'using_list_comprehension()')


# In[21]:


get_ipython().run_line_magic('timeit', 'using_for_loop()')


# ## When to use Jupyter Notebook and Python files
# 
# 1. Jupyter Notebook is useful for data analysis and experimentation.
# 2. It allows us to execute code cell by cell.
# 3. Python files are useful for reusable programs.
# 4. Python files are suitable for automation and applications.

# In[22]:


get_ipython().run_line_magic('timeit', 'using_list_comprehension()')


# In[23]:


get_ipython().run_line_magic('timeit', 'using_for_loop()')


# In[24]:


# Week 1 - Day 4
## Task 1 - Terminal, VS Code and Jupyter
### Python Performance Comparison


# 
