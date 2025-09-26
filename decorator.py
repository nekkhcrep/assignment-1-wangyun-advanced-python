from functools import wraps
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} is running  ")
        result = func(*args, **kwargs)
        return result
    return wrapper

def repeat(n):
    def decorator_repeat(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


if __name__ == "__main__":
    @logger
    def hello():
        print("Привет")
    hello()

    @repeat(3)
    def hi():
        print("Hi!")
    hi()