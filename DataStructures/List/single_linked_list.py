from DataStructures.List import list_node as node
def new_list ():
    new_list = {
    'first': None,
    'last': None,
    'size': 0,
    }
    return new_list

def add_first(my_list, element):
    nuevo = node.new_single_node(element)
    if my_list["size"]==0:
        my_list["first"]= nuevo
        my_list["last"]=nuevo
        my_list["size"]+=1
    else:
        inicial = my_list["first"]
        nuevo["next"] = inicial
        my_list["first"] = nuevo
        my_list["size"] += 1
        
    return my_list

def add_last(my_list, element):
    nuevo = node.new_single_node(element)
    if my_list["size"] == 0:
         my_list["first"] = nuevo
         my_list["last"] = nuevo
    else:
        my_list["last"]["next"] = nuevo
        my_list["last"] = nuevo
    my_list["size"] += 1
    
    return my_list
        

def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else:
        return False
    
def size(my_list):
    return my_list["size"]

def first_element(my_list):
    return my_list["first"]["info"]
    
def last_element(my_list):
    if is_empty(my_list):
        return None
    else:
        return my_list["last"]["info"]

def get_element(my_list, pos):
    if (is_empty(my_list)) or (pos < 0) or (pos > size(my_list)):
        return None
    if pos == 0:
        return my_list["first"]["info"]
    else:
        actual = my_list["first"]
        i = 0
        while (actual != None) and (i != pos):
            actual = actual["next"]
            i += 1    
            if i == pos:
                return actual["info"]

def remove_first(my_list):
    if is_empty(my_list):
        return None 
    else:
        first_nodo = my_list["first"]
        nodo = node.new_single_node(first_nodo)
        info_nodo = nodo["info"]
        my_list["first"] = first_nodo ["next"]
        my_list["size"] -= 1
        if size(my_list) == 0:
            my_list["last"] = None
            my_list["first"] = None
        return info_nodo

def remove_last(my_list):
    if is_empty(my_list):
        return None 
    else:
        actual = my_list ["first"]
        while actual["next"] is not None:
            prev = actual
            actual = actual["next"]
        prev["next"] = None
        my_list["last"] = prev
        my_list["size"] -= 1
        if size(my_list) == 0:
            my_list = new_list()
        return my_list

def insert_element(my_list, element, pos):
    if pos < 0 or pos > size(my_list): 
        return None
    else:
        nodo = node.new_single_node(element)
        if is_empty(my_list) or pos == 0:
            nodo["next"] = my_list["first"]
            my_list["first"] = nodo
            if my_list["size"] == 0:
                my_list["last"] = nodo
        else:
            actual = my_list ["first"]
            i = 0
            while (actual != None) and (i != pos):
                prev = actual
                actual = actual["next"]
                i += 1
            nodo["next"] = actual
            prev["next"] = nodo
            if nodo["next"] is None:
                my_list["last"] = nodo
        my_list["size"] += 1
        
        return my_list

def is_present(my_list, element, cmp_function):
    actual = my_list["first"]
    pos = 0
    while actual != None:
        if cmp_function(element, actual["info"]) == 0:
            return pos
        else:
            pos += 1
            actual = actual["next"]
    return -1

def delete_element(my_list, pos):    
    nodo = my_list["first"]
    nodo_anterior = None
    conteo = 0
    
    while conteo < pos:
        nodo_anterior = nodo
        nodo = nodo["next"]
        conteo += 1
    nodo_actual = nodo
    nodo_posterior = nodo_actual["next"]
    if nodo_anterior == None:
        my_list["first"] = nodo_posterior
    else:
        nodo_anterior["next"] = nodo_posterior
    if nodo_posterior == None:
        my_list["last"] = nodo_anterior
    
    my_list["size"] -= 1
    
    return my_list

def exchange(my_list, pos1, pos2):
    a1=get_element(my_list,pos1)
    a2=get_element(my_list,pos2)
    change_info(my_list,pos1,a2)
    change_info(my_list,pos2, a1)
    
    return my_list
    

def change_info(my_list, pos, new_info):
    a=my_list["first"]
    for i in range(pos):
        a=a["next"]
    a["info"] = new_info
    
    return my_list
        
        
        
    pass

