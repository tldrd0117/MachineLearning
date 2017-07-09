# -*- coding: utf-8 -*-
import kNN
import matplotlib
import matplotlib.pyplot as plt
from numpy import array

group, labels = kNN.createDataSet()
print( group )
print( labels )

result = kNN.classify0([0,0], group, labels, 3)
print( result )

datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')
print( datingDataMat )
print( datingLabels )

fig = plt.figure()
ax = fig.add_subplot(111)
# 주당 아이스크림 소비량 y축, 비디오 게임으로 보내는 시간의 비율 x축
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
plt.show()


