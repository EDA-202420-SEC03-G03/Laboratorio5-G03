def new_list():
    lst = {
        "elements":[],
        "size": 0
    }
    
    return lst


def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    
    return my_list


def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    
    return my_list


def is_empty(my_list):
    if my_list["size"]==0:
        return True
    else:
        return False 


def size(my_list):
    return my_list["size"]


def first_element(my_list):
    return my_list["elements"][0]


def last_element(my_list):
    return my_list["elements"][-1]


def get_element(my_list, pos):
    if my_list["size"]== 0:
        element = -1
    else:
        element = my_list["elements"][pos]
    return element


def delete_element(my_list, pos):
    my_list["elements"].pop(pos)
    my_list["size"] -= 1
    
    return my_list


def remove_first(my_list):
    my_list["elements"].pop(0)
    my_list["size"] -= 1
    
    return my_list


def remove_last(my_list):
    last = my_list["size"] - 1
    my_list["elements"].pop(last)
    my_list["size"] -= 1
    
    return my_list


def insert_element(my_list, element, pos):
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    
    return my_list


def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if (cmp_function(element, info) == 0):
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1


def change_info(my_list, pos, new_info):
    size = my_list["size"]
    if size > 0:
        my_list["elements"][pos] = new_info
    return my_list


def exchange(my_list, pos1, pos2):
    size = my_list["size"]
    if size > 0:
        info_pos1 = my_list["elements"][pos1]
        info_pos2 = my_list["elements"][pos2]
        
        my_list["elements"][pos1] = info_pos2
        my_list["elements"][pos2] = info_pos1
    return my_list


def sub_list(my_list, pos, numelem):
    size = my_list["size"]
    if size > 0:
        sub_elements = my_list.copy()["elements"][pos : pos + numelem]
        sublist = new_list()
        sublist["elements"] = sub_elements
        sublist["size"] = len(sub_elements)
        return sublist
    return -1

#-------------------
# Sorting criteria
#-------------------

def sort_crit_ascending(element1, element2):
    is_sorted = False
    if element1 <= element2:
        is_sorted = True
    return is_sorted

def sort_crit_descending(element1, element2):
    is_sorted = False
    if element1 >= element2:
        is_sorted = True
    return is_sorted

