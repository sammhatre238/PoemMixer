
# coding: utf-8

# In[5]:


def word_mixer(word_list) :
    new_words = list()
    word_list.sort()
    while len(word_list) > 5 :
        new_words.append(word_list.pop(-5))
        new_words.append(word_list.pop(0))
        new_words.append(word_list.pop(-1))
        new_words.append("\n")
    return new_words
          
poem = input ("enter a saying or poem :") 
words_list = poem.split()
i=0
for word in words_list :
    if len(word) <= 3 :
        word = word.lower()
        words_list[i] = word
    elif len(word) >= 7 :
        word = word.upper()
        words_list[i] = word
    i+=1
    
x = word_mixer(words_list)
y=len(x)
for wrd in range(y) :
    print(x[wrd], end=' ')

