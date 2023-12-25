
class BinarySearchTree():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):# below code is for new distinct child append
        if self.data==data.data:
            return

        elif self.data>data.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=data

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=data


    def preorder_print_tree(self):#here we print the tree using 'pre order' format.Means root-->left child-->right child
        elements=[]
        elements.append(self.data)
        if self.left:
            elements+=self.left.preorder_print_tree()
        if self.right:
            elements+=self.right.preorder_print_tree()
        return elements



    def inorder_print_tree(self):#here we  print the tree in 'in order' format.Means left child-->root-->right child
        elements=[]
        if self.left:
            elements+=self.left.inorder_print_tree()
        elements.append(self.data)
        if self.right:
            elements+=self.right.inorder_print_tree()
        return elements




    def postorder_print_tree(self):#here we  print the tree in 'post order' format.Means left child-->right child-->root
        elements=[]
        if self.left:
            elements+=self.left.postorder_print_tree()
        if self.right:
            elements+=self.right.postorder_print_tree()
        elements.append(self.data)
        return elements

    def sum_elements(self):  # here we mainly sum all the elements of the tree
        sum = 0
        if self.left:
            sum += self.left.sum_elements()
        sum += self.data
        if self.right:
            sum += self.right.sum_elements()
        return sum

    def find_min_element(self):  # here we mainly find out the minimum element of the tree

        if self.left is None:
            return self.data
        return self.left.find_min_element()

    def find_max_element(self):# here we mainly find out the maximum element of the tree
       if self.right is None:
           return self.data

       return self.right.find_max_element()



    def delete_element(self,target_value): #delete a node
        if self.data<target_value:
            if self.right:
                self.right=self.right.delete_element(target_value)
        elif self.data>target_value:
            if self.left:
                self.left = self.left.delete_element(target_value)
        else:
            if self.left is None  and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min_value=self.right.find_min_element()
                self.data=min_value
                self.right=self.right.delete_element(min_value)
        return self


    def search_element(self,target_value): # search a node
        if self.data==target_value:
            return True
        elif self.data>target_value:
            if self.left:
                return self.left.search_element(target_value)
            else:
                return False
        else:
            if self.right:
                return self.right.search_element(target_value)
            else:
                return False

def build_tree(elements):#mainly we build a tree with the elements of the list [20,10,9,12,8,11,13,30,35,60]
    root=BinarySearchTree(elements[0])
    for element in range(1,len(elements)):
        root.add_child(BinarySearchTree(elements[element]))
    return root


if __name__=='__main__':
    root = build_tree([20, 10, 9, 12, 8, 11, 13, 30, 35, 60])
    print(root.preorder_print_tree())  # [20, 10, 9, 8, 12, 11, 13, 30, 35, 60]
    print(root.inorder_print_tree())  # [8,9,10,11,12,13,20,30,35,60]
    print(root.postorder_print_tree())  # [8,9,11,13,12,10,60,35,30,20]
    print(root.sum_elements())  # 208
    print(root.find_min_element())  # 8
    print(root.find_max_element())  # 60
    print(root.search_element(11))  #return True as this element is in the tree
    print(root.search_element(10000))  # Return False as this element is not in the tree
    root.delete_element(30)
    print("After deleting '30', The tree elements in 'in order' format: ",root.inorder_print_tree())#[8,9,10,11,12,13,20,35,60]





