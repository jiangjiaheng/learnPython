# list
# fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
# print(fruits.count("apple"))
# print(fruits.count("tangerine"))
# print(fruits.index("banana"))
# print(fruits.index("banana", 4))

# fruits.reverse()

# print(fruits)

# fruits.append("grape")

# print(fruits)

# fruits.sort()

# print(fruits)

# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)

# from collections import deque

# queue = deque(["Eric", "John", "Micheal"])
# queue.append("Terry")
# queue.append("Graham")
# queue.popleft()
# queue.popleft()
# print(queue)

# squares = []
# for x in range(10):
#     squares.append(x**2)

# print(squares)

# squares2 = list(map(lambda x: x**2, range(10)))

# squares3 = [x**2 for x in range(10)]

# print(squares2)
# print(squares3)

# squares = [(x, y) for x in [1, 2, 3] for y in [4, 1, 6] if x != y]
# print(squares)

# vec = [-4, -2, 0, 2, 4]
# [x * 2 for x in vec]
# [x for x in vec if x >= 0]
# [abs(x) for x in vec]

# fruit = [" bannana ", " sadfasd", "passion fruit  "]
# [weapon.strip() for weapon in fruit]
# [(x, x**2) for x in range(6)]

# from math import pi

# [str(round(pi, i) for i in range(1, 6))]

# del
# a = [-1.1, 234, 234, 565, 7876]
# del a[0]
# print(a)
# del a[2:4]
# print(a)
# del a[:]
# print(a)

# ()
# t = 123, 456, "hello"
# print(t)
# print(t[0])
# u = t, (1, 2, 3, 4, 5)
# print(u)
# v = ([1, 2, 3], [4, 5, 6])
# print(v)
# empty = ()
# singleone = ("hello",)
# print(singleone)
# x, y, z = t

# {}
# basket = {"apple", "orange", "apple", "pear"}
# print(basket)
# print("orange" in basket)

# a = set("asdlkfjsdkj")
# b = set("dsafdsafdsf")
# print(a)
# print(a - b)
# print({x for x in a if x not in "abc"})

# {key:value}
# tel = {"jack": 123, "sape": "dsafds"}
# tel["guido"] = 123213
# print(tel)
# del tel["sape"]
# print(list(tel))
# print("guido" in tel)

# print(dict([("a", 123), ("b", 456)]))
# print({x: x**2 for x in (2, 4, 5)})
# print(dict(a=123, b=456))

# for
knights = {"gallahad": "the pure", "robin": "the brave"}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(["tic", "tac", "toe"]):
    print(i, v)

questions = ["name", "quest", "favorite color"]
answers = ["lancelot", "the holy grail", "blue"]
for q, a in zip(questions, answers):
    print("what is your {0}? It is {1}.".format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)

basket = ["apple", "orange", "apple", "pear", "banana"]
for f in sorted(set(basket)):
    print(f)
