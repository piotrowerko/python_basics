from typing import List
import collections
import itertools
import functools
import math
import string
import random
import bisect
import re
import operator
import heapq
import queue

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter


class Solution_():
    def getRow(self, rowIndex: int) -> List[int]:
        answer_list = []
        def one_down(temp_list):
            temp_list2 = []
            temp_list2.append(temp_list[0])
            for i in range(1, len(temp_list), 1):
                temp_list2.append(temp_list[i-1]+temp_list[i])
            temp_list2.append(temp_list[-1])
            return temp_list2
        
        temp_list = [1]
        for k in range(rowIndex):
            temp_list = one_down(temp_list)
        
        return temp_list
    
class Solution____:
    def getRow(self, rowIndex: int) -> List[int]:
        answer_list = []
        if rowIndex == 0:
            return [1]
        else:
            
            return Solution().getRow(rowIndex -1)
        
        #return temp_list

class __Solution():
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prev_row = self.getRow(rowIndex=rowIndex-1)
        curr_row = []
        curr_row.append(prev_row[0])
        for i in range(1, len(prev_row), 1):
            curr_row.append(prev_row[i-1]+prev_row[i])
        curr_row.append(prev_row[-1])
        return curr_row
    
class Solution():
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prev_row = self.getRow(rowIndex=rowIndex-1)
        curr_row = [1]
        for i in range(1, len(prev_row), 1):
            curr_row.append(prev_row[i-1]+prev_row[i])
        curr_row.append(1)
        return curr_row
            
def main():
    print(Solution().getRow(5))


# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]


if __name__ == '__main__':
    main()

