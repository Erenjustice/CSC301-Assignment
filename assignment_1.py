# --------------------------------------------
# CSC 301 – Assignment (Activities 1, 2, Tasks 5 & 6)
# --------------------------------------------

# -----------------------------
# Activity 1:
# Write a function to compute the sum of all elements in a list.
# Analyze its time complexity.
# -----------------------------

def total_sum(arr):
    total = 0
    for i in arr:
        total += i
    return total

print("Activity 1: Sum of list =", total_sum([3, 5, 7, 10]))
print("Time Complexity: O(n), Space Complexity: O(1)")
print()


# -----------------------------
# Activity 2:
# Trace how linked list insertion at the head works.
# (Implemented using a simple LinkedList class)
# -----------------------------

class Node:
    """A single node of a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Linked list supporting head insertion."""
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head   # new node points to old head
        self.head = new_node        # head becomes new node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


print("Activity 2: Inserting at head")
ll = LinkedList()
ll.insert_at_head(10)
ll.insert_at_head(20)
ll.insert_at_head(30)
ll.display()
print()


# -----------------------------
# Lab Task 5:
# Implement:
#   - insert_at_beginning
#   - insert_at_end
#   - delete_node(key)
#   - display_list()
# Insert at least 5 values and delete one.
# -----------------------------

class FullLinkedList:
    """Full linked list with all required operations."""
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert_at_end(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def delete_node(self, key):
        temp = self.head

        # If head needs deletion
        if temp and temp.data == key:
            self.head = temp.next
            return

        # Search for key
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp:  # Found
            prev.next = temp.next

    def display_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Test Lab Task 5
print("Lab Task 5: Full Linked List Operations")
lst = FullLinkedList()

# Insert 5 values
lst.insert_at_end(10)
lst.insert_at_end(20)
lst.insert_at_end(30)
lst.insert_at_end(40)
lst.insert_at_end(50)

print("Original list:")
lst.display_list()

# Delete one value
lst.delete_node(30)

print("After deleting 30:")
lst.display_list()
print()


# -----------------------------
# Discussion Questions (6)
# -----------------------------

print("Discussion Questions (Answers)")

# 1. Difference between primitive data types and ADTs.
print("\n1. Primitive Data Types vs ADTs:")
print("Primitive data types store single simple values (int, float, char).")
print("ADTs describe operations on data (List, Stack, Queue) without showing implementation.")

# 2. Why arrays are static and linked lists dynamic.
print("\n2. Why arrays are static, linked lists dynamic:")
print("Arrays have fixed size in memory; cannot grow/shrink.")
print("Linked lists use nodes allocated at runtime, so they grow or shrink freely.")

# 3. When to prefer linked list over array.
print("\n3. When to use linked list instead of array:")
print("Use linked lists when you need frequent insertions/deletions and do not require random access.")

# 4. Real-world examples.
print("\n4. Real-world Examples:")
print("Stack → Undo feature, browser back button")
print("Queue → Waiting lines, print queue")
print("Linked List → Music playlist where songs can be added/removed easily")

print("\n---- END OF ASSIGNMENT ----")

