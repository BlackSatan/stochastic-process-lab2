import random
import math
import matplotlib.pyplot as plt
import numpy as np

N = 48
ITERATION_COUNT = 1000
valueList = []
sqrt = math.sqrt(12.0 / N)
for i in range(1, ITERATION_COUNT):
    randomParam = [random.random() for _ in range(1, N)]
    valueList.append(0)
    for ii in range(1, N):
        valueList[i - 1] += randomParam[ii - 1] - 0.5
    print
    valueList[i - 1] *= sqrt

# maxValue = max(valueList)
# minValue = min(valueList)
# R = maxValue - minValue
# K = 9.0
# n = R / K
# H = 0
# valueList.sort()
# for i in range(0, int(K) - 1):
#     A = n * i + minValue
#     B = A + n
#     x = abs(B - A) / 2
#     t = (1 / math.sqrt(2 * math.pi)) * math.exp(-pow(x, 2) / 2)
#     if B == maxValue:
#         S = len([val for val in valueList if A <= val <= B])
#     else:
#         S = len([val for val in valueList if A <= val < B])
#     H += ((S / (ITERATION_COUNT - t)) ** 2) / t
# print H, valueList
print valueList
f, ax1 = plt.subplots()
ax1.hist(valueList)

plt.show()