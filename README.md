# Cython and python testing
This program allows you to compare the performance of Cython and Python.
# Installing
pip install cython-test
# How to use
```python
import cython-test as ct
def test_fib(n):    #Function for comparing speed using Fibbonacci numbers.
def integrate_f(a, b, N):   #Function for comparing speed using function integration.
```
# Example
```python
import PythonTest as pt
import cython-test as ct
import time

a = int(input('enter a: '))
b = int(input('enter b: '))
N = int(input('enter N: '))

start = time.time()
ct.integrate_f(a, b, N)
end =  time.time()
cy_time = end - start
print("Cython time = {}".format(cy_time))

start = time.time()
pt.integrate_f(a, b, N)
end =  time.time()
py_time = end - start
print("Python time = {}".format(py_time))
print("Speedup = {}".format(py_time / cy_time))
```
