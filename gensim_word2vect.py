# -*- coding: utf-8 -*-
"""
 @Time    : 2018/10/29 0029 下午 4:17
 @Author  : Shanshan Wang
 @Version : Python3.5
 @Function: 使用gensim 模块进行词向量的训练
"""
from gensim.models import word2vec

sentes=[
    'I am a good student'.split(),
    'Good good study day day up'.split()
]
print(sentes)
model=word2vec.Word2Vec(sentes,size=100,window=5, min_count=2, workers=10)
print(model.wv.word_vec('good'))
print(model.wv.most_similar('good',topn=2))
#保存模型得到的词向量到文件
model.wv.save_word2vec_format('word2vec.txt',binary=False)
