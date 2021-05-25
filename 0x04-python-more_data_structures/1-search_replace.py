#!/usr/bin/python
def search_replace(my_list, search, replace):
    if len(my_list) > 0:
        new_list = []
        for i in range(len(my_list)):
            if my_list[i] == search:
                new_list.insert(i,  replace)
            else:
                new_list.insert(i, my_list[i])
        return new_list
