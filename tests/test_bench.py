import unittest
from PythonTest import bench_cython
class Testbench_cython(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(bench_cython.fib(1), None)
    def test_integrate_f(self):
        self.assertEqual(bench_cython.integrate_f(6, 10, 2), 172.0)
        self.assertEqual(bench_cython.integrate_f(4, 23, 5), 2884.96)
        self.assertEqual(bench_cython.integrate_f(15, 42, 4), 17903.53125)

if __name__ == '__main__':
    unittest.main()