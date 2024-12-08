# import os

# print("os get cwd: ", os.getcwd())

# os.system("mkdir today")

# print(dir(os))
# print(help(os))

# import glob

# print(glob.glob("*.py"))

# import sys

# print(sys.argv)

# sys.stderr.write("Warning, log file not found starting a new one")

# import re

# print(re.findall(r"\bf[a-z]*", "Which foot or hand fell fastest"))

# print(re.sub(r"(\b[a-z]+) \1", r"\1", "cat in the hat"))

# import math

# print(math.cos(math.pi / 4))
# print(math.log(1024, 2))

# import random

# print(random.choice(["a", "b", "c"]))
# print(random.sample(range(100), 10))
# print(random.random())
# print(random.randrange(6))

# import statistics

# data = [2.123, 123, 56, 890.9, 100]

# print(statistics.mean(data))
# print(statistics.median(data))
# print(statistics.variance(data))

# from urllib.request import urlopen
# with urlopen('') as response:
#     for line in response:
#         line=line.decode()
#         if line.startswith('datetime'):
#             print(line.rstrip())

# from datetime import date

# now = date.today()
# print(now)

# birthday = date(1994, 2, 28)
# age = now - birthday
# print(age.days)

# import zlib

# s = b"witch which has which witches wrist watch"
# print(len(s))
# t = zlib.compress(s)
# print(len(t))
# y = zlib.decompress(t)
# print(y)
# print(zlib.crc32(s))
