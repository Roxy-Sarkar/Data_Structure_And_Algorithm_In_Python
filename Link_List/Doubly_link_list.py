class Node:
    '''
    Building Block of 'Node'
    '''
    def __init__(self,data,previous,next):
        '''
        there are three member functions(field) in the node for doubly link list which is 'data', address of the previous node
        which is called 'previous' here and the the other is the next address of the next node which is called
        'next' here'''

        self.data=data
        self.previous=previous
        self.next=next


class Linklist: #Creating Link_list

    def __init__(self):
        self.head=None

    def insert_at_the_begining(self,data): # Inserting element at the begining of the link list


        if self.head==None:
            ''' if there is no element prior , then the element 
            which is going to be inserted will be the first element '''
            node = Node(data, None, None)
            self.head = node

        else:
            node=Node(data,None,self.head)
            itr=self.head
            self.head = node  # Now head will be the new node
            itr.previous = self.head #The node that was head previous,now becoming the second node




    def insert_at_the_end(self,data):
        if self.head==None: #if there is no node still, then the inserted element is going to be our first element of the link list
            node=Node(data,None,None)
            self.head=node
        else:
            itr=self.head
            while itr.next: #we are checking our end node
                itr=itr.next
            node=Node(data,itr,None)# The new node has been created for insertion purpose
            itr.next=node#node address updated


    def insert_at_targeted_position(self,position,data):
        if position<0 or position>=self.get_the_link_list_size():#if the position is negative or out of the bound then exception will raise
            raise Exception("The position is not valid")
        elif self.head==None: #when the list is currently empty
            node=Node(data,None,None)#node creation
            self.head=node
        elif position == 0: #when we want to add the node at the begining of the link_list
            node = Node(data, None,self.head)
            ''' previous and next address of the corresponding nodes are updated below'''
            self.head.previous=node
            self.head=node
        else:
            node=Node(data,None,None)
            coun=0
            itr=self.head
            while itr: # basically we are trying to find out the previous positon of our targeted positon
                if coun==position-1:
                    node.previous=itr
                    node.next=itr.next
                    itr.next=node
                    break
                coun+=1
                itr=itr.next



    def insert_values(self,data_list):#inserted value in to the link_list from a python "list"
        for data in data_list:
            self.insert_at_the_end(data)

    def delete_at_the_begining(self):
        if self.head==None: #The link list is empty
            print("There is nothing to delete")
        else:
            self.head=self.head.next
            self.head.previous=None


    def delete_at_the_end(self):
        if self.head==None:#The link list is empty
            print("There is nothing to delete")
        else:
            itr=self.head
            while itr.next:#finding out the last element for delete purpose
                itr=itr.next
            itr.previous.next=None
            itr.previous=None

    def delete_at_the_given_position(self,position):
        if position<0 or position>=self.get_the_link_list_size():#if the position is out of bound or negative then the exception message will show
            raise Exception("The given position is not valid")
        elif position==0: # the list is empty currently
            self.delete_at_the_begining()
        elif position==self.get_the_link_list_size()-1:
            self.delete_at_the_end()
        else:
            itr=self.head
            current=0
            while itr: #finding out the position before the given position
                if current==position-1:
                    temp=itr.next
                    itr.next=temp.next
                    temp.next.previous=itr
                    break
                itr=itr.next
                current+=1



    def get_the_link_list_size(self): # return the size of the link list
        coun=0
        itr=self.head
        while itr:
            coun+=1
            itr=itr.next
        return coun


    def print(self): #The block  of the created link list traversal

        if self.head==None: #if there is no element in the list , the list must be empty

            print("There is nothing to print")
        itr=self.head
        link_list=""
        while itr:  # traversing the whole link_list upto end

            link_list+=str(itr.data)
            itr=itr.next
            if itr:
                link_list+="-->"

        print(link_list)


''' Testing input for the all the written methods above, are given below '''
lis=Linklist()
lis.insert_at_the_begining(1)
lis.insert_at_the_begining(2)
lis.insert_at_the_begining(3)
print("The list after insertion at the begining is :")
lis.print()
'''   '''
lis.insert_at_the_end(8)
lis.insert_at_the_end(10)
print("The list after insertion the element is: ")
lis.print()
'''   '''
lis.insert_at_targeted_position(1,1000)
print("The list after insertion to the given position is: ")
lis.print()
'''   '''
lis.insert_values([1000,2000000,3000000])
print("The list after insert the value from the  list is: ")
lis.print()
'''    '''
lis.delete_at_the_begining()
print("The list after delete the  begining element is: ")
lis.print()
'''       '''
lis.delete_at_the_end()
print("The list after delete last element is: ")
lis.print()
'''   '''
lis.delete_at_the_given_position(6)
print("The list after delete the given position element is: ")
lis.print()
''''  '''
print("The size of the link list  is: ",lis.get_the_link_list_size())














