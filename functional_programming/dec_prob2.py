def usercheck(f):
    def wrapper(a,b):
        if a=="admin":
            return f(a,b)
        else:
            return Exception("not authorized")
    return wrapper
@usercheck
def changepin(username,newpin):
    pin=newpin
    return "pin changed"
print(changepin("anu",5241))
print(changepin("admin",5241))