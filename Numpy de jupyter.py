import numpy as np
a_py = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a_np = np.array(a_py)
print(a_py[3:7:2], a_np[3:7:2])
print(a_py[2:-1:2], a_np[2:-1:2])
print(a_py[::-1], a_np[::-1])
idx = np.array([7,2])
a_np[idx]
# a_py[idx]
#Which allows convenient querying, reindexing and even sorting
ages = np.random.randint(low=30, high=60, size=10)
heights = np.random.randint(low=150, high=210, size=10)
print(ages)
print(heights)
print(ages < 50)
print(heights[ages < 50])
print(ages[ages < 50])
shuffled_idx = np.random.permutation(10)
print(shuffled_idx)
print(ages[shuffled_idx])
print(heights[shuffled_idx])
sorted_idx = np.argsort(ages)
print(sorted_idx)
print(ages[sorted_idx])
print(heights[sorted_idx])
#BRODCASTING
a = np.array([4, 5, 6])
b = np.array([2, 2, 2])
a * b
a = np.array([4, 5, 6])
b = 2
a * b
a = np.arange(10).reshape(1,10)
b = np.arange(12).reshape(12,1)
print(a)
print(b)
print(a*b)
