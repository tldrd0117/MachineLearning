# -*- coding: utf-8 -*-
from numpy import *

#  랜덤 4x4 행렬
randMat = mat(random.rand(4, 4))
print(randMat)

# 랜덤 4x4 역행렬
invRandMat = randMat.I
print(invRandMat)

# 행렬 곱하기 역행렬
identifyMatrix = randMat * invRandMat
print(identifyMatrix)

# 단위 행렬 생성
myEye = eye(4)
print(myEye)


