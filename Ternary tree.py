class Node:
    def __init__(self,character):
        self.character = character
        self.left = None
        self.middle = None
        self.right = None
        self.value = 0

class TRT:
    def __init__(self):
        self.root = None
    
    def put(self,key,value):
        self.root = self.put_item(self.root,key,value,0)
        
    def put_item(self,node,key,value,index):
        c = key[index]
        
        if node == None:
            node = Node(c)
        
        if c < node.character:
            node.left = self.put_item(node.left,key,value,index)
        elif c > node.character:
            node.right = self.put_item(node.right,key,value,index)
        elif index < len(key)-1:
            node.middle = self.put_item(node.middle,key,value,index +1)
        else:
            node.value = value
        return node
    
    def get(self,key):
        if self.get_item(self.root,key,0) == None:
            return -1
        else:
            self.get_item(self.root,key,0)
    
    def get_item(self,node,key,index):
        c = key[index]
        if node == None:
            return None
        
        if c < node.character:
            val = self.get_item(node.left,key,index)
        elif c > node.character:
            val = self.get_item(node.right,key,index)
        elif index < len(key)-1:
            val = self.get_item(node.middle,key,index+1)
        else:
            val = node.value
        return val
    
    
t = TRT()


