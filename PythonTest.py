import time
class bench_cython:
    def fib(n):
        a, b = 0.0, 1.0
        for i in range(n):
            a, b = a + b, a
            print (a)

    def integrate_f(a, b, N):
        s = 0
        dx = (b - a) / N
        for i in range(N):
            s += (a + i * dx) ** 2 - (a + i * dx)
        return s * dx
    def compare(n, a, b, N):
        start = time.time()
        bench_cython.fib(n)
        end = time.time()
        py_timefib = end - start
        start = time.time()
        bench_cython.integrate_f(a, b, N)
        end = time.time()
        py_timeint = end - start
        print("Python time fib = {}".format(py_timefib))
        print("Python time integrate = {}".format(py_timeint))
        start = time.time()
        CythonTest.cfib(n)
        end = time.time()
        cy_timefib = end - start
        print("Cython time fib = {}".format(cy_timefib))
        start = time.time()
        CythonTest.cintegrate_f(a, b, N)
        end = time.time()
        cy_timeint = end - start
        print("Cython time integrate = {}".format(cy_timeint))
        print("Speedup fib = {}".format(py_timefib / cy_timefib))
        print("Speedup integrate = {}".format(py_timeint / cy_timeint))
