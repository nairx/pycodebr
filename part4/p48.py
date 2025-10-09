# def add(*args):
#     print(sum(args))
# add(4,5,3,8)

# def add(**kwargs):
#     print(sum(kwargs.values()))
# add(a=2,b=3,c=5)


def add(*args,**kwargs):
    print(sum(args)+sum(kwargs.values()))
    # print(sum(kwargs.values()))
add(4,7,3,2,a=2,b=3,c=5)
