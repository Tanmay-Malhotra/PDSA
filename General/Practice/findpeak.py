# find peak using binary search 
def Findpeak(arr):
    
    left = 0
    right = len(arr) - 1
    #o(logn) implies division 
    # corner cases
    
    high = arr[left]
   
    
    while(left<=right):
        mid = (left+right)//2

        # not checking for mid 
        
        if (arr[mid]>high):
            high = arr[mid]
            left = mid+1
        else:
            right = mid -1
            if arr[mid]>high:
                high = arr[mid]

    return high
        
        
    