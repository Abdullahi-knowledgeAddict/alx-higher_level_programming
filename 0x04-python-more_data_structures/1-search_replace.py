#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
        Replaces all occurences of an element by another in a new list

        Args:
            my_list: The Original list
            replace: The replacement
            search : The element to search for

        Return: The new list
    """
    return list(map(lambda x, search=search, replace=replace:
                replace if x == search else x, my_list))
