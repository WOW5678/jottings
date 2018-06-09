# -*- coding:utf-8 -*-
'''
利用NLTK和gensim进行主题建模
实现过程:
1. 即使我们不确定主题是什么，我们也需要提前选择主题的数目
2. 每个文档都被表示成n个主题的分布
3. 每个主题都被表示成m个单词的分布
'''
# 文本清洗
import spacy
#spacy.load('en')
from spacy.lang.en import English
parser=English()

def tokenize(text):
    lda_tokens=[]
    tokens=parser(text)
    for token in tokens:
        if token.is_space:
            continue
        elif token.like_url:
            lda_tokens.append('URL')
        elif token.orth_.startswith('@'):
            lda_tokens.append('SCREEN_NAME')
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet
def get_lemma(word):
    # wordnet.morphy(word):获取原词
    lemma=wordnet.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma
from nltk.stem.wordnet import WordNetLemmatizer
def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)
# 测试
for w in ['dogs','ran','discouraged']:
    print(w,get_lemma(w),get_lemma2(w))

nltk.download('stopwords')
en_stop=set(nltk.corpus.stopwords.words('english'))
print('en_stop:',en_stop)

def prepare_text_for_lda(text):
    tokens=tokenize(text)
    tokens=[token for token in tokens if len(token)>4]
    tokens=[token for token in tokens if token not in en_stop]
    tokens=[get_lemma(token) for token in tokens]
    tokens=[get_lemma2(token) for token in tokens]
    return tokens
import random
text_data=[]
with open('data/dataset.csv') as f:
    for line in f:
        tokens=prepare_text_for_lda(line)
        if random.random()>0.99:
            print('tokens:',tokens)
            text_data.append(tokens)
from gensim import corpora
dictionary=corpora.Dictionary(text_data)
print('dictionary:',dictionary)
corpus=[dictionary.doc2bow(text) for text in text_data]
# (token_id, token_count)
print('corpus:',corpus)
import pickle
pickle.dump(corpus,open('corpus.pkl','wb'))
dictionary.save('dictionary.gensim')

# Try 5 topics
import gensim
Num_topics=5
ldamodel=gensim.models.ldamodel.LdaModel(corpus,num_topics=Num_topics,id2word=dictionary,passes=15)
ldamodel.save('model5.gensim')

# 从每个文档中选择前5个单词
topics=ldamodel.print_topics(num_words=4)
for topic in topics:
    print('topic:',topic)

new_doc='Practical Bayesian Optimization of Machine Learning Algorithms'
new_doc=prepare_text_for_lda(new_doc)
new_doc_bow=dictionary.doc2bow(new_doc)
print('new_doc_bow:',new_doc_bow)
print('get_document_topics:',ldamodel.get_document_topics(new_doc_bow))

ldamodel=gensim.models.ldamodel.LdaModel(corpus,num_topics=3,id2word=dictionary,passes=15)
ldamodel.save('model3.gensim')
topics=ldamodel.print_topics(num_words=4)
for topic in topics:
    print('topic:',topic)

# PYLDAvis
dictionary=gensim.corpora.Dictionary.load('dictionary.gensim')
corpus=pickle.load(open('corpus.pkl','rb'))
lda=gensim.models.LdaModel.load('model5.gensim')



