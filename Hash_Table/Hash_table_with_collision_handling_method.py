'''
all the code written below which can handle collision
'''
class Hash_Table: #defining a class called Hash with 2 member function
    def __init__(self):
        self.Max=1000
        self.arr=[[] for i in range(self.Max)]# declaring an array of list

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
        found=False
        arr_indx=self.get_the_hash(key)
        for indx in (self.arr[arr_indx]):
            if len(indx)==2 and indx[0]==key:
                ''' here we check if our key aready exist to the arr_index(or hash)
                             that we have gotten from the given key'''
                indx[1]=value
                found=True
                break
        if not found:
            self.arr[arr_indx].append([key,value])


    def __getitem__(self, key):


        ''' this  mainly returns the value of given key , that is stored in hash table.
        here we mainly retrive the hash of the given key by the 'get_the_hash_value' and and then return the value
         corresponding hash from the 'arr' '''
        arr_index = self.get_the_hash(key)

        for index in (self.arr[arr_index]):
            if  len(index)==2 and index[0] == key:
                return index[1]


    def __delitem__(self,key):
        '''
         this mainly  clear the value of the given key.
           here we mainly retrive the hash  of the given key by the 'get_the_hash_value' and
            then clear  the value of the corresponding hash from the 'arr' '''
        arr_index=self.get_the_hash(key)

        for index in (self.arr[arr_index]):
            if len(index)==2 and index[0] == key:
                index.clear()
                break


    def print_arr(self):#traversing the arr
        for element in self.arr:
            print(element)



''' test input for all the written methods above'''
dict=Hash_Table()#creatina an object hash

dict["Name"]='Roxy Sarkar' #mainly set the value into the hash table by taking the help of 'setitem'
dict['Country']='Bangladesh'
dict['Home_district']='Chittagong'
dict['Current_Location']='Dhaka'


print(dict['Name'])#will show the name 'Roxy Sarkar' by ta
print(dict['Country'])#will show the  country name 'Bnagladesh
print(dict['Home_district'])#will show the Home District name 'Chittagong'
print(dict['Current_Location'])#will show the current location  name 'Dhaka'

del dict['Current_Location']
print(dict['Current_Location'])#Now the value is None after delete
































