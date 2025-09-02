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
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            temp.get_next()
        msg = " ".join(msg)
        return "LinkedList data (Head to Tail): " + msg


# shopping list
list1 = LinkedList()
items = ["Milk", "Sugar", "Salt", "Biscuit", "Apple Juice"]
for item in items:
    list1.add(item)

# Items to search
search_items = ["Milk", "Salt", "Biscuit", "Apple Juice", "Pomegranate", "Watermelon"]

# Search and print results
for item in search_items:
    node = list1.find_node(item)
    if node is not None:
        print(f"{item}: Found")
    else:
        print(f"{item}: Not Found")
