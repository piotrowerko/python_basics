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
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        p = 0
        q = len(nums) - 1
        if target < nums[0]:
            return 0
        elif target > nums[q]:
            return q + 1
        while p <= q:
            mid = (p + q) // 2
            guess = nums[mid]
            if guess == target:
                return mid
            elif guess > target:
                q = mid - 1
            else:
                p = mid + 1
        # if target > nums[mid]:
        #     return mid + 1 
        # else:
        #     return mid
        return p

class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l

            
def main():
    print(Solution().searchInsert(nums=[1,3,5,6], target=2))

if __name__ == '__main__':
    main()
