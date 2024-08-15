class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None 
        
# traverse the linked list, make an array with the values, check if the current value is in the array, delete node 

class LinkedList:

    # Function to initialize head
    # head is a pointer / reference to the first node of the linked list
    def __init__(self):
        self.head= None

    def push(self, new_data):
        new_node = Node(new_data)
        # changing the head pointer 
        new_node.next = self.head
        self.head = new_node

    # function to delete a node in linked list given a head and key
    def deletenode(self,key):
        temp = self.head
        # temp is used to traverse the list 

        # if head node holds the key to be deleted 
        if( temp is not None):
            if(temp.data == key):
                #head is updated to point to the next node
                self.head=temp.next
                #current node(temp) is set to none to delete from memory
                temp = None
                return 
           
        # search for the key to be deleted , keep track of the previous node as we need to change prev.next
        while(temp.data is not None):
            # stop the loop if key is found
            if temp.data == key:
                break
            # this is traversal happening 
            prev = temp
            temp = temp.next

        # if key is not found
        if(temp == None):
            return 
        
        # this is the deletion part
        prev.next = temp.next  #connect the prev node with next node 
        temp = None  #delete the current node 


    def printList(self):
        curr = self.head
        #while curr        
        while (curr is not None) :
            print(curr.data, end = ' ')
            curr = curr.next

    def removeduplicates(self):
        temp = self.head

        if temp is None:
            return 
        
        # we want to remove duplicates from a sorted linked list 
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next
                #changing walue of temp.next
                temp.next= None
                temp.next= new
            else:
                temp = temp.next 

llist = LinkedList() 
 
llist.push(20) 
llist.push(13) 
llist.push(13)
llist.push(11)
llist.push(11)
llist.push(11)
print ("Created Linked List: ")
llist.printList()

print()
print("Linked List after removing", 
      "duplicate elements:")
llist.removeduplicates()
llist.printList()




            


