# https://github.com/qiyuangong/leetcode

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


class Solution:
    def two_sum(self, nums, target):
        index_map = {}
        for index, num in enumerate(nums):
            if target - num in index_map:
                return index_map[target - num], index
            index_map[num] = index
            
def main():
    print(Solution().two_sum(nums=[2, 7, 11, 15], target=9))
    print(Solution().two_sum(nums=[2, 7, 11, 15], target=18))
    print(Solution().two_sum(nums=[2, 7, 11, 15], target=22))

if __name__ == '__main__':
    main()

