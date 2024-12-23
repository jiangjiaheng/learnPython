# with open("a.txt", encoding="utf-8") as f:
#     read_data = f.read()
#     print(read_data)
# print(f.closed)

f = open("a.txt", "r+", encoding="utf-8")

# print(f.read())
# print(f.read())

# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

# for line in f:
#     print(line, end="")

# f.write("This is a test\n")

# value = ("the answer", 42)
# s = str(value)
# f.write(s)

# print(f.seek(5))

# import json

# x = {"a": 123, "b": 456, "c": 789}

# y = json.dumps(x)
# print(y)

# json.dump(x, f)

# y = json.load(f)
# print(y)

if not f.closed:
    f.close()
    print("f closed is", f.closed)
