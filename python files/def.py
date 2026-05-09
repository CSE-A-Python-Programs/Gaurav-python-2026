def change(func):
    def myinner():
        return func().upper()
    return myinner

@change
def myfunc():
    return "hello"

print(myfunc())