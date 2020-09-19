from functools import reduce

def counter(fn):
    '''
    x = checks chars limit and it is free variable
    returns True or False
    '''
    x = 50
    def inner():
        nonlocal x
        if len(fn.__doc__) > x:
            return True
        else:
            return False
    return inner

def fib(initial_value = 0):
    '''
    intial_value = 0, acts as cnt intializer
    fib_series = creates a series of fib series considered first 100 fib nums
    returns the next incremented index of fib series
    '''
    fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
    series = fib_series(100)
    def fib_loop(increment = 1):
        nonlocal fib_series, initial_value
        initial_value += increment
        return series[initial_value]
    return fib_loop

def closure_counts(fn):
    '''
    fn -> function name add, mul, div
    cnt intialize the cnount to 0.
    returns dictionary for all func name with counter.
    '''
    cnt = 0
    global dict1 
    dict1 = {}
    def inner(*args, **kwargs):
        nonlocal cnt
        if fn.__name__ == 'add':
            cnt += 1
            dict1['add'] = cnt
        elif fn.__name__ == 'mul':
            cnt += 1
            dict1['mul'] = cnt
        elif fn.__name__ == 'div':
            cnt += 1
            dict1['div'] = cnt
        return dict1
    return inner

def closure_counts_dict(fn, my_dict):
    '''
    fn -> function name add, mul, div
    my_dict -> param dict
    return -> dict for each method names div, mul, add
    '''
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        if fn.__name__ == 'add':
            cnt += 1
            my_dict['add'] = cnt
        elif fn.__name__ == 'mul':
            cnt += 1
            my_dict['mul'] = cnt
        elif fn.__name__ == 'div':
            cnt += 1
            my_dict['div'] = cnt
        return my_dict
    return inner