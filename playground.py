#unlimited positional arguments
def add(*args):
    sum = 0
    print(args[3])
    for n in args:
        sum += n
        #print(n)
    return(sum)

print(add(3, 5, 8, 10, 22))