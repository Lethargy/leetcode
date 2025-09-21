# https://leetcode.com/problems/remove-duplicates-from-sorted-list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        prev = head
        curr = head

        while curr:
            while curr and curr.val == prev.val:
                curr = curr.next
            prev.next = curr
            prev = curr
        
        return head

