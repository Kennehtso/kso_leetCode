from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val         
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) :
        ans_cur = ans = ListNode(0)
        addOne = 0
        l1_cur = l1 
        l2_cur = l2
        COUNT = 0
        while l1_cur or l2_cur or addOne == 1:
            l1_cur_val = l1_cur.val if l1_cur else 0
            l2_cur_val = l2_cur.val if l2_cur else 0
            t_cur_val = l1_cur_val + l2_cur_val + addOne
            
            if t_cur_val >= 10:
                addOne = 1
                t_cur_val = t_cur_val -10
            else:
                addOne = 0
            
            l1_cur = l1_cur.next if l1_cur else None
            l2_cur = l2_cur.next if l2_cur else None
            
            if l1_cur  or l2_cur or addOne == 1:
                ans_cur.next = ListNode()
                
            ans_cur.val = t_cur_val
            ans_cur = ans_cur.next
            COUNT += 1
            print(ans)
        return ans
slt = Solution()    
# Test Case
slt.addTwoNumbers(
    l1 = ListNode(2, ListNode(4, ListNode(3,  None))),
    l2 = ListNode(5, ListNode(6, ListNode(4,   None)))
)

"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

Examle 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

"""
