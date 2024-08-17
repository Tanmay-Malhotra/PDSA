#O(logn) implementation of binary search to find min element in rotated array
def findMinimum(L):

    left = 0
    right =len(L) -1

    #no rotation
    if L[left]<L[right]:
        return L[left]
    
    while(left<=right):
        mid = (left +right)//2

        # check middle 
        if L[mid]>L[mid+1]:
            return L[mid+1]
    
        if L[mid]<L[mid-1]:
            return L[mid]
        
        if L[mid]>L[left]:
            left=mid+1
        else:
            right = mid-1 

arr=[4,5,6,7,8,9,1,2,3]
print(findMinimum(arr))
        

