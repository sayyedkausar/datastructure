class Node: 

    def __init__ (self, element, next = None ):
        self.element = element
        self.next = next
        self.previous = None
    def display(self):
        print(self.element)

class LinkedList:
        
    def __init__(self):
        self.head = None
        self.size = 0
             
    def len(self):
        return self.size
    
    def get_head(self):
        return self.head
    
    
    def is_empty(self):
        return self.size == 0    
    
    def add_head(self,e):
        #temp = self.head 
        self.head = Node(e)
        #self.head.next = temp
        self.size += 1 
        
   

my_list = LinkedList()
order = int(input('Enter the order for polynomial : '))
my_list.add_head(Node(int(input(f"Enter coefficient for power {order} : "))))
for i in reversed(range(order)):
    my_list.add_tail(int(input(f"Enter coefficient for power {i} : ")))
    
my_list2 = LinkedList()
my_list2.add_head(Node(int(input(f"Enter coefficient for power {order} : "))))
for i in reversed(range(order)):
    my_list2.add_tail(int(input(f"Enter coefficient for power {i} : ")))
    
for i in range(order + 1):
    print(my_list.get_node_at(i).element + my_list2.get_node_at(i).element)
