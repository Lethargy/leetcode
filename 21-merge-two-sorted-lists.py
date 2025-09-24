# https://leetcode.com/problems/merge-two-sorted-lists

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# using while loop

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        curr = ans

        while list1 and list2:
            curr.next = ListNode()
            curr = curr.next
            if list1.val <= list2.val:
                curr.val = list1.val
                list1 = list1.next
            elif list2.val < list1.val:
                curr.val = list2.val
                list2 = list2.next
        
        while list1:
            curr.next = ListNode()
            curr = curr.next
            curr.val = list1.val
            list1 = list1.next

        while list2:
            curr.next = ListNode()
            curr = curr.next
            curr.val = list2.val
            list2 = list2.next

        return ans.next
        



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        elif list1.val > list2.val:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        


