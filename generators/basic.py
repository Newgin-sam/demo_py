# cube without generators

def create_cube(n):
    results = []
    for x in range(n):
        results.append(x**3)
    return results


# for x in create_cube(10):
#     print(x)


# cube with generators

def generator_create_cube(n):

    for x in range(n):
        yield x**3


# for x in generator_create_cube(5):
#     print(x)


# fibanocai with generators

def fib(n):
    a, b = 1, 2
    for i in range(n):
        yield a
        a, b = b, a+b


# for i in fib(5):
#     print(i)

# iter()

s = "hello"

S_iter = iter(s)

print(next(S_iter))
