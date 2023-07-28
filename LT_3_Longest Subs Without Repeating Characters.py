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
    def _lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        def find_single_max(_s):
            cur_sub_str = []
            recorded_max_length = 0
            for i, el in enumerate(_s):
                if el in cur_sub_str:
                    return recorded_max_length
                else:
                    cur_sub_str.append(el)
                    if len(cur_sub_str) > recorded_max_length:
                        recorded_max_length = len(cur_sub_str)
            return recorded_max_length
        
        ultra_max = 0
        for i in range(0, len(s), 1):
            _s = s[i:]
            curr_max = find_single_max(_s)
            if curr_max > ultra_max:
                ultra_max = curr_max
        return ultra_max
    
    def __lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {} # ley = char; val = ind


        return 'ppp'
    
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        length = 0
        for i, el in enumerate(s):
            if el in s[l:i]:
                l = s[:i].rindex(el) + 1
            else:
                length = max(length, i - l + 1)
        return length

class _Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l = 0
        length = 0
        for r in range(len(s)):
            char = s[r]
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                length = max(length, r - l + 1)
            seen[char] = r

        return length

     
def main():
    print(Solution().lengthOfLongestSubstring('bbtablud'))


if __name__ == '__main__':
    main()