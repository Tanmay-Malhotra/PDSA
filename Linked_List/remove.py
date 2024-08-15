# leet code 203 remove elements 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #given a value, we have to remove all the nodes containing that value from the list 

        #dummy node 

        dummy =ListNode()
        dummy.next = head
        curr=dummy

        while(curr.next is not None):
            #case when the value is at the head              
                
            #case when the value is not at the head
            if curr.next.val == val:
                #connect the heads 
                curr.next = curr.next.next
            else:
                curr = curr.next
        #returning dummy.next also ensure if the head is None; it gives None output
        return dummy.next
        