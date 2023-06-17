class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    head: Node = None
    tail: Node = None
    def add_node(self, data):
        new_node = Node(data)
        if(self.head is None):
            self.head = new_node
            self.tail = self.head
            return
        self.tail.next = new_node
        self.tail = new_node
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
    
    def delete_node(self,data):
        temp = self.head
        if(temp.data == data):
            self.head = self.head.next
            return
        prev = temp
        while temp is not None:
            if(temp.data == data):
                prev.next = temp.next
                if(temp == self.tail):
                    self.tail = prev
                return
            prev = temp
            temp = temp.next
                
def main():
    list = SinglyLinkedList()
    list.add_node(3)
    list.add_node(5)
    list.add_node(6)
    list.delete_node(5)
    list.display()
    list.display()
    


if __name__ == "__main__":
    main()
