def linear_search(Value_to_find,numbers): #linear search algorithm
    for index,value_in_that_index in enumerate(numbers):
        if value_in_that_index==Value_to_find:
            return index
    return -1


def binary_search(Value_to_find,numbers):#binary search algorithm with out recursion
    left_index=0
    right_index=len(numbers)-1
    while left_index<=right_index:
        mid_index = (left_index + right_index) // 2
        if numbers[mid_index]==Value_to_find:
            return mid_index
        else:
            if numbers[mid_index]>Value_to_find:
                right_index=mid_index-1
            else:
                left_index=mid_index+1
    return -1


def recursive_binary_search(left_index,right_index,value_to_find,numbers):#binary search using recursion
    while left_index<=right_index:
        mid_index =(left_index + right_index) // 2
        if numbers[mid_index] == value_to_find:
            return mid_index
        elif numbers[mid_index] < value_to_find:
                return recursive_binary_search(mid_index+1, right_index, value_to_find, numbers)
        else:
            return recursive_binary_search(left_index,mid_index-1, value_to_find, numbers)
    return -1



def find_all_position_of_the_target_value(value_to_find,numbers):
    '''
here the  code segment is used to  find out all the positions of the given target value from a sorted list using binary search
    '''
    index=binary_search(value_to_find,numbers)
    indices=[index]
    i=index-1
    while i>=0:
        if numbers[i]==value_to_find:
            indices.append(i)
        else:
            break
        i-=1
    index=index+1
    while index<len(numbers):
        if numbers[index]==value_to_find:
            indices.append(index)
        else:
            break
        index+=1
    return sorted(indices)








# testing code is written below


numbers=[1,2,3,4,5,6,7,8,9,10,100,1111,122222,123333333]
value_to_find=100
print("The",value_to_find,"is locataed in index",linear_search(value_to_find,numbers))#will return index 10
value_to_find=122222
print("The",value_to_find,"is locataed in index",binary_search(value_to_find,numbers))#will return index 12
value_to_find=1222228888
print("The",value_to_find,"is locataed in index",linear_search(value_to_find,numbers))#will return index -1 as the value is not in the list
print("The",value_to_find,"is locataed in index",binary_search(value_to_find,numbers))#will return index -1 as the value is not in the list
value_to_find=9
left_index=0
right_index=len(numbers)-1
print("The",value_to_find,"is locataed in index",recursive_binary_search(left_index,right_index,value_to_find,numbers))#will return index 8
value_to_find=99999
print("The",value_to_find,"is locataed in index",recursive_binary_search(left_index,right_index,value_to_find,numbers))# will return index -1 as the value is not in the list

numbers=[1,2,3,4,5,6,7,8,10,10,10,10,11,11,24]
value_to_find=10

print("The",value_to_find,"is locataed in ",find_all_position_of_the_target_value(value_to_find,numbers),"positions")#will return the list of the positions where the value_to_find is located