class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def of(Cls, lst):
        head = None
        for val in reversed(lst):
            head = Cls(val, head)
        return head

    def __iter__(self):
        head = self
        while head:
            yield head.val
            head = head.next

class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


def main():
    head = ListNode.of([1,2,3,4,5])
    print(*Solution().middleNode(head))

if __name__ == '__main__':
    main()
