from collections import namedtuple
Price = namedtuple("Price",["Laptop","Desktop","Phone"])
p = Price(2344,4566,6543)
print(p)
print(p.Laptop)

