def fun_pro(num, fun):
    result = fun(num)
    print(result)


def add_fun(a):
    b = a + 1
    return b


def del_fun(a):
    b = a - 1
    return b


fun_pro(2, add_fun)

fun_pro(2, del_fun)

fun_pro(2, lambda num: num + 5)

fun_pro(4, lambda num: num ** num)
