# https://leetcode.com/problems/middle-of-the-linked-list

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        curr = head
        mid = head

        while curr:
            curr = curr.next
            i += 1
            if i % 2 == 0:
                mid = mid.next
        
        return mid