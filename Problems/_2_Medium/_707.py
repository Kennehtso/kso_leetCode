from typing import List
class Solution:
    class Node:
        def __init__(self, val = 0):
            self.val = val
            self.next = None
        
    class MyLinkedList:

        def __init__(self):
            self.head = None
            self.size = 0
            
        def viewNode(self,action):
            print("Action : %s"%(action))
            cur = self.head
            chk = []
            while cur:
                chk.append(cur.val)
                cur = cur.next
            print("Node Status : ", chk)
            print("head: ", self.head.val if self.head else None)
            print("size: ",self.size)
            print("----------")
            
        def get(self, index: int) -> int:
            #print("get : %s"%(index))
            if index >= self.size:
                #print("index >= self.size:")
                return -1
            
            if not self.head:
                #print("Not Head")
                return -1
            
            cur = self.head
            for i in range(index):
                cur = cur.next
                
            #self.viewNode("get")
            return cur.val if cur else -1
            

        def addAtHead(self, val: int) -> None:
            self.addAtIndex(0, val)

        def addAtTail(self, val: int) -> None:
            self.addAtIndex(self.size, val)

        def addAtIndex(self, index: int, val: int) -> None:
            if index > self.size:
                #print("addAtIndex index > self.size")
                return
            
            node = Node(val)
            if index == 0 :
                node.next = self.head
                self.head = node
            else:
                cur = self.head
                for i in range(index - 1):
                    cur = cur.next
                node.next = cur.next
                cur.next = node
            self.size += 1
            #self.viewNode("addAtIndex")

        def deleteAtIndex(self, index: int) -> None:
            if index > self.size:
                return 
            if index == 0:
                if self.head:
                    self.head = self.head.next
                    self.size -= 1
            else:
                cur = self.head
                for i in range(index - 1):
                    cur = cur.next
                if cur.next:
                    cur.next = cur.next.next
                    self.size -= 1
            #self.viewNode("deleteAtIndex")



slt = Solution()    

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
"""
707. Design Linked List

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:
    1. MyLinkedList() Initializes the MyLinkedList object.
    2. int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
    3. void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
    4. void addAtTail(int val) Append a node of value val as the last element of the linked list.
    5. void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
    6. void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

 

Example 1:
    Input
        ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
        [[], [1], [3], [1, 2], [1], [1], [1]]
        Output
        [null, null, null, null, 2, null, 3]

    Explanation
        MyLinkedList myLinkedList = new MyLinkedList();
        myLinkedList.addAtHead(1);
        myLinkedList.addAtTail(3);
        myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
        myLinkedList.get(1);              // return 2
        myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
        myLinkedList.get(1);              // return 3

    Constraints:
        0 <= index, val <= 1000
        Please do not use the built-in LinkedList library.
        At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.

"""