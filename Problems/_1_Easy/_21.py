from typing import List
import copy
class ListNode:
    def __init__(self, val=0, next =None):
        self.val = val
        self.next = next

class Solution:
     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = res = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        #print("res: ", res.next)
        return res.next
        
        """
        print(f"--- The End ---")
        print(f"result: {result}")
        print("---------------------------")
        print(f"Work: {work}")
        print("---------------------------")
        print(f"cur_l1: {cur_l1}")
        print("---------------------------")
        print(f"cur_l2: {cur_l2}")
        print("----------------------------------------------------")
        """
        """
        # print result
        chk, chkList = copy.copy(result), []
        while chk:
            chkList.append(chk.val) 
            chk = chk.next
        chkList.pop(0)
        print(chkList)
        """
        return result.next

slt = Solution()

# Test Case
l1 = ListNode(1, ListNode(2, ListNode(3,  ListNode( 5,  ListNode(8, None)))))
l2 = ListNode(1, ListNode(3, ListNode(4,  ListNode( 5,  ListNode(6, ListNode(7, None))))))
slt.mergeTwoLists(l1,l2)
"""
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
================================================================================================================
Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
================================================================================================================
Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both l1 and l2 are sorted in non-decreasing order.
"""
