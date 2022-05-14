

def main_fuc(another_function):

    def wrapper():
        print("wrap head")
        another_function()
        print("wrap tail")

    return wrapper


def func_need_wrapper():
    print("this is the main finction")


wrapped_func = main_fuc(func_need_wrapper)

wrapped_func()
