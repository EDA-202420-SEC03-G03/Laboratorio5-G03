def new_list():
    lst = {
        "elements":[],
        "size": 0,
        "type":"ARRAY_LIST"
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

def selection_sort(my_list, sort_crit):
    
    
    for i in range(my_list["size"]):
        menor= my_list["elements"][i]
        
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
            
def merge_sort(my_list,sort_crit):
    def sort(list):
        if size(list)==2:
            if sort_crit(get_element(list,0),get_element(list,1)):
              pass
            else:
                
                exchange(list,1,0)
        
             
    if size(my_list)>2:
        mitad=size(my_list)//2
        iz=new_list()
        der=new_list()
        der["elements"]=my_list["elements"][mitad:]
        iz["elements"]=my_list["elements"][:mitad]
        iz["size"]=len(iz["elements"])
        der["size"]=len(der["elements"])
        
        merge_sort(iz,sort_crit)
        merge_sort(der,sort_crit)
        
        my_list["elements"] = []
        i, j = 0, 0
        
        while i < size(iz) and j < size(der):
            if sort_crit(get_element(iz, i), get_element(der, j)):
                my_list["elements"].append(get_element(iz, i))
                i += 1
            else:
                my_list["elements"].append(get_element(der, j))
                j += 1
        
        # Agregar los elementos restantes de iz y der
        my_list["elements"].extend(iz["elements"][i:])
        my_list["elements"].extend(der["elements"][j:])
        my_list["size"] = len(my_list["elements"])
                    
                     
            
            
    else:
         sort(my_list)
         
         
    return my_list            

def insertion_sort(my_list, sort_crit):
    for i in range(1, size(my_list)):
        llave = get_element(my_list, i)
        j = i - 1
        while j >= 0 and sort_crit(llave, get_element(my_list, j)):
            my_list['elements'][j + 1] = my_list['elements'][j]
            j -= 1
        my_list['elements'][j + 1] = llave
    return my_list