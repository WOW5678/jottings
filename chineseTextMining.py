# -*- coding:utf-8 -*-
'''
function:介绍中文文本挖掘的一般步骤
1. 分词
2. 去掉停用词
3.特征处理（向量化）
4.建立分析模型
'''
import jieba

# 对于一些人名和地名，jieba处理不好，可以通过手动加入这些词汇改进分词效果
jieba.suggest_freq('沙瑞金',True)
jieba.suggest_freq('易学习',True)
jieba.suggest_freq('王大陆',True)
jieba.suggest_freq('李达康',True)

with open('data/nlp_test0.txt') as f1:
    document=f1.read()
    # document_decode=document.decode('GBK')
    document_cut=jieba.cut(document)
    result_test0=' '.join(document_cut)
    #result=result.encode('utf-8')
    with open('data/nlp_test1.txt','w') as f2:
        f2.write(result_test0)
with open('data/nlp_test2.txt') as f:
    document=f.read()
    document_cut=jieba.cut(document)
    result_test2=' '.join(document_cut)
    with open('data/nlp_test3.txt','w') as f2:
        f2.write(result_test2)

# 引入停用词
stop_dict=open('data/stop_words/stop_words.txt','r')
stop_content=stop_dict.read()
#将停用词词表转换为list
stopwordsList=stop_content.splitlines()
print(stopwordsList)
stop_dict.close()

#特征处理
from sklearn.feature_extraction.text import TfidfVectorizer
corpus=[result_test0,result_test2]
vector=TfidfVectorizer(stop_words=stopwordsList)
tfidf=vector.fit_transform(corpus)
print('tfidf:',tfidf)
# 查看每个词与IF-IDF的对应关系
wordlist=vector.get_feature_names() # 获取词袋模型中所有的词
# tf-idf矩阵 元素a[i][j]表示第i个文档中的第j个词的tf-idf权重
weightlist=tfidf.toarray()
print('tfidf array:',weightlist)
# 打印每类文本的tf-idf词语权重，
for  i in range(len(weightlist)):
    print('-------第'+str(i)+'段文本的词的tf-idf的值--------')
    for j in range(len(wordlist)):
        print('单词：%s,权重:%f'%(wordlist[j],weightlist[i][j]))