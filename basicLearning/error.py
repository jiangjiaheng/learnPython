# while True print('hello world')

# 10 * (1 / 0)

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("No, it's not a number!")

# try:
#     raise Exception("spam", "eggs")
# except Exception as inst:
#     print(type(inst))
#     print(inst.args)
#     print(inst)

#     x, y = inst.args
#     print("x=", x)
#     print("y=", y)

# import sys

# try:
#     f = open("myfle.txt")
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error:", err)
# except ValueError:
#     print("Could not convert data to an integer")
# except Exception as err:
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise

# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, "r")
#     except OSError:
#         print(f"cannot open {arg}")
#     else:
#         print(arg, "has", len(f.readlines()), "lines")
#         f.close()


# def this_fails():
#     x = 1 / 0


# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print(f"Handling run time error: {err}")

# raise NameError("Hi there")

# try:
#     raise NameError("HiThere")
# except NameError:
#     print("An exception flew by!")
#     raise


# def func():
#     raise ConnectionError


# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError("Failed to open database") from exc

# try:
#     raise KeyboardInterrupt
# finally:
#     print("Goodbye world")


# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("division by zero!")
#     else:
#         print(f"result is {result}")
#     finally:
#         print("executing finally clause")


# divide(2, 0)

# try:
#     raise TypeError("bad type")
# except Exception as e:
#     e.add_note("add some information")
#     e.add_note("add some more information")
#     raise


def f():
    raise OSError("operation failed")


excs = []
for i in range(3):
    try:
        f()
    except Exception as e:
        e.add_note(f"Happened in Iteration {i+1}")
        excs.append(e)

raise ExceptionGroup("we have some problems", excs)
