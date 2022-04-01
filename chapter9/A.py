#########################
# import sys
# sys.path.append('./')
# print(sys.path)

# from module1 import func1, func2, func3
from . import module1

# if __name__ == '__main__':
#     if __module1__ is None:
#         import sys
#         from os import path
#         print(path.dirname( path.dirname( path.abspath(__file__) ) ))
#         # sys.path.append(path.dirname( path.dirname( path.abspath(__file__) ) ))
#         sys.path.append(path.dirname(path.abspath(__file__)))
#         from module1 import *
#     else:
#         # from ..mymath import my_add
#         pass
#
#     func1()
#     func2()
#     func3()
#
#
# # import module1
#
if __name__ == '__main__':
    module1.func1()
    module1.func2()
    module1.func3()

# func1()
# func2()
# func3()