def mergeSortedList(head1,head2):
    # retrun a new sorted linked 
    arr = []
    
    curr = head1
    temp = head2
    while (curr is not None):
        #print(curr.data)
        arr.append(curr.data)
        curr = curr.next
    #print(arr)
    while (temp is not None):
        arr.append(temp.data)
        temp=temp.next
    #print(arr)
    arr.sort()
    #print("Array",arr)
    
    head = Node(arr[0])
    curr1 = head
    #problem in linking
    # everytime, a node has to be initailised 
    
    for i in range(1,len(arr)):
        curr1.next =Node(arr[i])
        #print(type(curr1.next))
        curr1=curr1.next
        
    return head
        
        
    
    