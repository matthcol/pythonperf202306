# Concurrency
- multi processing: isolation RAM
(RAM shared by creating a segment)
- multi threading: RAM shared (global, heap), 1 stack by thread

- async: "idem as threads"
Exemple: fastapi (https://fastapi.tiangolo.com/async/)

Warning: creating process or thread can be 'contreproductif'
without a good scheduler

- Scheduler: ThreadPoolExecutor, ProcessPoolExecutor
