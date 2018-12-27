#!/usr/bin/env python
# coding: utf-8

# In[18]:


import gensim


# In[19]:


model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)  


# In[20]:


selected_categories=['capital-world', 'currency', 'city-in-state', 'family', 'gram1-adjective-to-adverb', 'gram2-opposite', 'gram3-comparative', 'gram6-nationality-adjective']
        


# In[21]:


text_file = open("word-test.txt", "r")
lines = text_file.readlines()
lower=False
NextCategory=False


# In[22]:


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
            if d==model.most_similar(positive=[b,c],negative=[a])[0][0]:
                numCorrect=numCorrect+1
            total=total+1
    print('Word2Vec acc:')
    print(category)
    print(numCorrect/total)


# In[23]:


# Problem 3
# Testing with analogies which are not part of Mikolovos data set

#Example 1

print (model. most_similar(positive=['salt','cup'], negative=['pepper'])) 


# In[25]:


# Example 2

print (model. most_similar(positive=['love','life'],negative=['hate']))


# In[26]:


#Example 3

print(model.most_similar(positive=['computer','human'],negative=['cpu']))


# In[27]:


#Example 4
print(model.most_similar(positive=['he','she'],negative=['him']))


# In[28]:


#Example 5

print(model.most_similar(positive=['smarter','faster'],negative=['smartest']))


# In[29]:


#Example 6

print(model.most_similar(positive=['example','word'],negative=['examples']))


# In[ ]:




