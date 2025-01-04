# print("hello" + " world" + "!")
# print('cat\'s color')
# print("hello\n world")
# print("""
#     hello
#     world
#     hope you everything
#     is okay
# """)

# my_love = 123
# print(f"my love num is {my_love}")

import math

# result = math.log2(8)
# print(result)

a = -1
b = -2
c = 3
delta = b ** 2 - 4 * a * c
result_a = (-b + math.sqrt(delta)) / (2 * a)
result_b = (-b - math.sqrt(delta)) / (2 * a)

print(result_a, result_b)
