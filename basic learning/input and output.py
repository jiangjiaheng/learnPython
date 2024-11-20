# year = 2016
# event = "Referendum"
# print(f"Result of the {year} {event}")

# yes_votes = 42_572_654
# total_votes = 85_705_149
# percentage = yes_votes / total_votes
# print("{:-9} Yes votes {:2.2%}".format(yes_votes, percentage))

# s = "hello,world"
# print(str(s))
# print(repr(s))
# print(str(1 / 7))

# x = 10 * 3.25
# y = 200**2
# z = "the value of z is " + repr(x) + ", and y is " + repr(y) + "..."
# print(z)

# hello = "hello world\n"
# hellos = repr(hello)
# print(hello)
# print(hellos)

# print(repr((x, y, ("spam", "eggs"))))

# import math

# print(f"the value of pi is approximately {math.pi:3f}.")

# table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 7678}
# for name, phone in table.items():
#     print(f"{name:10}===>{phone:10d}")

# animals = "eels"
# print(f"My hovercraft is full of {animals}.")
# print(f"My hovercraft is full of {animals!r}")

# bugs = "roaches"
# count = 13
# area = "living room"
# print(f"Debugging {bugs=} {count=} {area=}")

print("we are the {} who say {}".format("knights", "Ni"))

print("{0} and {1}".format("spam", "eggs"))
print("{1} and {0}".format("spam", "eggs"))

print("This {food} is {adjective}".format(food="spam", adjective="absolutely horrible"))

table = {"a": 123, "b": 456, "c": 789}

print("c:{0[c]:d}; b:{0[b]:d}; a:{0[a]:d}".format(table))
print("c:{c:d}; b:{b:d}; a:{a:d}".format(**table))

for x in range(1, 11):
    print("{0:2d} {1:3d} {2:4d}".format(x, x**2, x**3))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x**2).rjust(3), end="")
    print(repr(x**3).rjust(4))

print("12".zfill(5))
print("-3.14".zfill(7))
print("3.13213123123".zfill(5))

import math

print("the value of pi is approximately %5.3f" % math.pi)
