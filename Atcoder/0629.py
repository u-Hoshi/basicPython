# C102 B問題
s = int(input())
x = list(map(int, input().split()))
x.sort(reverse = True)
 
print(x[0]-x[s-1])

# C113 B問題
s = int(input())
x = list(map(int, input().split()))
y= list(map(int, input().split()))

import math

y=list(map(lambda a: x[0]-a*0.0006, y))

import numpy as np

def nearest(data, value):
    idx = np.argmin(np.abs(np.array(data) - value))
    return idx+1

print(nearest(y, x[0]))

