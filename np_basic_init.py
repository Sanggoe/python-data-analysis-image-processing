import numpy as np

list_data = [1, 2, 3]

# 기본적으로 List는 numpy의 array와 호환됨
array = np.array(list_data)

print(array.size)
print(array.dtype)
print(array[2])

# 0부터 3까지의 배열 만들기
array1 = np.arange(4)
print(array1)

# 0으로 초기화된 배열 만들기
array2 = np.zeros((4, 4), dtype=float)
print(array2)

# 1로 초기화된 배열 만들기
array3 = np.ones((3, 3), dtype=str)
print(array3)

# 0부터 9까지 랜덤 초기화 된 배열 만들기
array4 = np.random.randint(0, 10, (3, 3))
print(array4)

# 평균이 0이고, 표준 편차가 1인 표준 정규를 띄는 배열
array5 = np.random.normal(0, 1, (3, 3))
print(array5)