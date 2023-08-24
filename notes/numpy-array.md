```python
my_list = [1,2,3]
```


```python
import numpy as np
```


```python
arr = np.array(my_list)
```


```python
arr
```




    array([1, 2, 3])




```python
my_mat = [[1,2,3],[4,5,6],[7,8,9]]
```


```python
np.array(my_mat) # Convert single line array to matrix
```




    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])




```python
np.arange(0,11,2) # Generate the event number array with size
```




    array([ 0,  2,  4,  6,  8, 10])




```python
np.zeros((3,3)) # Generate 3x3 Matrix for zeros
```




    array([[0., 0., 0.],
           [0., 0., 0.],
           [0., 0., 0.]])




```python
np.ones(4) # Generate 4 ones array
```




    array([1., 1., 1., 1.])




```python
np.linspace(0,5,100) # Generate array with 100 item between value 0 to 5
```




    array([0.        , 0.05050505, 0.1010101 , 0.15151515, 0.2020202 ,
           0.25252525, 0.3030303 , 0.35353535, 0.4040404 , 0.45454545,
           0.50505051, 0.55555556, 0.60606061, 0.65656566, 0.70707071,
           0.75757576, 0.80808081, 0.85858586, 0.90909091, 0.95959596,
           1.01010101, 1.06060606, 1.11111111, 1.16161616, 1.21212121,
           1.26262626, 1.31313131, 1.36363636, 1.41414141, 1.46464646,
           1.51515152, 1.56565657, 1.61616162, 1.66666667, 1.71717172,
           1.76767677, 1.81818182, 1.86868687, 1.91919192, 1.96969697,
           2.02020202, 2.07070707, 2.12121212, 2.17171717, 2.22222222,
           2.27272727, 2.32323232, 2.37373737, 2.42424242, 2.47474747,
           2.52525253, 2.57575758, 2.62626263, 2.67676768, 2.72727273,
           2.77777778, 2.82828283, 2.87878788, 2.92929293, 2.97979798,
           3.03030303, 3.08080808, 3.13131313, 3.18181818, 3.23232323,
           3.28282828, 3.33333333, 3.38383838, 3.43434343, 3.48484848,
           3.53535354, 3.58585859, 3.63636364, 3.68686869, 3.73737374,
           3.78787879, 3.83838384, 3.88888889, 3.93939394, 3.98989899,
           4.04040404, 4.09090909, 4.14141414, 4.19191919, 4.24242424,
           4.29292929, 4.34343434, 4.39393939, 4.44444444, 4.49494949,
           4.54545455, 4.5959596 , 4.64646465, 4.6969697 , 4.74747475,
           4.7979798 , 4.84848485, 4.8989899 , 4.94949495, 5.        ])




```python
np.eye(4) # Generateb 4x4 Matrix of 0 and 1
```




    array([[1., 0., 0., 0.],
           [0., 1., 0., 0.],
           [0., 0., 1., 0.],
           [0., 0., 0., 1.]])




```python
np.ones((3,4)) # Generate all ones 3x4 matrix
```




    array([[1., 1., 1., 1.],
           [1., 1., 1., 1.],
           [1., 1., 1., 1.]])




```python
np.random.rand(5) # Generate 5 random values 
```




    array([0.43149786, 0.97547358, 0.94947786, 0.85319884, 0.7575099 ])




```python
np.random.rand(5,5) # Generate 5x5 Random matrix 
```




    array([[0.34376204, 0.56081635, 0.82025671, 0.16167618, 0.70917511],
           [0.00907192, 0.54843282, 0.54593378, 0.66658696, 0.78558745],
           [0.28127318, 0.08920067, 0.2072205 , 0.4439081 , 0.56569263],
           [0.10922138, 0.86157718, 0.94250474, 0.91693962, 0.62264798],
           [0.57109036, 0.27659487, 0.34065093, 0.05566971, 0.38304917]])




```python
np.random.randn(2) # Generate 2 random value array
```




    array([-0.4576278 ,  1.15481282])




```python
np.random.randn(4,4) # Generate 4x4 Matrix from the random values
```




    array([[-1.34675024,  1.09530033, -0.75191013,  0.19385645],
           [ 0.63220178,  0.24775647,  1.87312177, -0.38173341],
           [ 0.61951403, -1.14866941,  2.20954979,  0.02427298],
           [-0.80061995,  1.20301866,  0.17525841,  1.05495789]])




```python
np.random.randint(1,20) # Generate Random value from 1 to 20
```




    5




```python
arr = np.arange(25) # Generate the 25 digit sequence array
arr
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19, 20, 21, 22, 23, 24])




```python
randarr = np.random.randint(0,50,10) # Generate 10 integer array using random method
```


```python
randarr
```




    array([47, 43, 18, 39,  2, 29,  4, 25, 24, 29])




```python
arr.reshape(5,5) # Convert Simple array to 5x5 Matrix
```




    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14],
           [15, 16, 17, 18, 19],
           [20, 21, 22, 23, 24]])




```python
randarr
```




    array([47, 43, 18, 39,  2, 29,  4, 25, 24, 29])




```python
randarr.max() # Return Max Value From Array
```




    47




```python
randarr.min() # Return Min Value From Array
```




    2




```python
randarr.argmax() # Return Max Value Index Location
```




    0




```python
randarr.argmin() # Return Min Value Index Location
```




    4




```python
arr.shape # Return size of array matrix
```




    (25,)




```python
arr = arr.reshape(5,5) # Reshape the array in 5x5 matrix
```


```python
arr.shape
```




    (5, 5)




```python
arr.dtype # Return the array data type
```




    dtype('int64')




```python
from numpy.random import randint
```


```python
randint(2,10,5)
```




    array([6, 3, 7, 5, 8])
