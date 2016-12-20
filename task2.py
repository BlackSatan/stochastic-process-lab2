import random

N = 999
randomParam = [random.random() for _ in range(1, N)]
countUp = 0
for i in range(0, N - 2):
    if randomParam[i + 1] - randomParam[i] > 0:
        countUp += 1
print countUp, N - countUp