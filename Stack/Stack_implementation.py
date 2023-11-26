'''
Here below we implemented Stack with taking the help of Deque. It  mainly works on the idea of LIFO method
'''

from collections import deque #importing deque
class stack: #a class called stack is declared
    def __init__(self):
        self.container=deque()

    def push(self,item): # inserting element to the stack
        self.container.append(item)


    def pop(self): #deleting element from the stack following the LIFO method
        if self.is_empty():#checking whether the stack size is empty or not
            print(" There is nothing to delete")
        else:
            self.container.pop()


    def peek(self):#printing the element of the last inserted element in to the stack
        print(self.container[-1])


    def size(self):# returning the current size of stack
         print(len(self.container))


    def print(self):#traversing the current stack
        for items in self.container:
            print(items)

    def is_empty(self): #checking whether the stack is empty or not and return true if stack is empty otherwise alse
         return len(self.container)==0

'''
Below code is wriiten to test all the methods
'''

stck=stack()#creating a stack object named stck
'''
below code is written to check whether the method called 'push' is working correctly or not
'''
stck.push('https://www.google.com')
stck.push('https://en.wikipedia.org/')
stck.push('https://www.youtube.com/')
stck.push('https://www.tutorialspoint.com/')
stck.push('https://twitter.com/')

'''below code is written to check whether the method called 'pop' is working correctly or not'''
stck.pop()
stck.pop()
stck.print()

''' below code is written to check whether the method called 'peek' is working correctly or not'''

#stck.peek()

'''below code is written to check whether the method called 'size' is working correctly or not'''
stck.size()







