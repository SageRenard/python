import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()          
        result = func(*args, **kwargs)    
        end_time = time.time()            
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time} секунд")
        return result                    
    return wrapper
def validate_args(func):
    def wrapper(*args):
        if len(args) < 1:
            return "Not enough arguments"
        elif len(args) > 1:
            return "Too many arguments"

        arg = args[0]

        if not isinstance(arg, int):
            return "Wrong types"

        if arg < 0:
            return "Negative argument"

        return func(*args)

    return wrapper

def memoize(func):
    cache = {}

    def wrapper(*args):

        if args in cache:
            return cache[args]

        result = func(*args)
        cache[args] = result
        return result

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__

    return wrapper



@timer
@memoize
@validate_args
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fib_without_memoize = timer(fibonacci)
print('Фибоначчи без memoize с аргументом 35: ', fib_without_memoize(35))

fibonacci = memoize(fibonacci)
fib_with_memoize = timer(fibonacci)
print('Фибоначчи с memoize и аргументом 35: ', fib_with_memoize(35))
