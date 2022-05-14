def main_fuc(another_function):

    def wrapper():
        print("wrap head")
        another_function()
        print("wrap tail")

    return wrapper


@main_fuc
def func_need_wrapper():
    print("this is the main finction")


func_need_wrapper()
