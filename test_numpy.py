import numpy as np

# 建立一個 1D numpy array
array_1d = np.array([1, 2, 3, 4, 5])

# 建立一個 2D numpy array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 基本數學運算
array_sum = np.sum(array_1d)  # 計算陣列元素總和
array_mean = np.mean(array_1d)  # 計算平均值
array_max = np.max(array_1d)  # 最大值
array_min = np.min(array_1d)  # 最小值

# 生成範圍數組
range_array = np.arange(0, 10, 2)  # 建立一個從0到10，間隔為2的數組

# 隨機生成數組
random_array = np.random.random((3, 3))  # 生成3x3隨機數組

# 矩陣乘法
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix_a, matrix_b)  # 矩陣相乘

# 顯示結果
print("1D Array:", array_1d)
print("2D Array:\n", array_2d)
print("Sum:", array_sum)
print("Mean:", array_mean)
print("Max:", array_max)
print("Min:", array_min)
print("Range Array:", range_array)
print("Random Array:\n", random_array)
print("Matrix Product:\n", matrix_product)
