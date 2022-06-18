from collections import Counter
from collections import defaultdict
from collections import namedtuple

# counter

s = "aaasdf l;kj asdf iasdfkj asdf  aaasdf aaasdf aosdfuasd mvbcvkjher i"

counterofs = Counter(s)

print("counter", counterofs)

print(Counter(s.upper().split()))

print("list", list(counterofs))

print("set", set(counterofs))

print("dict", dict(counterofs))

print("most 2 common", counterofs.most_common(2))

print("values", counterofs.values())

print("______________________________________________________________________________________________________")


# defaultdict

d = {'a': 1}

# print(d['b'])  # this throws an error as b is no defined in dict


f = defaultdict(lambda: 0)

f['a'] = 10

print(f['b'])  # prints 0 as the values are defaulted

print("______________________________________________________________________________________________________")
# named tuple

tup = (3, 4, 5, 6, 7, 8, 8, 9)

print(tup[1])


Dog = namedtuple('dog', ['age', 'breed', 'name'])

ron = Dog(5, 'lab', 'ron')
print(type(ron))
print(ron)

print(ron[0], ron.name)
