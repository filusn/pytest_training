import sys
import requests


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
#     print("This is linux-only function")
#     if not sys.platform.startswith("win"):
#         return True
#     else:
#         raise RuntimeError
#
#
def impossible_function():
    print("This method runs only with certain configuration")
    response = requests.get('fifinow.com/amazing')
    return response.text
#
# def raises():
#     x = list()
#     p = x[1]
#
#


def getting_response(request):
    if request.method == 'GET':
        return {}
    if request.method == 'POST':
        return request.POST
