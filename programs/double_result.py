def double_result(func):
    def wrapper(a,b):
        print("before doubling...")
        sum=func(a,b)
        print("after doubling...")
        return sum
    return wrapper
@double_result
def add(a,b):
    return a+b
x=int(input("enter first number:"))
y=int(input("enter second number:"))
print("result:",2*add(x,y))
