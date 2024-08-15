def removeDuplicate(head):
    curr = head
    while (curr.next is not None): # we cannot use curr.next.data because 
        if curr.data == curr.next.data:
            new = curr.next.next
            curr.next = None
            curr.next = new
        else:
            curr = curr.next