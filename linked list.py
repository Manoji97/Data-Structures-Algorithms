
class node:
    def __init__(self,data):
        self.data = data
        self.nextnode = None

class Linked_list:
    def __init__(self):
        self.head = None
        self.size = 0
    def show_head(self):
        return self.head.data
    
    def add_first(self,data):
        self.size += 1
        new_node = node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.nextnode = self.head
            self.head = new_node
    
    def add_end(self,data):
        self.size += 1
        new_node = node(data)
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.nextnode != None:
                current_node = current_node.nextnode
            current_node.nextnode = new_node
        
    def show_size(self):
        return self.size
    
    def show(self):
        if self.head == None:
            return
        current_node = self.head
        while current_node != None:
            print(current_node.data,current_node.nextnode)
            current_node = current_node.nextnode
    
    def remove(self,data_remove):
        if self.head == None:
            return
        
        current_node = self.head
        previous_node = None
        while current_node.data != data_remove:
            if current_node.nextnode is not None:
                previous_node = current_node
                current_node = current_node.nextnode
            else:
                return 
            
        self.size -= 1
        if previous_node == None:
            self.head = current_node.nextnode
        else:
            previous_node.nextnode = current_node.nextnode




