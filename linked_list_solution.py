class DoubleLinkedList:
    #Creates a new node
    class node:
        def __init__(self, value):
            self.value = value
            self.previous = None
            self.next = None
            
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        new_node = DoubleLinkedList.node(value)
        if self.head is None:
            self.head = new_node      #Since this is the only node it is both the head and tail. 
            self.tail = new_node
        else:
            self.head.previous = new_node # Connect the previous head to the new node
            new_node.next = self.head # Connect new node to the previous head
            self.head = new_node      # Makes the new node the head
            
    def insertIntoAfter(self, insertAfter, new_value):
        current_node = self.head
        
        while current_node is not None:
            if current_node.value == insertAfter:
                new_node = DoubleLinkedList.node(new_value)
                new_node.previous = current_node       # Connects the new node to the node containing value
                new_node.next = current_node.next  # Connects the new node to the node after value
                current_node.next = new_node      # Connects the the node containing value to the new node
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
            if current_node.previous is not None:
                prev = current_node.previous.value
            else:
                prev = None
            if current_node.next is not None:
                nex = current_node.next.value
            else:
                nex = None
            # node_values.append(current_node)
            string += f"[{prev}[{current_node.value}]{nex}],"
            current_node = current_node.next
        return string

colors_list = DoubleLinkedList()
colors_list.insert("Red")
colors_list.insert("Blue")
colors_list.insert("Yellow")
colors_list.insert("Green")
colors_list.insert("Purple")
colors_list.insertIntoAfter("Yellow","Cyan")
colors_list.insertIntoAfter("Red","Black")
print(colors_list)