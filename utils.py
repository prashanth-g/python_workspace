from random import randint

# list comprehensions
# get random integers
print([randint(0,50) for _ in range(10)])

print([x * x for x in range(10) if not x % 2])

# dictionaries as switch/case
def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()

print(dispatch_dict('add', 4, 6))
