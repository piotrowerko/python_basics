# https://github.com/qiyuangong/leetcode

# https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/3785463/video-visualization-of-o-n-sliding-window-solution/

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

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str_num  = str(digits)[1:-1].replace(",","").replace(" ","")
        number_ = int(str_num)
        plus_1 = number_ + 1
        plus_1_str = str(plus_1)
        end_list = []
        for el in plus_1_str:
            end_list.append(int(el))
        return end_list

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(x) for x in str(int(''.join([str(i) for i in digits])) + 1)]
     
def main():
    print(Solution().plusOne([1,2,3]))


if __name__ == '__main__':
    main()