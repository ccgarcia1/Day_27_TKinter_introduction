#unlimited positional arguments *args
#unlimited arguments are nothing but tuples
def add(*args):
    sum = 0
    print(args[3])
    for n in args:
        sum += n
        #print(n)
    return(sum)

#print(add(3, 5, 8, 10, 22))


#**kwargs many keyworded Arguments
#keyword arguments are nothing but dictionaries
def calculate(n, **kwargs):
    #print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    #print(kwargs["add"])
calculate(3, add=3, multiply=5)


#example of a class using **kwargs

class Car:

    def __init__(self, **kw):
        self.make = kw["make"] #if initialize like that and the user doesn't pass the argument
                               #there will be an error
        self.model = kw.get("model") #if initialize like that there is no error if
                                    #the user doesn't put the argument


my_car = Car(make="Honda")

print(my_car.model)

