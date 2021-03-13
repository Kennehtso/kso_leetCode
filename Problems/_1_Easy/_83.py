from typing import List
class ListNode:
    def __init__(self, val=0, next =None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        d={}
        pre = cur = head
        while cur:
            if cur.val in d:
                pre.next = cur.next
            else:
                d[cur.val] = cur.val
                pre = cur
            cur = cur.next
        return head
slt = Solution()    
# Test Case
l1 = ListNode(1, ListNode(1, ListNode(2,  ListNode(3,  ListNode(3, None)))))
slt.deleteDuplicates(head = l1)

"""
83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, 
delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.

Example 1:
    Input: head = [1,1,2]
    Output: [1,2]

Example 2:
    Input: head = [1,1,2,3,3]
    Output: [1,2,3]

Constraints:
    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.

"""
