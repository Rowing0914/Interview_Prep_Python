def array():
    """ Array

    - Accessing time: O(1)
    - Search time: O(n) for sequential search, O(log n) for Binary search
    - Insertion time: O(n)
    - Deletion time: O(n)
    """
    data = [0, 1, 2]

    # search
    print(f"Search an item: {data.index(2)}")

    # insertion
    print(f"Before Insertion: {data}")
    data.insert(1, 4)
    print(f"After Insertion: {data}")

    # deletion
    print(f"Before Deletion: {data}")
    data = data[1:]
    print(f"After Deletion: {data}")


def linked_list():
    """ Singly Linked List: each node contains the reference to the next linked node or None indicating the last node

    - Accessing time: O(n)
    - Search time: O(n) for sequential search, O(log n) for Binary search
    - Insertion time: O(1)
    - Deletion time: O(1)

    # Ref
    - Link: https://www.geeksforgeeks.org/linked-list-set-1-introduction/
    """

    class Node(object):
        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList(object):
        def __init__(self):
            self.head = None

    llist = LinkedList()
    llist.head = Node(data=1)
    llist.head.next = Node(data=2)
    llist.head.next.next = Node(data=3)


def stack():
    """ Stack
    - Accessing time: O(n)
    - Insertion(Append) time: O(1)
    - Deletion(Pop) time: O(1)

    # Ref
    - Link: https://www.geeksforgeeks.org/stack-in-python/
    """
    data = []

    # append() function to push an element in the data
    data.append('a')
    data.append('b')

    print(f'Initial data {data}')

    # pop() function to pop element from data in LIFO order
    print('\nElements poped from data:')
    print(data.pop())
    print(data.pop())

    print(f'\nStack after elements are poped: {data}')


def queue():
    """ Stack
    - Accessing time: O(n)
    - Insertion(Append) time: O(1)
    - Deletion(Pop) time: O(1)

    # Ref
    - Link: https://www.geeksforgeeks.org/queue-in-python/
    """
    data = []

    # append() function to push an element in the data
    data.append('a')
    data.append('b')

    print(f'Initial data {data}')

    # pop() function to pop element from data in LIFO order
    print('\nElements popped from data:')
    print(data.pop(0))
    print(data.pop(0))

    print(f'\nStack after elements are popped: {data}')


def binary_tree():
    """ Trees are hierarchical data structures

    # Key components
    1. Data
    2. Pointer to left child
    3. Pointer to right child

    # Properties
    - Max num of nodes at level(denotes l): 2^{l-1}
    - Max num of nodes in a tree: 2^{h+1} - 1 where h is the height of the tree
    - Time Complexity of Tree Traversal: O(n)

    # Ref
    - https://www.geeksforgeeks.org/binary-tree-set-1-introduction/
    """

    class Node(object):
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data

    # Create a root
    root = Node(data=1)
    root.left = Node(data=2)
    root.right = Node(data=3)
    root.left.left = Node(data=4)
    """ Structure
        1    <-- root
      /   \
     2     3  
     /   
    4
    """


def binary_search_tree():
    """ Binary Tree with the following properties
    - The left subtree of a node contains only nodes with keys LESSER than the node's key
    - The right subtree of a node contains only nodes with keys GREATER than the node's key

    # Complexity ** h is the height of the tree
    - Search time: O(h)
    - Insertion time: O(h)
    - Deletion time: O(h)
    Extra Space: O(n) for pointers

    # Binary Tree vs Binary Search Tree
    ## Binary Tree
        1
      /   \
     2     3
     /
    4

    ## Binary Search Tree
        3             2
      /   \         /   \
     2     4  or   1     3 and so on!
     /                   \
    1                    4

    # Ref
    - https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
    """
    class Node(object):
        def __init__(self, key):
            self.left = None
            self.right = None
            self.key = key

    def insert(node, key):
        """ Insertion method for a binary search tree """
        # If the tree is empty, return a new node
        if node is None:
            return Node(key)

            # Otherwise recur down the tree
        if key < node.key:
            node.left = insert(node.left, key)
        else:
            node.right = insert(node.right, key)

            # return the (unchanged) node pointer
        return node

    """ Let us create the following BST 
              50 
           /     \ 
          30      70 
         /  \    /  \ 
       20   40  60   80
    """

    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)


if __name__ == '__main__':
    array()
    linked_list()
    stack()
    queue()
    binary_tree()
    binary_search_tree()