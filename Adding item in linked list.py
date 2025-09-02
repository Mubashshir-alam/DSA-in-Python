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
        current = self.__head
        while current is not None:
            print(current.get_data())
            current = current.get_next()

    def find_node(self, data):
        current = self.__head
        while current is not None:
            if current.get_data() == data:
                return current
            current = current.get_next()
        return None

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp = self.__head
        msg = []
        while (temp is not None):
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg

# Create Maria's shopping list
shopping_list = LinkedList()
shopping_list.add("Milk")
shopping_list.add("Salt")
shopping_list.add("Biscuit")
shopping_list.add("Apple Juice")

print("\nItems in Maria's list:")
shopping_list.display()

print(shopping_list)

# Items to search
items_to_search = ["Milk", "Salt", "Biscuit", "Apple Juice", "Pomegranate", "Watermelon"]

# Search and print results
for item in items_to_search:
    result = shopping_list.find_node(item)
    if result:
        print(f"{item} is present in the list.")
    else:
        print(f"{item} is NOT present in the list.")
