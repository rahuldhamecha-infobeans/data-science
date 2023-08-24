```python
import numpy as np
```


```python
arr = np.arange(0,11)
```


```python
arr
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])




```python
arr[8]
```




    8




```python
arr[1:5]
```




    array([1, 2, 3, 4])




```python
arr[0:5]
```




    array([0, 1, 2, 3, 4])




```python
arr[:6]
```




    array([0, 1, 2, 3, 4, 5])




```python
arr[5:]
```




    array([ 5,  6,  7,  8,  9, 10])




```python
arr[0:5] = 100
```


```python
arr
```




    array([100, 100, 100, 100, 100,   5,   6,   7,   8,   9,  10])




```python

```


```python
arr = np.arange(0,11)
```


```python
arr
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])




```python
slice_of_array = arr[0:6]
```


```python
slice_of_array
```




    array([0, 1, 2, 3, 4, 5])




```python
slice_of_array[:] = 99
```


```python
slice_of_array
```




    array([99, 99, 99, 99, 99, 99])




```python
arr_copy = arr.copy()
```


```python
arr_copy[:] = 100
```


```python
arr_copy
```




    array([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100])




```python
arr
```




    array([99, 99, 99, 99, 99, 99,  6,  7,  8,  9, 10])



### 2D Array


```python
arr_2d = np.array([[1,2,3],[4,5,6],[3,4,6]])
```


```python
arr_2d
```




    array([[1, 2, 3],
           [4, 5, 6],
           [3, 4, 6]])




```python
arr_2d[0,2]
```




    3




```python
arr_2d[:2,1:]
```




    array([[2, 3],
           [5, 6]])




```python
arr_2d[:2,:1]
```




    array([[1],
           [4]])




```python
arr_2d[2:,1:]
```




    array([[4, 6]])




```python
arr = np.arange(0,11)
```


```python
arr
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])




```python
bool_arr = arr > 6
```


```python
bool_arr
```




    array([False, False, False, False, False, False, False,  True,  True,
            True,  True])




```python
arr[bool_arr]
```




    array([ 7,  8,  9, 10])




```python
arr[arr<5]
```




    array([0, 1, 2, 3, 4])




```python
arr_2d = np.arange(50).reshape(5,10)
```


```python
arr_2d[1:3]
```




    array([[10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
           [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])




```python
arr_2d[1:3,2:6]
```




    array([[12, 13, 14, 15],
           [22, 23, 24, 25]])




```python

```
