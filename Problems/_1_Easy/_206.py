from typing import List

class ListNode:
    def __init__(self, val=0, _next =None):
        self.val = val
        self._next = _next
class Solution:
    def reverseList_iteratively(self, head: ListNode) -> ListNode:
        # iteratively 
        cur = head
        tmp = None
        res = None
        while cur:
            tmp =  cur._next
            cur._next = pre
            pre = cur
            cur = tmp
        return res
       
    def reverseList_recursively(self, head: ListNode) -> ListNode: #iteratively 
        # recursively
        if not head  or not head._next :
            return head
        p = self.reverseList_recursively(head._next)
        head._next._next = head
        head._next = None
        return p
            
slt = Solution()
# Test Case
slt.reverseList_iteratively(ListNode(1, ListNode(2, ListNode(3,  ListNode( 4,  ListNode(5, None))))))
slt.reverseList_recursively(ListNode(1, ListNode(2, ListNode(3,  ListNode( 4,  ListNode(5, None))))))
"""
206. Reverse Linked List

Reverse a singly linked list.
================================================================================================================
Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

================================================================================================================
[1,2,3,4,5]
None
ListNode{val: 1, next: None}
ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}
--------------------
ListNode{val: 1, next: None}
ListNode{val: 2, next: ListNode{val: 1, next: None}}
ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
--------------------
ListNode{val: 2, next: ListNode{val: 1, next: None}}
ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}
ListNode{val: 4, next: ListNode{val: 5, next: None}}
--------------------
ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}
ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}
ListNode{val: 5, next: None}
--------------------
ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}
ListNode{val: 5, next: ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}}
None
--------------------
"""