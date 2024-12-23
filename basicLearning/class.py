# def scope_test():
#     def do_local():
#         spm = "local spam"

#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"

#     def do_global():
#         global spam
#         spam = "global spam"

#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)


# scope_test()
# print("In global scope:", spam)


# class MyClass:
#     i = 123

#     def f(self):
#         return "hello world"


# x = MyClass()

# print(x.i, x.f())


# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart


# x = Complex(3, -4)

# print(x.r, x.i)

# x.counter = 1
# while x.counter < 10:
#     x.counter = x.counter * 2
# print(x.counter)


# class Dog:
#     kind = "canine"

#     def __init__(self, name):
#         self.name = name
#         self.tricks = []

#     def add_trick(self, trick):
#         self.tricks.append(trick)


# d = Dog("Fido")
# e = Dog("Buddy")
# d.add_trick("roll over")
# e.add_trick("play dead")

# print(d.kind, e.kind)
# print(d.name, e.name)
# print(d.tricks, e.tricks)


# class Warehouse:
#     purpose = "storage"
#     region = "west"


# w1 = Warehouse()
# print(w1.purpose, w1.region)
# w2 = Warehouse()
# w2.region = "east"
# print(w2.purpose, w2.region)


# def f1(self, x, y):
#     return min(x, x + y)


# class C:
#     f = f1

#     def g(self):
#         return "hello world"

#     h = g


# c = C()

# print(c.f(1, 2), c.h())


# class Bag:
#     def __init__(self):
#         self.data = []

#     def add(self, x):
#         self.data.append(x)

#     def addtwice(self, x):
#         self.add(x)
#         self.add(x)


# b = Bag()

# b.add("clothes")
# b.addtwice("pants")
# print(b.data)


# class Mapping:
#     def __init__(self, iterable):
#         self.item_list = []
#         self.__update(iterable)

#     def update(self, iterable):
#         for item in iterable:
#             self.item_list.append(item)

#     __update = update


# class MappingSubclass(Mapping):
#     def update(self, keys, values):
#         for item in zip(keys, values):
#             self.item_list.append(item)


# map1 = Mapping([1, 2, 3])
# print(map1.item_list)

# map11 = Mapping({"a": 1, "b": 2})
# print(map11.item_list)

# map2 = MappingSubclass({"a": 1, "b": 2})
# print(map2.item_list)

# map3 = MappingSubclass([1, 2, 3])
# print(map3.item_list)

# map4 = MappingSubclass(["a", "b", "c"])
# print(map4.item_list)

# for item in {"a": 1, "b": 2}:
#     print(item)

# from dataclasses import dataclass

# @dataclass
# class Employee:
#     name: str
#     dept: str
#     salary: int


# john = Employee("john", "computer lab", 1000)

# print(john)

# s = "abc"
# it = iter(s)
# print(next(it))
# print(next(it))
# print(next(it))


# class Reverse:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]


# rev = Reverse("abcd")
# iter(rev)
# for char in rev:
#     print(char)


# def reverse(data):
#     for index in range(len(data) - 1, -1, -1):
#         yield data[index]


# for char in reverse("abcd"):
#     print(char)

print(sum(i * i for i in range(10)))

a = [10, 20, 30]
b = [7, 5, 3]
print(sum(x * y for x, y in zip(a, b)))


class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa


graduates = [
    Student("zhangsan", 100),
    Student("lisi", 90),
    Student("landscape", 60),
]

maxP = max((student.name, student.gpa) for student in graduates)
minP = min((student.name, student.gpa) for student in graduates)

print(maxP, minP)

data = "abcd"
print(list(data[i] for i in range(len(data) - 1, -1, -1)))
