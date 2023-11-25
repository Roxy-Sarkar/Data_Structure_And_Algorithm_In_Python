'''
all the code written below which can't handle collision
'''
class Hash_Table: #defining a class called Hash with 2 member function
    def __init__(self):
        self.Max=1000
        self.arr=['' for i in range(self.Max)]

    def get_the_hash(self,key):#get the hash of the key
        sum=0
        if type(key)!="string":
            key=str(key)
        for char in key:
            sum+=ord(char) #'ord' mainly takes a character as input and convert it its equivalent  unicode
            return sum%self.Max

    def __setitem__(self, key, value):
        ''' Here we first get the hash  of the given key using
        'get_the_hash' function and then insert the given 'value' to the 'arr' and the index of the 'value' will
        be our gotten hash
          '''
        self.arr[self.get_the_hash(key)]=value

    def __getitem__(self, key):
        ''' this  mainly returns the value of given key , that is stored in hash table.
        here we mainly retrive the hash of the given key by the 'get_the_hash_value' and and then return the value
         corresponding hash from the 'arr' '''
        return self.arr[self.get_the_hash(key)]

    def __delitem__(self,key):
        ''' this mainly  clear the value of the given key.
           here we mainly retrive the hash of the given key by the 'get_the_hash_value' and and
            then clear  the value corresponding hash from the 'arr' '''
        self.arr[self.get_the_hash(key)]=''



''' test input for all the written methods above'''
dict=Hash_Table()#creatina an obect

dict["Name"]='Roxy Sarkar' #mainly set the value into the hash table by taking the help of 'setitem'
dict['country']='Bangladesh'
dict['Home district']='Chittagong'
dict['Current Location']='Dhaka'


'''
below we mainly retrive the value of the hash table by the  '__getitem__'
 '''

print(dict['Name'])#will show the name 'Roxy Sarkar' and
print(dict['country'])#will show the  country name 'Bnagladesh
print(dict['Home district'])#will show the Home District name 'Chittagong'
print(dict['Home district'])#will show the Home District name 'Chittagong'
print(dict['Current Location'])#will show the current location  name 'Dhaka'



del dict['Current Location']# deleting the value whose key is 'Current location' by taking the help of 'delitem'

print(dict['Current Location'])#will show empty as we deleted the item






