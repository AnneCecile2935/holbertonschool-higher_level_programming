#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
     # 'map' applies the lambda function to each element of 'my_list'.
    # The lambda function multiplies each element by 'number'.
    # The result of 'map' is an iterable, so we convert it to a list.
    return list(map(lambda x: x * number, my_list))
