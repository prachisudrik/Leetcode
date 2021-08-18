from typing import Optional
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class SLinkedList:
   def __init__(self):
      self.headval = None

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        while(l1.headval != None or l2.headval != None):
            return l1.next


list1=SLinkedList()
list1.headval=ListNode('P')
e2=ListNode("R")
e3=ListNode("S")
list1.headval.next = e2
e2.next = e3
list2=SLinkedList()
list1.headval=ListNode('1')
e2=ListNode("2")
e3=ListNode("3")
list1.headval.next = e2
e2.next = e3

obj = Solution()
ans=obj.mergeTwoLists(list1,list2)
temp=ans.headval
while(temp):
    print(temp.val)
    temp = temp.next
