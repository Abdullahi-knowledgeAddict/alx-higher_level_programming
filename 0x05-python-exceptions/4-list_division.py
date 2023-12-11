#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """ Generates new list, for dividing, Index corresponding
        Elements in list1 by list2

        Args:
            list_length: Number of element expected in quotient list
            my_list_1:   The list of dividend
            my_list_2:   The list of divisors

        Return:
            The new list with list_length number of element
    """
    new_list = []
    i = 0
    while (i < list_length):
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            i += 1
    return new_list
