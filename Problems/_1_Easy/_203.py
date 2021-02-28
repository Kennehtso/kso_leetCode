from typing import List

class ListNode:
    def __init__(self, val=0, next =None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pre = sentinelPrint = sentinel = ListNode(0)
        cur = sentinel.next= head
        
        while cur:
            nxt = cur.next
            if cur.val == val:
                pre.next = nxt
            else:
                pre = cur
            cur = nxt
        
        while sentinelPrint:
            print(sentinelPrint.val)
            sentinelPrint = sentinelPrint.next
            print(f"--------------------")
        print(f"------------------------------------------------------------")
        
        return sentinel.next
            
slt = Solution()
_6_2 = ListNode( 6,  None)
_5 = ListNode( 5, _6_2)
_4 = ListNode( 4,  _5)
_3 = ListNode( 3,  _4)
_6_1 = ListNode( 6,  _3)
_2 = ListNode( 2,  _6_1)
_1_1 =  ListNode( 1,  _2)
_1_2  =  ListNode( 1,  _2)
# Test Case
slt.removeElements(_1_2, 4)
slt.removeElements(_1_1, 6)
"""
203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
--------------------
"""