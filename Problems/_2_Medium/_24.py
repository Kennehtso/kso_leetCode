from typing import List
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = vir = ListNode(0, head)
        while cur.next and cur.next.next:
            st = cur.next
            nd = cur.next.next
            st.next = nd.next
            cur.next = nd
            nd.next = st
            cur = cur.next.next
        return vir


slt = Solution()
_8 = ListNode(8, None)
_7 = ListNode(7,_8)
_6 = ListNode(6,_7)
_5 = ListNode(5,_6)
_4 = ListNode(4,_5)
_3 = ListNode(3,_4)
_2 = ListNode(2,_3)
_root = ListNode(1,_2)
slt.swapPairs(_root)
"""
24. Swap Nodes in Pairs
Medium

Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes 
(i.e., only nodes themselves may be changed.)

Example 1:
    Input: head = [1,2,3,4]
    Output: [2,1,4,3]

Example 2:
    Input: head = []
    Output: []

Example 3:
    Input: head = [1]
    Output: [1]



Constraints:
    The number of nodes in the list is in the range [0, 100].
    0 <= Node.val <= 100

"""