from typing import List

class ListNode:
    def __init__(self, val=0, next =None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            # Not just move slow forward
            # record the other half
            tmp = rev
            rev = slow
            slow = slow.next
            rev.next = tmp
        #print(rev)  # reverse from the first half
        # load remain part check if same as "rev"
        if fast: slow = slow.next # this one is to force len of odd numbers linklist to start from mid + 1
        #print(slow) # remain part
        #print(fast) # fast is end
        # Check remain part
        while rev and rev.val == slow.val:
            # IF NOT SAME, RETURN False
            rev = rev.next
            slow = slow.next
        return not slow # if remain run to None means is empty, else which means that sth remain
            
        
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
