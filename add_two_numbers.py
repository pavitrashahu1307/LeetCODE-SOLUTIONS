# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy head node to start building our new list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Loop continues as long as there are digits left in l1 OR l2, 
        # or if there is still a remaining carry value to add at the end
        while l1 or l2 or carry:
            # Get the value from the current nodes (use 0 if a list ran out of digits)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the total sum for this column
            total_sum = val1 + val2 + carry
            
            # Update the carry for the next column (e.g., 12 // 10 = 1)
            carry = total_sum // 10
            
            # Create a new node with the single digit (e.g., 12 % 10 = 2)
            current.next = ListNode(total_sum % 10)
            
            # Move our result pointer forward
            current = current.next
            
            # Move l1 and l2 pointers forward if they have more nodes
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        # Return the actual head of the new list (skipping our dummy 0)
        return dummy_head.next
