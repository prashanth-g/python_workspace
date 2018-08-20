""" Find fib with iterative way """
def get_fib(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    first = 0
    second = 1
    i = 2
    next = first + second
    while i < position:
        first = second
        second = next
        next = first + second
        i += 1
    return next

def get_fib_recursive(position):
    if position <= 1:
        return position
    return get_fib_recursive(position-1) + get_fib_recursive(position-2)

#print(get_fib(8))
print(get_fib_recursive(2))