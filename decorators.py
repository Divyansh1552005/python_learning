import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' ran in {end - start:.5f} seconds")
        return res
    return wrapper

@timer
def omago(fk):
    print("awfcs", fk)
    time.sleep(1.5)
    print("Done!")

omago("divyansh")