def sub_list(my_list, pos, numelem):
    sub_list = new_list()
    nodo = my_list["first"]
    conteo = 0

    while conteo < pos and nodo != None:
        nodo = nodo["next"]
        conteo += 1

    for nodos in range(numelem):
        if nodo is None:
            break
        nuevo_nodo = node.new_single_node(nodo["info"])
        if sub_list["first"] is None:
            sub_list["first"] = nuevo_nodo
        else:
            sub_list["last"]["next"] = nuevo_nodo
        sub_list["last"] = nuevo_nodo
        sub_list["size"] += 1
        nodo = nodo["next"]

    return sub_list
def selection_sort(my_list, sort_crit):
    for i in range(my_list["size"]):
        menor= get_element(my_list,i)
        
        for  j in range(i,my_list["size"]):
            if sort_crit(get_element(my_list,j),menor):
                menor=get_element(my_list,j)
                pos_menor=j
        exchange(my_list,i,pos_menor)
    return   my_list


def shell_sort(my_list,sort_crit):
    gaps=size(my_list)//2+1
    while gaps!=0:
        for i in range(0,size(my_list)-gaps):
            if sort_crit(get_element(my_list,i),get_element(my_list,i+gaps)):
                pass
            else:
                exchange(my_list,i,i+gaps)
        if gaps==1:
            gaps=0
        gaps=gaps//2 
    return my_list        
def clear(my_list):
    my_list['first'] = None
    my_list['last'] = None
    my_list['size'] = 0
    return my_list
                
def merge_sort(my_list, sort_crit):
    if size(my_list) > 1:
        mitad = size(my_list) // 2
        iz = sub_list(my_list, 0, mitad)
        der = sub_list(my_list, mitad, size(my_list) - mitad)
        merge_sort(iz, sort_crit)
        merge_sort(der, sort_crit)
        clear(my_list)
        i, j = 0, 0
        while i < size(iz) and j < size(der):
            if sort_crit(get_element(iz, i), get_element(der, j)):
                add_last(my_list, get_element(iz, i))
                i += 1
            else:
                add_last(my_list, get_element(der, j))
                j += 1
        while i < size(iz):
            add_last(my_list, get_element(iz, i))
            i += 1
        while j < size(der):
            add_last(my_list, get_element(der, j))
            j += 1
    elif size(my_list) == 2:
        sort(my_list, sort_crit)
    return my_list

def sort(my_list, sort_crit):
    if size(my_list) == 2:
        if not sort_crit(get_element(my_list, 0), get_element(my_list, 1)):
            exchange(my_list, 0, 1)
    return my_list
def quick_sort(my_list, sort_criterial):
    def quicksort(arr, left, right):
        if left <right:
            partition_pos = partition (arr, left, right)
            quicksort(arr, left, partition_pos- 1)
            quicksort(arr, partition_pos + 1, right)
    def partition(arr, left, right):
        
        
        i = left
        j =right - 1
        pivot = get_element(arr,right)
        while i < j:
            
            while i < right and (sort_criterial(get_element(arr,i),pivot) or (sort_criterial(get_element(arr,i),pivot))and sort_criterial(pivot,get_element(arr,i))):
                i += 1
            while j > left and sort_criterial(pivot,get_element(arr,j)):
                j -= 1
            if i < j:
                exchange(arr,i,j)
        if sort_criterial(pivot,get_element(arr,i)):
            exchange(arr,right,i)
        return  i
    quicksort(my_list,0,size(my_list)-1)
    return my_list
#holaa

def insertion_sort(my_list, sort_crit):
    sorted_list = new_list()
    current = my_list["first"]
    while current is not None:
        next_node = current["next"]
        insert(sorted_list, current["info"], sort_crit)
        current = next_node
    return sorted_list

def insert(my_list, element, sort_crit):
    nodo = node.new_single_node(element)
    if size(my_list) == 0:
        my_list["first"] = nodo
        my_list["last"] = nodo
    else:
        actual = my_list["first"]
        prev = None
        while actual is not None and sort_crit(actual["info"], element):
            prev = actual
            actual = actual["next"]
        if prev is None:
            nodo["next"] = my_list["first"]
            my_list["first"] = nodo
        else:
            nodo["next"] = actual
            prev["next"] = nodo
        if nodo["next"] is None:
            my_list["last"] = nodo
    my_list["size"] += 1
    return my_list

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
