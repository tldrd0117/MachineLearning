# -*- coding: utf-8 -*-
from numpy import *
import operator

# 데이터셋 생성
def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0,0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

# k-최근접 이웃 알고리즘
# inX 분류를 위한 입력 벡터
# dataSet 전체 행렬
# labels 분류 항목을 표시한 벡터
# k 최근접 이웃 수
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    # 거리계산 유클리드 거리를 사용하여 계산
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    # 가장 짧은 k 거리를 투표
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    #아이템 정렬
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


