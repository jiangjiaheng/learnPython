contact_list = {"zhangsan": 123, "lisi": 456}
contact_list[("wangwu", 20)] = 789
contact_list[("wangwu", 25)] = 110

# print(contact_list["zhangsan"])
# print(contact_list)
# print(contact_list[("wangwu", 25)])

# test = ("wangwu", 25)
# test2 = "zhangsan"
# print(len(test))
# print(len(test2))

import re
import ast

query = input("please input your contact user name: ")

if re.match(r'^\(.*\)$', query):
    query = ast.literal_eval(query)

if query in contact_list:
    print(f"this user number is {contact_list[query]}")
else:
    print("this user is not in your contact list")
    print(f"your contact amount is {len(contact_list)}")
