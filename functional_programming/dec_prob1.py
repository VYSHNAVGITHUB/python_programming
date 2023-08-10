def agecheck(func):
    def wrapper(name,age):
        if age>=18:
            return func(name,age)
        else:
            raise Exception("not eligible")
    return wrapper

@agecheck
def vaccine(name,age):
    return "vaccinated successfully"
print(vaccine("anu",13))
