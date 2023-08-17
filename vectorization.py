import time
import numpy as np

def timeit():
    """
    a utitlity decorator to time running time
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            print(f"running time: {end - start} sec")
            return end - start
        return wrapper
    return decorator


@timeit()
def test():
    time.sleep(1)


@timeit()
def add_iteratively(n):
    sum = 0
    for i in range(n+1):
        sum += i
    print(sum)


@timeit()
def add_vectorize(n):
    """
    add number upto n
    """
    
    sum = np.sum(np.arange(n+1))
    print(sum)


@timeit()
def add_mul_itervatively(v,w, b):
    out = np.zeros(len(v))

    for i in range(len(v)):
        out[i] = v[i] * w[i] + b


@timeit()
def add_mul_vector(v, w, b):
     v * w * b
if __name__ == "__main__":
    n = 10000
    a0 = add_iteratively(n)
    a1 = add_vectorize(n)

    print(f"A magnitude of { a0 / a1 } difference")