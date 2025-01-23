contact_list = ["zhangsan", "lisi", "wangwu"]

for person in contact_list:
    # message = f"""
    # hi {person},
    # your phone is out of fee,
    # please recharge it, thanks
    # """
    message = """
        hi {0},
        your phone is out of fee,
        please recharge it, thanks
    """.format(person)
    print(message)
