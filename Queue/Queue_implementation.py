'''
Here below we implemented Queue with taking the help of Deque. It  mainly works on the idea of FIFO method
'''
from collections import deque


class queue():
    def __init__(self):
        self.buffer=deque()


    def enqueue(self,item):#inserting the element to the queue
        self.buffer.appendleft(item)

    def dequeue(self):#poping the element using the idea of FIRST INN FIRST OUT method
        if self.is_empty():#check whether the queue is empty or not
            print('There is nothing to dequeue')
        else:
            self.buffer.pop()

    def size(self):# mainly returns the length of the current queue
        return len(self.buffer)

    def is_empty(self):#mainly checks whether the queue is empty  or not. If queue is empty  then return true otherwise false
        return len(self.buffer)==0

    def print(self):  # traversing the current queue
        for items in self.buffer:
            print(items)


'''
Below code is wriiten to test all the methods
'''
qu=queue()#creating a queue object named qu

'''
below code is written to check whether the method called 'enqueue' is working correctly or not
'''
qu.enqueue({'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10})
qu.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})
qu.print()

'''
below code is written to check whether the method called 'dequeue' is working correctly or not
'''

qu.dequeue()

qu.print()

'''below code is written to check whether the method called 'is_empty' is working correctly or not'''
print(qu.is_empty())#will return False as the queue is not empty

'''below code is written to check whether the method called 'size' is working correctly or not'''
print(qu.size())



