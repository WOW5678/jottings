# -*- coding: utf-8 -*-
"""
 @Time    : 2018/12/24 0024 上午 9:47
 @Author  : Shanshan Wang
 @Version : Python3.5
 @Function: beam search decoder
"""
from numpy import log
from numpy import array
from numpy import argmax
#beam search
def beam_search_decoder(data,k):
    sequences=[[list(),1.0]]
    #walk over each step in sequence
    for row in data:
        print('row:',row)
        #也就是针对每一步都要执行所有可能的单词
        all_condidates=list()
        #expand each current candidate
        for i in range(len(sequences)):
            seq,score=sequences[i]
            for j in range(len(row)):
                candidate=[seq+[j],score*-log(row[j])]
                all_condidates.append(candidate)
        #order all candidates by score
        ordered=sorted(all_condidates,key=lambda tup:tup[1])
        #select k best
        print('ordered:',ordered)
        sequences=ordered[:k]
    return sequences

#Greedy Search Decoder
def greedy_search_decoder(data):
    # index for largest probability each row
    return [argmax(s) for s in data]

if __name__ == '__main__':
    # define a sequence of 10 words over a vocab of 5 words
    data = [[0.1, 0.2, 0.3, 0.4, 0.5],
            [0.5, 0.4, 0.3, 0.2, 0.1],
            [0.1, 0.2, 0.3, 0.4, 0.5],
            [0.5, 0.4, 0.3, 0.2, 0.1],
            [0.1, 0.2, 0.3, 0.4, 0.5],
            [0.5, 0.4, 0.3, 0.2, 0.1],
            [0.1, 0.2, 0.3, 0.4, 0.5],
            [0.5, 0.4, 0.3, 0.2, 0.1],
            [0.1, 0.2, 0.3, 0.4, 0.5],
            [0.5, 0.4, 0.3, 0.2, 0.1]]
    data = array(data)
    # decode sequence
    result = beam_search_decoder(data, 3)
    # print result
    for seq in result:
        print(seq)
    #############################
    # decode sequence
    result = greedy_search_decoder(data)
    print(result)