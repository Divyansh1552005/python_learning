# decorator to print the function name and the value of its arguments everytime the function is called


def deco(func):
    def wrapper(*args):
        res = func(*args)
        func_name = func.__name__
        args_val = ', '.join(str(arg) for arg in args)

        print(f"The name of the function is {func_name} and the value of its arguments is : {args_val}")
        return func(*args)

    return  wrapper

@deco
def func(a,b):
    return a+b

func(3,4)