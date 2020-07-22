# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from multiprocessing import current_process
from threading import current_thread
import time

def test_fun(sec):
    print('process will sleep {} sec'.format(sec))
    time.sleep(sec)
    return 'sleep done from {}'.format(current_thread().name)

# =============================================================================
# with ThreadPoolExecutor() as exe:
#     e_1 = exe.submit(test_fun, 5)
#     e_2 = exe.submit(test_fun, 4)
#     print(e_1.result())
#     print(e_2.result())
#     
# with ThreadPoolExecutor() as exe:
#     result = [exe.submit(test_fun, i) for i in range(5,0,-1)]
#     for i in as_completed(results):
#         print(r.result())
# =============================================================================

with ThreadPoolExecutor() as exe:
    results = exe.map(test_fun, [5,4,3,2,1])
    for r in results:
        print(r)