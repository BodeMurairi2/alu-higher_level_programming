#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0

    weight_sum = 0
    score_product = 0

    for i in my_list:
        score_product += i[0] * i[1]
        weight_sum += i[1]
    result = score_product / weight_sum

    return result
