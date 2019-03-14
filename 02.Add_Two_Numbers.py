# Add Two Numbers

"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    	dummy = curr = ListNode(0)
    	carry = 0
    	while l1 or l2 or carry:
    		if l1:
    			carry += l1.val
    			l1 = l1.next
    		if l2:
    			carry += l2.val
    			l2 = l2.next
    		curr.next = ListNode(carry%10)
    		curr = curr.next
    		carry = carry // 10
    	return dummy.next