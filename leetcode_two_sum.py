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
    def two_sum(self, nums, target):
        answer = []
        for i in range(0, len(nums), 1):
            for j in range(i+1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    answer.append(i)
                    answer.append(j)
        return answer

class Solution__():
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found
    
class Solution():
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i, el in enumerate(nums):
            complement = target - el
            if complement in numMap:
                return [numMap[complement], i]
            numMap[el] = i

        return []  # No solution found

class Solution():
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        needs_dictc = {}
        for i, el in enumerate(nums):
            if el in needs_dictc:
                return [needs_dictc[el], i]
            needs_dictc[target - el] = i

            
def main():
    print(Solution().two_sum(nums=[2, 7, 11, 15], target=9))
    print(Solution().two_sum(nums=[2, 7, 11, 15], target=18))
    print(Solution().two_sum(nums=[2, 7, 11, 15], target=22))

# responser u should get:
# (0, 1)
# (1, 2)
# (1, 3)


if __name__ == '__main__':
    main()

