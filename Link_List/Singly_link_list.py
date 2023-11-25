class Node: #A class called Node is declared with two member function
    def __init__( self,data, next):
        self.data=data
        self.next=next
class Linklist:# a linklist class is created
    def __init__(self):
        self.head=None
    def insert_at_the_begining(self,data):#inserting value at the begining of the linklist
        node=Node(data,self.head)# a node is created
        self.head=node#Now head will point to  the new node

    def insert_at_the_end(self,data):#inserting value at the end of the link list
        if self.head==None: #check whether the linklist is empty or not.if empty then process will be followed same as 'inserting_at_the_begining
            node=Node(data,None)
            self.head=node

        else:
            itr=self.head
            while itr.next:#finding out the end node
                itr=itr.next
            itr.next=Node(data, None)

    def insert_values(self, data_list):#inserting values into linklist from list
        for data in data_list:
            self.insert_at_the_end(data)

    def insert_at_position(self, position, data):
        if position < 0 or position >= self.get_the_size():#check whether the given position is valid or not
            raise Exception("The position is not valid")
        elif self.head == None:#check whether the linklist is empty
            self.insert_at_the_begining(data)
        else:
            node = Node(data, None)#creating the node
            itr = self.head
            count = 0# will track the node number
            while itr:
                if count == position - 1:#cheeck whether the position is the previous position of our targeted position
                    node.next = itr.next
                    itr.next = node
                    break
                itr = itr.next
                count += 1
    def insert_after_value(self,the_data_aft_which_insert_done,the_value_to_be_inserted):#mainly insert a new  value after the given value
        itr=self.head
        node=Node(the_value_to_be_inserted,None)
        while itr:
            if itr.data==the_data_aft_which_insert_done:
                node.next=itr.next
                itr.next=node
                break
            itr=itr.next

    def delete_at_the_begining(self):#delete the first element of the link list
        if self.head==None:
            print("There is nothing to delete")
        else:
            itr=self.head
            self.head=itr.next

    def delete_at_position(self, pos):  # delete at the targeted position
        if self.head == None:  # check whether the list is empty or not
            print("There is nothing to delete")
        elif pos < 0 or pos >= self.get_the_size():  # validity check of the position
            raise Exception("The index is not valid at all")
        elif pos==0:
            self.delete_at_the_begining()
        else:
            itr = self.head
            count = 0
            while itr:  # finding out the previous node of the given position
                if count == pos - 1:
                    itr.next = itr.next.next
                    break
                itr = itr.next
                count += 1

    def delete_by_value(self,data):#delete that node whose value is matched with given value
        if self.head==None:#check whether the link list is empty or not
            print("There is nothing to delete")
        else:
            itr = self.head
            count = 0
            while itr:
                if itr.data == data:
                    break
                itr = itr.next
                count += 1
            current = 0
            if count == 0:  # if our given data matched with head node
                self.head = self.head.next
            else:
                itr = self.head
                while itr:  # finding out the previous node of the node that had our given data
                    if current == count - 1:
                        itr.next = itr.next.next
                        break
                    itr = itr.next
                    current += 1

    def delete_at_the_end(self):#delete the last node of the link list
        if self.head==None:
            print("There is nothing to delete")
        else:
            itr=self.head
            count=0
            while itr:
                count+=1
                itr=itr.next
            current=0
            itr=self.head
            while itr:
                current+=1
                if count-1==current:
                    itr.next=itr.next.next
                    break
                itr=itr.next


    def get_the_size(self):#get the size of the link  list
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count


    def print(self):#traversing the link  list
        lis = ""
        if self.head==None:#check whether the link list is empty
            print("The list is empty")
        else:
            itr=self.head
            while itr:
                lis+=str(itr.data)
                itr=itr.next
                if itr:
                    lis+="-->"
        print(lis)




lis=Linklist()
''' the below code is to check for insert node at the begining of link list method'''
lis.insert_at_the_begining(1)
lis.insert_at_the_begining('Mango')
lis.insert_at_the_begining(67.89)
lis.print()
''' the below code is to check for insert node at the end of link list method'''

lis.insert_at_the_end(34)
lis.insert_at_the_end('Banana')
lis.print()
''' the below code is to check for insert node from the list  to the  link list method'''

lis.insert_values([56,89.589,5895,'apple'])
lis.print()
''' the below code is to check for insert node at the given position  of  link list method'''

lis.insert_at_position(4,'40')
lis.print()

''' the below code is to check for insert node after given value  of  link list  method'''
lis.insert_after_value('Banana',10000)
lis.print()

''' the below code is to check for delete node at the begining  of  link list  method'''

lis.delete_at_the_begining()
lis.print()

'''the below code is to check for delete node at the begining  of  link list  method'''
lis.delete_at_position(0)
lis.print()
'''the below code is to check for delete node at the end  of  link list  method'''

lis.delete_at_the_end()
lis.print()

'''the below code is to check for delete_by_value  from the   link list  method'''

lis.delete_by_value('Banana')
lis.print()
print(lis.get_the_size())#mainly print the current size of the lik  list















































