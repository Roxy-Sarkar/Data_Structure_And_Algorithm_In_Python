class TreeNode:#a node class
    def __init__(self, data):
        self.data = data
        self.children = []#store the child of the current parent node in the list
        self.parent = None


    def append_child(self, child):# child node insertion to the tree
        child.parent = self
        self.children.append(child)


    def print_tree(self):#traversal of the tree
        print(' '*self.get_level()*3+'|--'+self.data)
        for child in self.children:
            child.print_tree()

    def get_level(self):#get the level of the contructed tree
        parent=self.parent
        level=0
        while parent:
            level+=1
            parent=parent.parent
        return level




'''
 Below code is written for testing purpose
 
 
  below here we mainly build our root node at first which is called 'Electronics. Then we created another node which is 
  'laptop' and three child of this 'laptop' node by 'append_child' method . After that we also apply same for the 'TV' and 
  'Smart_phone' and also append their child by using same method. Then we appned these 'Laptop','TV' and 'smart_phone'node to the root
   Then we traverse the tree


'''
def Build_Elctronics_Item_List():
    root=TreeNode('Electronics')


    laptop=TreeNode('Laptop')#
    laptop.append_child(TreeNode('Mac'))
    laptop.append_child(TreeNode('Dell'))
    laptop.append_child(TreeNode('Lenovo'))

    Cell_Phone=TreeNode('Smart_Phone')
    Cell_Phone.append_child(TreeNode('Iphone'))
    Cell_Phone.append_child(TreeNode('Samsung'))
    Cell_Phone.append_child(TreeNode('Walton'))

    TV=TreeNode('TV')
    TV.append_child(TreeNode('Samsung'))
    TV.append_child(TreeNode('Google'))

    root.append_child(laptop)
    root.append_child(Cell_Phone)
    root.append_child(TV)
    root.print_tree()
Build_Elctronics_Item_List()










