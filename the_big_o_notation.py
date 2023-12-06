import random as rd
import numpy as np
from data_structures import SearchEngine

def ssss_(list_, search_for):
    """
    sequential list (sequence) search
    returns:
    - true if 'search_for' is in the string
    - no. of operations
    """
    for i, el in enumerate(list_):
        if search_for == el:
            return True, i+1
    return False, 'not found'

def exp_time_compl(n_sim, list_):
    """
    returns simulation based:
    - the expected time complexity of sequential list (sequence) search
    - the pessimistic time complexity of sequential list (sequence) search
    """
    res = []
    for i in range(n_sim):
        no_of_op = ssss_(list_, rd.randint(0, len(list_)-1))[1]
        res.append(no_of_op)
    std = np.std(res)
    return f'{np.round((std / len(list_)), 2)} * n', f'{max(res) / len(list_)} * n'

def exp_time_compl_bs(n_sim, list_):
    """
    returns simulation based:
    - the expected time complexity of binary search
    - the pessimistic time complexity of binary search
    """
    res = []
    for i in range(n_sim):
        no_of_op = SearchEngine.binary_search(list_, rd.randint(0, len(list_)-1))[1]
        res.append(no_of_op)
    std = np.std(res)
    return std, max(res), f'{np.round((std / len(list_)), 2)} * n', f'{max(res) / len(list_)} * n'


def main():
    list_length = 4096
    n_sim = 30000
    my_list = [i for i in range(list_length)]
    #print(exp_time_compl(n_sim, my_list))
    print(exp_time_compl_bs(n_sim, my_list))


if __name__ == '__main__':
    main()