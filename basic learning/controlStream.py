# while
# a, b=0,1
# while a<10:
#     print(a,end=',')
#     a,b=b,a+b

# if
# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('it\'s negative')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# for
# words=['cat','window','defenestrate']
# for w in words:
#     print(w,len(w))

# users={'Hans':'active','Brant':'inactive','tt':'active'}

# for user,status in users.copy().items():
#     if status=='inactive':
#         print(user,status)
#         del users[user]
#         print(users)

# active_users={}
# for user,status in users.items():
#     if status=='active':
#         active_users[user]=status
# print(active_users)

# range

# for i in range(5):
#     print(i,end=',')

# list(range(5,10))
# list(range(0,10,3))
# list(range(-10,-100,-30))

# a=['mary','had','a','little','lamb']
# for i in range(len(a)):
#     print(i,a[i])

# break and continue

# for n in range(2,10):
#     for x in range(2,n):
#         if n%x==0:
#             print(f"{n} = {x} * {n//x}")
#             break

# for num in range(2,10):
#     if num%2==0:
#         print(f"found an even number {num}")
#         continue
#     print(f"found an odd number {num}")

# for else

# for n in range(2,10):
#     for x in range(2,n):
#         if n%x==0:
#             print(n,'equals',x,'*',n//x)
#             break
#     else:
#         print(n,'is a prime number')

# pass
# while True:
#     pass

# class MyEmptyClass:
#     pass

# def initlog(*args):
#     pass

# match case

# def http_error(status):
#     match status:
#         case 400:
#             return '400'
#         case 404:
#             return '404'
#         case 418:
#             return '418'
#         case 401|403|406:
#             return 'other'
#         case _:
#             return 'anything'

# print(http_error(406))

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

# def where_is(point):
#     match point:
#         case Point(x=0,y=0):
#             print("origin")
#         case Point(x=0,y=y):
#             print(f"y={y}")
#         case Point(x=x,y=0):
#             print(f"x={x}")
#         case Point():
#             print("somewhere else")
#         case _:
#             print("not a point")

# pi=Point(2,2)

# where_is(1)

# from enum import Enum
# class Color(Enum):
#     Red='red'
#     Green='green'
#     Blue='blue'

# color=Color(input("enter your favourite color: "))

# match color:
#     case Color.Red:
#         print('red')
#     case Color.Green:
#         print('green')
#     case Color.Blue:
#         print('blue')
#     case _:
#         print('other color')

# function
# def fib(n):
#     a,b=0,1
#     while a<n:
#         print(a,end=' ')
#         a,b=b,a+b
#     print()
#     return a,b

# f=fib

# a=f(10)

# print(a)


# def ask_ok(prompt, retries=4, reminder="Please try again!"):
#     while True:
#         reply = input(prompt)
#         if reply in {"y", "ye", "yes"}:
#             return True
#         if reply in {"n", "no", "nop", "nope"}:
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError("invaild user response")
#         print(reminder)


# ask_ok("OK to overwrite the file?", 2, "Come on, only yes or no!")


# def parrot(a, b="b", c="c", d="d"):
#     print(f"a={a}, b={b}, c={c}, d={d}")


# parrot(d="4", a=2, c="9")


# def cheese_shop(a, *b, **c):
#     print("a: ", a)
#     for argB in b:
#         print("b: ", argB)
#     print("_" * 40)
#     for kw in c:
#         print(kw, ":", c[kw])


# cheese_shop("testA", "testB1", "testB2", testC1="C1", testC2="C2")


# def combined_example(pos_only, /, standard, *, kwd_only):
#     print(pos_only, standard, kwd_only)


# combined_example(1, 2, kwd_only=3)

# arg = [3, 6]
# print(list(range(*arg)))


# def make_in(n):
#     return lambda x: x + n


# f = make_in(42)
# print(f(0))


def my_fun():
    """
    do noting
    do nothing
    do anything
    """


print(my_fun.__doc__)
