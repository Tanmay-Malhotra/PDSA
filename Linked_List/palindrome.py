#Leet code 234
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        arr =[]
        while(curr is not None):
            arr.append(curr.val)
            curr = curr.next 
        if arr == arr[::-1]:
            return True
        else: 
            return False