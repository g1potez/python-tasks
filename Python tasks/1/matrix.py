import numpy as np

with open('matrix.txt', 'r') as f:
    l = [[int(num) for num in line.split(',')] for line in f]

matrix = np.array(l)
trans = matrix.transpose()
print(matrix)
print(trans)