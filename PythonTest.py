import time
class bench_cython:
    def fib(self, n):
        a, b = 0.0, 1.0
        for i in range(n):
            a, b = a + b, a
            print (a)

    def integrate_f(self, a, b, N):
        s = 0
        dx = (b - a) / N
        for i in range(N):
            s += (a + i * dx) ** 2 - (a + i * dx)
        return s * dx
