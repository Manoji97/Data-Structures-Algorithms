class node_BT:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Binary_tree:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        if self.root is None:
            self.root = node_BT(data)
        else:
            self.insert_crct(data,self.root)
    
    def insert_crct(self,new_data, node):
        if new_data < node.data:
            if node.left:
                self.insert_crct(new_data,node.left)
            else:
                node.left = node_BT(new_data)
        elif new_data > node.data:
            if node.right:
                self.insert_crct(new_data,node.right)
            else:
                node.right = node_BT(new_data)
    
    def get_min(self):
        if self.root:
            node = self.get_min_val(self.root)
            return node.data
            
    def get_min_val(self,node):
        if node.left:
            node = self.get_min_val(node.left)
        return node
            
    def get_max(self):
        if self.root:
            node = self.get_max_val(self.root)
            return node.data
    def get_max_val(self,node):
        if node.right:
            node = self.get_max_val(node.right)
        return node
    
    def print_all(self):
        if self.root:
            self.print_all_val(self.root)
            
    def print_all_val(self,node):
        if node.left:
            self.print_all_val(node.left)
        print(node.data)
        if node.right:
            self.print_all_val(node.right)
            
    def delete_element(self,data):
        if self.root:
            self.root = self.delete_val(data,self.root)
    
    def delete_val(self,data,node):
        if not node:
            return node
        if node.data > data:
            node.left = self.delete_val(data,node.left)
        elif node.data < data:
            node.right = self.delete_val(data,node.right)
        else:
            if not node.left and not node.right:
                del(node)
                return None
            
            if not node.right:
                temp_node = node.left
                del(node)
                return temp_node
            elif not node.left:
                temp_node = node.right
                del(node)
                return temp_node
            
            pre_node_data = self.get_precedor(node.left)
            node.data = pre_node_data
            node.left = self.delete_val(pre_node_data,node.left)
        return node
                
    def get_precedor(self,node):
        if node.right:
            return self.get_precedor(node.right)
        return node.data
            
            
   
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
                