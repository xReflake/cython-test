def c_fib(int n):
   cdef int i
   cdef double a=0.0, b=1.0
   for i in range(n):
      a, b = a + b, a
   print (a)

cdef double f(double x):
    return x**2-x

def c_integrate_f(double a, double b, int N):
    cdef int i
    cdef double s, x, dx
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx
