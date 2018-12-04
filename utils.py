from random import randint

print("===== List comprehensions =====")
# list comprehensions
# get random integers
print([randint(0,50) for _ in range(10)])
print([x * x for x in range(10) if not x % 2])

print("\n")
print("===== Dictionaries, collections =====")
# dictionaries as switch/case
def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()

print(dispatch_dict('add', 4, 6))

# collections.Counter lets you find the most common
# elements in an iterable:
import collections

c = collections.Counter('python_experience')

print(c.most_common(3))

print("\n")
print("===== Class Methods =====")
class PyClass:
    data = 100
    def method(self):
        print("Instance method called", self.data)
    
    @classmethod
    def class_method(cls):
        print("Class method called", cls.data)

    @staticmethod
    def static_method():
        print("Static method called")

obj = PyClass()
obj.method()
obj.class_method()
obj.static_method()

print("\n")
print("===== Lambda functions =====")
# lambda functions 

multiply = lambda x, y: x * y

print(multiply(10,20))

print((lambda x, y: x // y)(400,2))

print("\n")
print("===== Inner functions =====")

def parent():
    print("Inside parent")

    def first_child():
        print("Inside first child")

        def second_child():
            print("Inside second child")

        second_child()
        
    first_child()
    
parent()
        