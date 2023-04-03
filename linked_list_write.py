class SingleLinkedList:
    #Creates a new node
    class node:
        def __init__(self, value):
            self.value = value
            self.next = None
            
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = SingleLinkedList.node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head # Connect new node to the previous head
            self.head.prev = new_node # Connect the previous head to the new node
            self.head = new_node   
            
    def insertIntoAfter(self, insertAfter, new_value):
        current_node = self.head
        
        while current_node is not None:
            if current_node.value == insertAfter:
                new_node = SingleLinkedList.node(new_value)
                new_node.next = current_node.next
                current_node.next = new_node
                return 
                
            current_node = current_node.next
                
    def search(self, value):
        current_node = self.head
        while current_node is not None:
            if value == current_node.value:
                return True
            else:
                current_node = current_node.next
        return False

    def __str__(self):
        node_values = []
        current_node = self.head
        string = "Linked List Values:"
        while current_node is not None:
            node_values.append(current_node)
            string += f"{current_node.value},"
            current_node = current_node.next
        return string

colors_list = SingleLinkedList()
colors_list.insert("Purple")
colors_list.insert("Green")
colors_list.insert("Yellow")
colors_list.insert("Blue")
colors_list.insert("Red")
colors_list.insertIntoAfter("Yellow","Cyan")
colors_list.insertIntoAfter("Red","Black")
print(colors_list)