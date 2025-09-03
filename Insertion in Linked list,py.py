class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data(), end=" ")
            temp = temp.get_next()
        print()

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

    def insert(self, data, data_before=None):
        new_node = Node(data)

        if self.__head is None:
            if data_before is None:
                self.__head = new_node
                self.__tail = new_node
            else:
                print("List is empty. Cannot insert.")
            return

        node_before = self.find_node(data_before)
        if node_before is None:
            print(f"Node with data '{data_before}' not found.")
            return

        new_node.set_next(node_before.get_next())
        node_before.set_next(new_node)

        if node_before == self.__tail:
            self.__tail = new_node

    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


# Example usage
list1 = LinkedList()
list1.add("Milk")
list1.add("Sugar")
list1.add("Tea")
list1.insert("Salt", "Sugar")
list1.display()

