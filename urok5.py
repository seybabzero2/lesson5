# import requests
#
# def func():
#     pass
#
# class Human:
#     pass
#
# rq = requests
# func = func
# nick = Human
# print(requests.__name__)
# print(rq.__name__)
# print(func.__name__)
# print(nick.__name__)

#!ACHTUNG!
# import tkinter
#
# list_1 = []
# # for method in dir(tkinter):
# #     print(method)
#
# for method in dir(tkinter.mainloop):
#     print(method)
# test = "string"
# print(hasattr(test, "reverse"))
# print(hasattr(test, "index"))

#!!
# test = "test"
# def func():
#     pass
# print(callable(test)) #call able
# print(callable(func))

# class Father:
#     pass
#
# class Son(Father):
#     pass
#
# obj_son = Son()
# print(issubclass(Father, Son))
# print(issubclass(Son, Father))
# print(isinstance(obj_son, Son))
# print(isinstance(obj_son, Father))



#!WARNING!
# import inspect
# import datetime
#
# print(inspect.ismodule(datetime))
# print(inspect.isclass(datetime))
# print(inspect.isfunction(datetime))

# import sys
#
# print(sys.executable)
# print(sys.version)
# print(sys.platform)
# print(sys.argv)

# for _ in dir(__builtins__):
#     print(_)

import inspect
print(inspect.ismodule(inspect))
print(callable(inspect))
for method in dir(inspect):
    print(method)
print(inspect.isclass(inspect.ismodule))
print(callable(inspect.ismodule))
for method in dir(inspect.ismodule):
    print(method)
