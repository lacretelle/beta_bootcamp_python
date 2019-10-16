def log(func):
    def wrapper(*args, **kwargs):
        print(func)
        if func.count:
            print(func.count)
        if func.index:
            print(func.index)
        with open('machine.log', 'w') as f:
            f.write(func.__name__)
        return func(*args, **kwargs)
    return wrapper
