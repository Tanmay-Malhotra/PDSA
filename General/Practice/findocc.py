#find occ.py to check the occurences of the number in a sorted string 

# use two functions 
# one to find the first occurence 
# one to find the last occurence 

def find_first(arr,key):
    left =0
    right = len(arr)-1

    fo = -1

    while (left<=right):
        mid = (left+right)//2
        if arr[mid]==key:
            fo = mid
            right = mid - 1 #continue searching left of the value to find the first occurence in a sorted arr

        if arr[mid]>key:
            right = mid-1
        else:
            left = mid + 1
    
    return fo

def find_last(arr,key):
    left =0
    right = len(arr)-1

    while(left <= right):
        mid = (left+right)//2
        if arr[mid]==key:
            lo =mid
            left = mid +1 # continue searching right of the value to find the last occurence in a sorted arr
        if arr[mid]>key:
            right = mid-1
        else :
            left = mid + 1
    

    return lo

def fin_occ(arr,key):
    fo = find_first(arr,key)
    if fo ==-1:
        return(-1)
    lo = find_last(arr,key)

    return (lo - fo +1)


L=[1,1,1,2,2,2,3,3,3,3,4,4,4,5]
print(fin_occ(L,3))

""" def find(arr,key):
    left = 0
    right =len(arr)-1

    mid = (left + right)//2
    count = 0
    while (left <= right):
        if key == mid:
            count+=1
            if arr[mid+1]==key :
                count+=1
            

        if key<mid:
            right=mid-1 """


