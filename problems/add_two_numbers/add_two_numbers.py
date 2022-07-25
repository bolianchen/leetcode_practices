# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """a solution of O(n), n is the larger length of the two input lists

        runtime faster than 99.31% of submissions
        memory usage less than 99.83% of submissions
        """

        sum_of_two = l1.val + l2.val
        carry = sum_of_two//10
        output = ListNode(sum_of_two%10)
        curr_node = output
        
        while l1.next or l2.next:
            if l1.next and l2.next:
                l1 = l1.next
                l2 = l2.next
                sum_of_two = l1.val + l2.val + carry
            elif l1.next:
                l1 = l1.next
                sum_of_two = l1.val + carry
            elif l2.next:
                l2 = l2.next
                sum_of_two = l2.val + carry
                
            carry = sum_of_two//10
            curr_node.next = ListNode(sum_of_two%10)
            curr_node = curr_node.next
        
        if carry > 0:
            curr_node.next = ListNode(carry)
            
        return output  
