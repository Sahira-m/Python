import time
import timeit


def main_func(name="one"):
    print("This is a main function")

    def sub_func1():
        print("/t first sub function")

    def sub_func2():
        print("/t second sub function")

    if name == "one":
        return sub_func1
    else:
        return sub_func2


start_time = time.time()
functionAssignment = main_func(name="one")
functionAssignment()
end_time = time.time()
# calculate how much time used to execute this function
time_spend = end_time - start_time
print("Times consumed is", time_spend)

# FUNCTION DECORATOR eXAMPLE
print("FUNCTION DECORATOR EXAMPLE")


def new_decorator(original_func):
    def wrap_func():
        print("some code before decorate function")
        original_func()
        print("some code after decorate function")

    return wrap_func


def arg_func():
    print("This is a argument function")


decorator1 = new_decorator(arg_func)
print("\t \t call decorator")
decorator1()

print("\n\n\t ORGINAL APPLYING DECORATOR")


# ORGINAL APPLYING DECORATOR
@new_decorator
def newfunc():
    print("This is a ORGINAL APPLYING DECORATOR")


start_time = time.time()
newfunc()
end_time = time.time()
# calculate how much time used to execute this function
time_spend = end_time - start_time
print("Times consumed for decorator function  is", time_spend)


def func_square():
    for i in range(10):
        print("squrae of the number is", i**2)


start_time = time.time()
func_square()
end_time = time.time()
# calculate how much time used to execute this function
time_spend = end_time - start_time
print("Times consumed for square function  is", time_spend)

setup = """
def func_one(n):
    return [str(num) for num in range(n)]
"""
stmt = "func_one(100)"
print("Time consumed in timeit", timeit.timeit(stmt, setup, number=100), "Micro second")
