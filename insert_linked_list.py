def insert(self, data, position):
    new_node = Node(data)
    current = self.head

    if position == 0:
        new_node.next = self.head
        self.head = new_node
    else:
        while position > 1:
            current = current.next
            position -= 1
        next = current.next
        current.next = new_node
        current.next.next = next

        new_node = next
