class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'{self.data} --> {self.next}'

class LinkedList:
    def __init__(self, head):
        self.head = head

    def __repr__(self):
        next_node = self.head.next
        print(f'{self.head.data} --> ', end="")
        while next_node is not None:
            print(f'{next_node.data} --> ', end="")
            next_node = next_node.next
        print("None", end="")
        return ""

    def insert_front(self, data):
        original_head = self.head
        self.head = Node(data=data, next=original_head)

    def insert_end(self, data):
        current = self.head # Current position of the pointer is at head
        while current.next is not None:
            current = current.next
        current.next = Node(data=data)

    def insert_between(self, position, data):
        counter = 0
        current = self.head # Current position of the pointer is at head
        if position == 0:
            self.insert_front(data=data)
            return
        try:
            while counter != position-1:
                current = current.next
                counter += 1
            next_node = current.next
            current.next = Node(data=data, next=next_node)
        except AttributeError:
            print("Invalid Insert Position Value")
            
    def remove_node(self, position):
        counter = 0
        current = self.head # Current position of the pointer is at head
        if position == 0:
            next_node = self.head.next
            self.head = next_node
            del next_node
            return
        try:
            while counter != position-1:
                current = current.next
                counter += 1
            next_node = current.next.next
            current.next = next_node
            del next_node
        except AttributeError:
            print("Invalid Remove Position Value")


if __name__ == "__main__":
    head_node = Node(data=1) # Initialize a Node
    linked_list = LinkedList(head=head_node) # Set that Node as the head node of the linked list
    for i in range(20,100,10):
        linked_list.insert_end(i)
    linked_list.insert_front(10)
    linked_list.insert_between(position=3, data=454)
    print(linked_list)
    linked_list.remove_node(1)
    print(linked_list)