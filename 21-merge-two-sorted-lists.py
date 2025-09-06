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

        while list1 or list2:
            curr.next = ListNode()
            curr = curr.next
            if list1 and list2 and list1.val <= list2.val:
                curr.val = list1.val
                list1 = list1.next
            elif list1 and list2 and list1.val > list2.val:
                curr.val = list2.val
                list2 = list2.next
            elif list1 and not list2:
                curr.val = list1.val
                list1 = list1.next
            elif list2 and not list1:
                curr.val = list2.val
                list2 = list2.next

        return ans.next
    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()

        def dp(L1,L2,curr):
            if L1 or L2:
                curr.next = ListNode()
                curr = curr.next
            else:
                return
            
            if L1 and L2 and L1.val <= L2.val:
                curr.val = L1.val
                dp(L1.next,L2,curr)
            elif L1 and L2 and L1.val >= L2.val:
                curr.val = L2.val
                dp(L1,L2.next,curr)
            elif L1 and not L2:
                curr.val = L1.val
                dp(L1.next,L2,curr)
            elif L2 and not L1:
                curr.val = L2.val
                dp(L1,L2.next,curr)
        dp(list1,list2,ans)

        return ans.next
