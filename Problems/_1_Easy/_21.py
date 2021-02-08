from typing import List
class ListNode:
    def __init__(self, val=0, next =None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode, round : int, nodeAsArr: []) -> ListNode:
        round+=1
        print(f"Round {round}: ")
        print(f"nodeAsArr: {nodeAsArr}")
        if l1 is None:
            print(f"l1 is None, return l2")
            print("------------------------------------")
            nodeAsArr.append(l2.val)
            print(f"return l2: {l2.val}")

            return l2
        elif l2 is None:
            print(f"l2 is None, return l1")
            print("------------------------------------")
            nodeAsArr.append(l1.val)
            print(f"return l1: {l1.val}")

            return l1
        elif l1.val < l2.val:
            
            l1_dis = None if l1.next is None else l1.next.val
            l2_dis = None if l2 is None else l2.val
            print(f"l2 is Higher, return mergeTwoLists(l1 next: {l1_dis}, l2 :{l2_dis})")
            print("------------------------------------")
            nodeAsArr.append(l1.val)

            l1.next = self.mergeTwoLists(l1.next, l2, round, nodeAsArr)
            print(f"return l1: {l1.val}")
            return l1
        else:
            l1_dis = None if l1 is None else l1.val
            l2_dis = None if l2.next is None else l2.next.val
            print(f"l2 is Lower, return mergeTwoLists(l1 : {l1_dis}, l2 next:{l2_dis})")
            print("------------------------------------")
            nodeAsArr.append(l2.val)

            l2.next = self.mergeTwoLists(l1, l2.next, round, nodeAsArr)
            print(f"return l2: {l2.val}")
            return l2

slt = Solution()

# Test Case
l1 = ListNode(1, ListNode(2, ListNode(3,  ListNode( 5,  ListNode(8, None)))))
l2 = ListNode(1, ListNode(3, ListNode(4,  ListNode( 5,  ListNode(6, ListNode(7, None))))))
slt.mergeTwoLists(l1,l2, 0, [])
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
