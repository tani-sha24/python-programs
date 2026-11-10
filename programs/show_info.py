def show_info(func):
    def wrapper(num):
        print("Calling function..")
        result=func(num)
        print("Function executed..")
        return result
    return wrapper
@show_info
def square(num):
    return num*num
print(square(5))