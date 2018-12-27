#!/usr/bin/env python
# coding: utf-8

# In[28]:


import gensim.downloader as api


# In[29]:


model = api.load("glove-wiki-gigaword-100")


# In[30]:


selected_categories=['capital-world', 'currency', 'city-in-state', 'family', 
                 'gram1-adjective-to-adverb', 'gram2-opposite', 'gram3-comparative', 'gram6-nationality-adjective']
        


# In[31]:


text_file = open("word-test.txt", "r")
lines = text_file.readlines()
total=0
numCorrect=0
NextCategory=False
lower=True 


# In[33]:


for category in selected_categories:
    total=0
    numCorrect=0
    for rowNo in range(1,len(lines)):
        curRow=lines[rowNo]
        if ':' in curRow:
            #This is start of a category
            curRow=curRow.replace('\n','')
            curRow=curRow[2:]
            if curRow==category:
                print('Category Name:')
                NextCategory=False
            else:
                NextCategory=True
        elif NextCategory:
            b=1
        else:
            #Run the analysis
            curRow=curRow.replace('\n','')
            curRow=curRow.replace('\t','')
            splitRow=curRow.split(' ')
            if not lower:
                a=splitRow[0]
                b=splitRow[1]
                c=splitRow[2]
                d=splitRow[3]
            else:
                a=splitRow[0].lower()
                b=splitRow[1].lower()
                c=splitRow[2].lower()
                d=splitRow[3].lower()
            #print(model.most_similar(positive=[b,c],negative=[a]))
            if d==model.most_similar(positive=[b,c],negative=[a])[0][0]:
                numCorrect=numCorrect+1
            total=total+1
    print(category)
    print('Glove accuracy:')
    print(numCorrect/total)


# In[34]:


print(model.most_similar(positive=['woman','king'],negative=['man'])) 


# In[35]:


print(model.most_similar(positive=['thailand','cairo'],negative=['bangkok']))                         


# In[44]:


#Question 3 

# Testing with some Analogies which are not part of Mikolovs analogy data set

# 1st Example

print(model.most_similar(positive=['salt','cup'],negative=['pepper'])) 


# In[45]:


# 2nd Example

print(model.most_similar(positive=['love','life'],negative=['hate'])) 


# In[50]:


# 3rd Example

print(model.most_similar(positive=['computer','human'],negative=['cpu'])) 


# In[47]:


# 4th Example

print(model.most_similar(positive=['he','she'],negative=['him'])) 


# In[48]:


#5th Example

print(model.most_similar(positive=['smarter','faster'],negative=['smartest'])) 


# In[49]:


# 6th Example

print(model.most_similar(positive=['example','word'],negative=['examples'])) 


# In[ ]:





# In[ ]:




