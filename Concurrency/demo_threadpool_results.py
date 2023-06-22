from concurrent.futures import ThreadPoolExecutor
from time import sleep

import numpy as np

def f(x, delai):
    res = 2*x**2 + 1
    sleep(delai)
    # print(f"f({x}) = {res}")
    return res

def run_2_jobs():
    with ThreadPoolExecutor(max_workers=4) as pool:
        # call pool.__enter__ entering in the with section
        print("Workers:", pool._max_workers)
        futureRes1 = pool.submit(f, 4, 30)
        futureRes2 = pool.submit(f, 5, 6)
        for futureRes in futureRes1, futureRes2: 
            print("job:", futureRes, 
                "; cancelled = ", futureRes.cancelled(),
                "; done = ", futureRes.done(),
                "; running = ", futureRes.running()
            )
        # sleep(10)
        # for futureRes in futureRes1, futureRes2: 
        #      if futureRes.running():
        #           futureRes.cancel()
    # => pool.__exit__ => pool.shutdown()
    for futureRes in futureRes1, futureRes2: 
            print("job:", futureRes, 
                "; cancelled = ", futureRes.cancelled(),
                "; done = ", futureRes.done(),
                "; running = ", futureRes.running()
            )
            res = futureRes.result()
            print("Result:", res)

def run_n_jobs(w,n):
    """ run n tasks with w workers
    """
    values = np.random.normal(10, 4, n)
    with ThreadPoolExecutor(w) as pool:
        # submit n computations

        # retrieve n results
        results = None
    print(results)

if __name__ == '__main__':
    run_2_jobs()
    run_n_jobs(w=4, n=20)