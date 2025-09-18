# https://leetcode.com/problems/reverse-linked-list

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# O(n) time, O(1) space    

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            nextNode = curr.next
            curr.next = prev # reverses arrow
            prev = curr
            curr = nextNode
        
        return prev
        
        