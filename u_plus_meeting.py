from typing import List, Optional

class Solution__:
    def maxArea_brutforce(self, heights: list[int]) -> int:
        max_areas = []
        for i in range(len(heights)):
            areas = []
            heights_ = heights[i:]
            for hor_pos, height in enumerate(heights_):
                min_height = min(heights_[0], height)
                hor_dist = hor_pos - 0
                areas.append(min_height * hor_dist)
            max_areas.append(max(areas))
        return max(max_areas)
    
    def maxArea(self, heights: list[int]) -> int:
        left_pointer = 0
        right_pointer = len(heights) - 1
        max_area = 0
        while left_pointer < right_pointer:
            min_height = min(heights[left_pointer], heights[right_pointer])
            hor_dist = right_pointer - left_pointer
            current_area = min_height * hor_dist
            if current_area > max_area:
                max_area = current_area
            if heights[left_pointer] > heights[right_pointer]:
                right_pointer -= 1
            else:
                left_pointer += 1
        return max_area
    
class Solution_:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        else:
            return False


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_rev = l1[::-1]
        l2_rev = l2[::-1]
        l1_no = int(str(l1_rev)[1:-1].replace(' ','').replace(',',''))
        l2_no = int(str(l2_rev)[1:-1].replace(' ','').replace(',',''))
        output_ = str(l1_no + l2_no)[::-1]
        output_list = []
        for i in output_:
            output_list.append(int(i))
        return output_list 

# class Solution2:
#     def addTwoNumbers(self, l1, l2):
#         l1_rev = l1[::-1]
#         l2_rev = l2[::-1]
#         l1_no = int(str(l1_rev)[1:-1].replace(' ','').replace(',',''))
#         l2_no = int(str(l2_rev)[1:-1].replace(' ','').replace(',',''))
#         output_ = str(l1_no + l2_no)[::-1]
#         output_list = []
#         for i in output_:
#             output_list.append(int(i))
#         return output_list 



def main():
    #heights = [1,8,6,2,5,4,8,3,7]
    #heights = [2,3,10,5,7,8,9]
    l1 = ListNode[2,4,3]
    l2 = [5,6,4]
    sol = Solution()
    print(sol.addTwoNumbers(l1, l2))

if __name__ == '__main__':
    main()