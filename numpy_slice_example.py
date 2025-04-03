import numpy as np

arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
arr2 = np.array([
    [2, 4, 5],
    [1, 3, 6],
    [7, 8, 9]
])

result = np.dot(arr1, arr2)
print("arr1:")
print(arr1)
print("arr2:")
print(arr2)
print("Result of dot product:")
print(result)