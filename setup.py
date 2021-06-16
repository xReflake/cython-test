from setuptools import setup, find_packages

with open("C:\Packs\README.txt", 'r') as f:
    long_description = f.read()

setup(
    name='cython-test',
    version='1.0',
    author='xReflake',
    author_email='xreflake@mail.ru',
    description='python and cython testing',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/xReflake/cython-test',
    packages=find_packages(),
    license='MIT',
    test_suite='tests',
    python_requires='>=3.6'
)