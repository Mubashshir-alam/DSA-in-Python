"""This function provides the capacity, size and space left in the list.
You can invoke it to get the details of the list."""
import sys

def list_details(lst):
    #Number of elements that can be stored in the list
    print("Capacity:", (sys.getsizeof(lst)-64)//8)

    #Number of elements in the list
    print("Size:", len(lst))

    #Number of elements that can be accommodated in the space left
    print("Space Left:", ((sys.getsizeof(lst)-64) - len(lst*8))//8)

marias_lst=[]
print("Empty list created!!!")
print("List details:")
list_details(marias_lst)

# Apppending elements in list
marias_lst.append("Sugar")
print("Maria's list after adding Sugar:")
print(marias_lst)
print("List details:")
list_details(marias_lst)

marias_lst.append("Tea Bags")
marias_lst.append("Milk")
marias_lst.append("Biscuit")
print(marias_lst)
print("List details:")
list_details(marias_lst)

# Insrting elements in list
marias_lst.insert(1,"Salt")
print(marias_lst)
print("List details:")
list_details(marias_lst)

# Deleting elements in list
marias_lst.pop(1)
print(marias_lst)
print("List details:")
list_details(marias_lst)