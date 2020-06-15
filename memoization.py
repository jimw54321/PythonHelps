from functools import lru_cache

# memoization: will reuse previously called function with the value
# of those param(s) instead of a fresh call to the function
@lru_cache
def expensive_func(params):
    some interesting code
    return value
