from time import perf_counter as time_perf_counter
from functools import wraps as fnct_wraps

def timer(func):
    @fnct_wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time_perf_counter()
        result = func(*args, **kwargs)
        end_time = time_perf_counter()
        
        elapsed_time = end_time - start_time
        print(f"Time: {elapsed_time:.6f} seconds")
        
        return result
    return wrapper
