class SearchEngine():
    def __init__(self, name):
        self.name = name

   
    def __str__(self) -> str:
        return f'Search Engine Name: {name}'
 
    @staticmethod
    def binary_search(user_list, el):
        """returns:
        - index of given element in a list
        - number of operations
        """
        
        mid = len(user_list) // 2
        if el == user_list[mid]:
            return mid, 1
        
        i = 0
        p = 0
        q = len(user_list)
        while True:
            i += 1
            mid = p + (q - p) // 2 #  p + len(user_list[p:q]) // 2
            if el == user_list[mid]:
                return mid, i - 1
            elif el > user_list[mid]:
                p += (q - p) // 2 #  len(user_list[p:q]) // 2
            else:
                q -= (q - p) // 2 # len(user_list[p:q]) // 2
            if q - p == 0:
                return 'No such value in list'

    @staticmethod
    def binary_search_(user_list, el, p=0, q=None):
        """returns index of given element in a list"""
        mid = p + len(user_list[p:q]) // 2
        if not q:
            q = len(user_list)
        if el == user_list[mid]:
            return mid
        if q - p == 1:
            return 'No such value in list'
        elif el > user_list[mid]:
            p += len(user_list[p:q]) // 2
            return SearchEngine.binary_search_(user_list, el, p, q)
        else:
            q -= len(user_list[p:q]) // 2
            return SearchEngine.binary_search_(user_list, el, p, q)
    
    @staticmethod
    def binary_search__(user_list, el):
        """returns:
        - index of given element in a list,
        - no. of operations
        """
        i = 0
        p = 0
        q = len(user_list) - 1
        while p <= q:
            i += 1
            mid = (p + q) // 2
            guess = user_list[mid]
            if guess == el:
                return mid, i - 1
            elif guess > el:
                q = mid - 1
            else:
                p = mid + 1
        return None
    
    @staticmethod
    def find_smallest_val(user_list):
        """returns index of smallest item in list"""
        ind = 0
        for i, el in enumerate(user_list[1:], start=1):
            if el < user_list[i-1] and el < user_list[ind]:
                ind = i
        return ind
    
    @staticmethod
    def sort_by_choice(user_list):
        sorted_list = []
        for i in range(len(user_list)):
            ind = SearchEngine.find_smallest_val(user_list)
            sorted_list.append(user_list[ind])
            user_list = user_list[:ind] + user_list[ind+1:]
        return sorted_list
    
    @staticmethod
    def count_el(user_list, i=0):
        """returns no. of elements in the input list"""
        if not user_list:
            return 0
        else:
            i =+ 1
            return 1 + SearchEngine.count_el(user_list[i:])


def main():
    my_list = [4,6,7,9,11,13,16,21,22,29,34]
    my_ind = SearchEngine.binary_search(my_list, 21)
    print(my_ind)
    # my_list = [101,501,100,1001,1111,13,16,21,1.11,29,34]
    # index_of_smallest = SearchEngine.find_smallest_val(my_list)
    # print(index_of_smallest)
    # my_sorted_list = SearchEngine.sort_by_choice(my_list)
    # print(my_sorted_list)
    # count_el = SearchEngine.count_el([100, 99, 33,'i', 'k', 'l'])
    # print(count_el)

if __name__ == '__main__':
    main()