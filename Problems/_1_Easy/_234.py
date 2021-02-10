from typing import List

class ListNode:
    def __init__(self, val=0, next =None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        checkList = []
        while head:
            checkList.append(head.val)
            head = head.next
        return checkList == checkList[::-1]
            
        
#1 , (2, (3, (4, (5, (4, (3, (2, (1, None))))))))
slt = Solution()
slt.isPalindrome(ListNode(1, ListNode(2, ListNode(3, ListNode(2,  ListNode(1, None))))))

"""
234. Palindrome Linked List
   Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
    Could you do it in O(n) time and O(1) space?
"""
