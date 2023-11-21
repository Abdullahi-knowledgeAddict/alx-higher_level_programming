#!/usr/bin/python3
def weight_average(my_list=[]):
    """
        calculate the weighted average of all integers tuple
        (<score>, <weight>)

    Args:
        my_list: list containing all the tuples

    Return:
        The weighted average = \
        (score1 * weight1) + ... + (scoreN * weightN)/weight1 + ... + weightN
    """
    if my_list == []:
        return 0
    mult_tot = weight_tot = 0
    for x in my_list:
        mult_tot += (x[0] * x[1])
        weight_tot += x[1]
    return mult_tot / weight_tot
