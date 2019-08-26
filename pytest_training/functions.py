def add(a, b):
    return a+b


def t_or_f(x):
    if x < 5:
        return True
    elif x < 10:
        return False
    else:
        return None


# def not_implemented():
#     ...
#
#
# def linux_function():
#     """
#     This function
#     :return:
#     """
#     print("This is linux-only function")
#     return True
#
#
# def impossible_function():
#     print("This method runs only with certain configuration")
#
# def raises():
#     x = list()
#     p = x[1]
#
#
# if __name__ == '__main__':
#     import xdoctest as xdoc
#     xdoc.doctest_module(__file__)