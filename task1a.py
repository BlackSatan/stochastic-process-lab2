import random
import math
import matplotlib.pyplot as plt
import numpy as np

ITERATION_COUNT = 100
firstRandomParam = [random.random() for _ in xrange(ITERATION_COUNT)]
secondRandomParam = [random.random() for _ in xrange(ITERATION_COUNT)]
firstProcessList = []
secondProcessList = []
for i in xrange(ITERATION_COUNT):
    firstPart = math.sqrt((-2 * math.log(firstRandomParam[i])))
    trigonometricFunctionArg = 2 * math.pi * secondRandomParam[i]
    firstProcessList.append(firstPart * math.cos(trigonometricFunctionArg))
    secondProcessList.append(firstPart * math.sin(trigonometricFunctionArg))
processList = firstProcessList + secondProcessList
minValue = min(processList)
maxValue = max(processList)
R = maxValue - minValue
K = 9.0
n = R / K
H = 0
processList.sort()
for i in range(0, int(K) - 1):
    A = n * i + minValue
    B = A + n
    x = abs(B - A) / 2
    t = (1 / math.sqrt(2 * math.pi)) * math.exp(-pow(x, 2) / 2)
    if B == maxValue:
        S = len([val for val in processList if A <= val <= B])
    else:
        S = len([val for val in processList if A <= val < B])
    H += ((S / (ITERATION_COUNT*2 - t)) ** 2) / t
print H
f, (ax1, ax2) = plt.subplots(2)
x = np.arange(0, 1, .02)
ax1.plot(firstRandomParam, firstProcessList, 'r--')
ax2.plot(secondRandomParam, secondProcessList, 'r--')

plt.show()