# python-data-analysis-image-processing
python 언어를 이용한 데이터 분석 및 이미지 처리 연습

<br/>

## 행렬의 필요성

* 1차원 배열 : 벡터
* 2차원 배열 : 행렬
* 3차원 배열 : 텐서

<br/>

#### **행렬은 어디에 쓰일까?**

* 컴퓨터 메모리 구조, 표 형태의 데이터, 이미지는 행렬로 표현 가능하다.

<br/>

<br/>

<br/>

## 다양한 개발환경 소개

* Pycham : IDE
* CoLab : Jupyter 기반
* Repl.it

<br/>

<br/>

## Numpy

* 다차원 배열을 효과적으로 처리할 수 있도록 도와주는 라이브러리
* Python의 기본 List에 비해 빠르고 강력한 기능 제공

<br/>

### Numpy의 차원

* 1차원 축(행) : axis 0 => Vector
* 2차원 축(열) : axis 1 => Matrix
* 3차원 축(채널) : axis 2 => Tensor(3차원 이상)

<br/>

<br/>

## Numpy 기본 문법

```python
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
```

<br/>

**Numpy 배열 합치기**

[1, 2] + [3, 4] = [1, 2, 3, 4]

```python
import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.concatenate([array1, array2])

print(array3.shape)
print(array3)
print(type(array3))
```

<br/>

**Numpy 배열 형태 바꾸기**

```python
import numpy as np

array1 = np.array([1,2,3,4])
print(array1)

# 형태 바꾸기
array2 = array1.reshape((2,2))
print(array2)
```

<br/>

**Numpy 배열 세로 축으로 합치기**

```python
import numpy as np

array1 = np.arange(4).reshape((1, 4))
array2 = np.arange(8).reshape((2, 4))
print(array1)
print(array2)

# 세로로 합치기
array3 = np.concatenate([array1, array2], axis=0)
print(array3)
```

<br/>

**Numpy 배열 나누기**

```python
import numpy as np

array = np.arange(8).reshape(2, 4)
left, right = np.split(array, [2], axis=1)

print(left.shape)
print(right.shape)

print(array)
print(left)
print(right)
```

<br/>

<br/>

<br/>

<br/>

<br/>

<br/>

<br/>

<br/>
