from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep
from datetime import datetime

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
        # NB: attention à la lazy evaluation !!!
        
        # 1st round
        # submit n computations
        futures = [ pool.submit(f, x, 1 + (i % 5)) for i, x in enumerate(values, start=1) ]
        print(futures)
        # retrieve n results (barrière de synchronisation)
        results = [ future.result() for future in futures ]
        print(results)

        # 2nd round
        results2 = np.empty(n) 
        futuresDict = { pool.submit(f, x, 5 - (i % 5)): i for i, x in enumerate(values) }
        for future in as_completed(futuresDict):
            indexFuture = futuresDict[future]
            res = future.result()
            print(f"Received result #{indexFuture}:", res)
            # todo another task on this task
            results2[indexFuture] = res
        print(results2)
if __name__ == '__main__':
    # run_2_jobs()
    t1 = datetime.now()
    run_n_jobs(w=4, n=8)
    t2 = datetime.now()
    print("Time elapsed:", t2-t1)