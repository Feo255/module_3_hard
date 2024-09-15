data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def dict_fun(_dict):
    dict_sum = 0
    for key in _dict.keys():
        print(type(key))
        if type(key) is int:
            dict_sum += key
        else:
            dict_sum += len(key)
    for value in _dict.values():
        print(type(value))
        if type(value) is int:
            dict_sum += value
        else:
            dict_sum += len(value)
    return(dict_sum)

def list_fun(_list):
    list_sum = 0
    for k in _list:
        print(type(k))
        if type(k) is int:
            list_sum += k
        elif type(k) is set:
            list_sum += set_func(k)
        else:
            list_sum+= len(k)

    return(list_sum)

def tuple_fun1(_tuple):
    tuple_sum = 0
    for v_tuple in _tuple:
        print(type(v_tuple))
        if type(v_tuple) is int:
            tuple_sum += v_tuple
        elif type(v_tuple) is dict:
            tuple_sum += dict_fun(v_tuple)
        elif type(v_tuple) is tuple:
            tuple_sum += tuple_fun1(v_tuple)
        elif type(v_tuple) is set:
            tuple_sum += set_fun(v_tuple)
        elif type(v_tuple) is str:
            tuple_sum += len(v_tuple)
        elif type(v_tuple) is list:
            tuple_sum += list_fun(v_tuple)
    return (tuple_sum)

def set_func(_set):
    set_sum = 0
    for v_set in _set:
        print(type(v_set))
        if type(v_set) is int:
            set_sum += v_set
        elif type(v_set) is dict:
            set_sum += dict_fun(v_set)
        elif type(v_set) is tuple:
            set_sum += tuple_fun1(v_set)
    return (set_sum)

def calculate_structure_sum(d_s):
    d_s_sum = 0
    for i in d_s:
        if type(i) is list:
            print(type(i))
            d_s_sum += list_fun(i)
            print(d_s_sum)
        elif type(i) is dict:
            d_s_sum += dict_fun(i)
            print(d_s_sum)
        elif type(i) is tuple:
            d_s_sum += tuple_fun1(i)
            print(d_s_sum)
        elif type(i) is str:
            d_s_sum += len(i)





    return(d_s_sum)


result = calculate_structure_sum(data_structure)
print(result)