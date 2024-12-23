# import reprlib

# reprTxt = reprlib.repr(set("dsafdsafsdafdsfsdafsdvlzxkjvlkz"))
# print(reprTxt)

# import pprint

# t = [[[["black", "cyan"], "white", ["green", "red"]], [["magenta", "yellow"], "blue"]]]

# ppTxt = pprint.pprint(t, width=30)
# print(ppTxt)

# import textwrap

# doc = """The wrap() method is just like fill() except that it returns
# a list of strings instead of one big string with newlines to separate
# the wrapped lines."""

# print(textwrap.fill(doc, width=40))

# import locale

# time2 = locale.setlocale(locale.LC_ALL, "English_United States.1252")
# print(time2)

# from string import Template

# t = Template("${village} folk send $$10 to $cause")
# s = t.substitute(village="Nottingham", cause="the ditch fund")
# print(s)

# import time, os.path

# photofiles = ["files/a.txt", "files/b.txt"]


# class BatchRename(Template):
#     delimiter = "%"


# fmt = input("Enter rename style (%d-date %n-seqnum %f-format):  ")


# t = BatchRename(fmt)
# date = time.strftime("%d%b%y")
# for i, filename in enumerate(photofiles):
#     base, ext = os.path.splitext(filename)
#     newname = t.substitute(d=date, n=i, f=ext)
#     print("{0} --> {1}".format(filename, newname))

# import struct

# with open("basic learning/files.zip", "rb") as f:
#     data = f.read()

# start = 0
# for i in range(2):
#     fields = struct.unpack("<IIIHH", data[start : start + 16])
#     crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

#     start += 16
#     filename = data[start : start + filenamesize]
#     start += filenamesize
#     extra = data[start : start + extra_size]
#     print(filename, hex(crc32), comp_size, uncomp_size)

#     start += extra_size + comp_size

# import threading, zipfile


# class AsyncZip(threading.Thread):
#     def __init__(self, infile, outfile):
#         threading.Thread.__init__(self)
#         self.infile = infile
#         self.outfile = outfile

#     def run(self):
#         f = zipfile.ZipFile(self.outfile, "w", zipfile.ZIP_DEFLATED)
#         f.write(self.infile)
#         f.close()
#         print("Finished background zip of:", self.infile)


# background = AsyncZip("basicLearning/fibo.py", "basicLearning/files.zip")
# background.start()
# print("the main program continues to run in foreground.")

# background.join()
# print("main program waited until background was done.")

# import logging

# logging.debug("debug information")
# logging.info("information message")
# logging.warning("warning message")
# logging.error("error occurred")
# logging.critical("critical error -- shutting down")

# from array import array

# a = array("H", [400, 200, 10, 222])

# print(sum(a))
# print(a[1:3])

# from collections import deque

# d = deque(["task1", "task2", "task3"])
# d.append("task4")
# print("Handling", d.popleft())

# import bisect

# scores = [(100, "perl"), (200, "tcl"), (400, "lua"), (500, "python")]
# bisect.insort(scores, (300, "ruby"))
# print(scores)

# from heapq import heapify, heappop, heappush

# data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# heapify(data)  # 将列表重新调整为堆顺序
# heappush(data, -5)  # 添加一个新条目
# h = [heappop(data) for i in range(3)]
# print(h)

from decimal import *

print(round(Decimal("0.70") * Decimal("1.05"), 2))
print(round(0.70 * 1.05, 2))

print(Decimal("1.00") % Decimal(".10"))
print(sum([Decimal("0.1")] * 10) == Decimal("1.0"))
