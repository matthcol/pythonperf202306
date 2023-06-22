from concurrent.futures import ThreadPoolExecutor
from time import sleep

def f(x):
    res = 2*x**2 + 1
    sleep(3)
    print(f"f({x}) = {res}")

def run():
    pool = ThreadPoolExecutor()
    print(pool._max_workers)
    pool.shutdown() # wait for all tasks to be finished

    with ThreadPoolExecutor(max_workers=4) as pool:
        # call pool.__enter__ entering in the with section
        print(pool._max_workers)
        for i in range(16):
            pool.submit(f, i)
    # => pool.__exit__ => pool.shutdown()

if __name__ == '__main__':
    run()