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


def binary_heap():
    """ Binary Heap is a Binary Tree with the following properties
    - A complete tree
    - Either being a Min heap or a Max Heap

    # Complexities
    - Get Minimum in Min Heap: O(1) [Or Get Max in Max Heap]
    - Extract Minimum Min Heap: O(Log n) [Or Extract Max in Max Heap]
    - Decrease Key in Min Heap: O(Log n)  [Or Decrease Key in Max Heap]
    - Insert: O(Log n)
    - Delete: O(Log n)

    # Min heap: The key at the root node must be minimum among the keys of all it’s children

            5                      13
         /      \               /       \
       10        15           16         31
      /                      /  \        /  \
    30                     41    51    100   41

    # Max heap: The key at the root node must be maximum among the keys of all it’s children
    """

    # Min heap
    import sys

    class MinHeap(object):
        def __init__(self, maxsize):
            self.maxsize = maxsize
            self.size = 0
            self.heap = [0] * (self.maxsize + 1)
            self.heap[0] = -1 * sys.maxsize

        def parent(self, pos):
            """ Return the position of parent for the node currently at pos """
            return pos // 2

        def leftChild(self, pos):
            """ Return the position of the left child for the node at pos """
            return 2 * pos

        def rightChild(self, pos):
            """ Return the position of the right child for the node at pos """
            return (2 * pos) + 1

        def isLeaf(self, pos):
            """ Return if the node at pos is a leaf node """
            if (self.size // 2) <= pos <= self.size:
                return True
            return False

        def swap(self, fpos, spos):
            """ Swap the two nodes """
            self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

        def minHeapify(self, pos):
            """ Heapify the nodes of the heap """

            # if the node is a non-leaf node and greater than any of its child
            if not self.isLeaf(pos):
                if self.heap[pos] > self.heap[self.leftChild(pos)] or self.heap[pos] > self.heap[self.rightChild(pos)]:
                    if self.heap[self.leftChild(pos)] < self.heap[self.rightChild(pos)]:
                        # Swap with the left child and heapify the left child
                        self.swap(pos, self.leftChild(pos))
                        self.minHeapify(self.leftChild(pos))
                    else:
                        # Swap with the right child and heapify the left child
                        self.swap(pos, self.rightChild(pos))
                        self.minHeapify(self.rightChild(pos))

        def insert(self, element):
            """ Insert a node into the heap"""
            if self.size >= self.maxsize:
                return
            self.size += 1
            self.heap[self.size] = element

            current = self.size

            while self.heap[current] < self.heap[self.parent(current)]:
                self.swap(current, self.parent(current))
                current = self.parent(current)

        def Print(self):
            """ Print the entire heap structure """
            for i in range(1, (self.size // 2) + 1):
                print(f" PARENT : {str(self.heap[i])}"
                      f" LEFT  CHILD : {str(self.heap[2 * i])}"
                      f" RIGHT CHILD : {str(self.heap[2 * i + 1])}")

        def minHeap(self):
            """ Build the min heap using the minHeapify API """
            for pos in range(self.size // 2, 0, -1):
                self.minHeapify(pos)

    print('The minHeap is ')
    minHeap = MinHeap(15)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)
    minHeap.minHeap()
    minHeap.Print()

    # Max Heap
    class MaxHeap(object):
        def __init__(self, maxsize):
            self.maxsize = maxsize
            self.size = 0
            self.heap = [0] * (self.maxsize + 1)
            self.heap[0] = sys.maxsize

        def parent(self, pos):
            """ Return the position of parent for the node at pos """
            return pos // 2

        def leftChild(self, pos):
            """ Return the position of the left child for the node at pos """
            return 2 * pos

        def rightChild(self, pos):
            """ Return the position of the right child for the node at pos """
            return (2 * pos) + 1

        def isLeaf(self, pos):
            """ Return if the node is a leaf node """
            if (self.size // 2) <= pos <= self.size:
                return True
            return False

        def swap(self, fpos, spos):
            """ Swap the two nodes """
            self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

        def maxHeapify(self, pos):
            """ Heapify the node at pos """
            if not self.isLeaf(pos):
                if self.heap[pos] < self.heap[self.leftChild(pos)] or self.heap[pos] < self.heap[self.rightChild(pos)]:
                    if self.heap[self.leftChild(pos)] > self.heap[self.rightChild(pos)]:
                        self.swap(pos, self.leftChild(pos))
                        self.maxHeapify(self.leftChild(pos))
                    else:
                        self.swap(pos, self.rightChild(pos))
                        self.maxHeapify(self.rightChild(pos))

        def insert(self, element):
            if self.size >= self.maxsize:
                return
            self.size += 1
            self.heap[self.size] = element
            current = self.size

            while self.heap[current] > self.heap[self.parent(current)]:
                self.swap(current, self.parent(current))
                current = self.parent(current)

        def Print(self):
            """ Print the entire heap structure """
            for i in range(1, (self.size // 2) + 1):
                print(f" PARENT : {str(self.heap[i])}"
                      f" LEFT  CHILD : {str(self.heap[2 * i])}"
                      f" RIGHT CHILD : {str(self.heap[2 * i + 1])}")

    print('The maxHeap is ')
    maxHeap = MaxHeap(15)
    maxHeap.insert(5)
    maxHeap.insert(3)
    maxHeap.insert(17)
    maxHeap.insert(10)
    maxHeap.insert(84)
    maxHeap.insert(19)
    maxHeap.insert(6)
    maxHeap.insert(22)
    maxHeap.insert(9)

    maxHeap.Print()


def hash_table():
    """
    # Diff: Dictionary vs Hash Table
    - A dictionary is a data structure that maps keys to values.
    - A hash table is a data structure that maps keys to values
      by taking the hash value of the key (by applying some hash function to it)
      and mapping that to a bucket where one or more values are stored.

    For clarity it may be important to note that it MAY be the case that
    Python currently implements their dictionaries using hash tables,
    and it MAY be the case in the future that Python changes
    that fact without causing their dictionaries to stop being dictionaries.
    """
    return 0


def graph():
    """ Graph is a data structure which consists of the following components
    1. A finite set of vertices, aka nodes
    2. A finite set of edges which connecting two nodes
       ** Usually denoted as (u, v) indicating an edge connecting vertex u -> vertex v

    # Adjacency Matrix
    An adjacency matrix is a 2D array of size V x V where V is the num of vertices in a graph
    Ex)
          0 1 2 3
        0 0 1 0 0
        1 1 0 1 1
        2 0 1 0 1
        3 0 1 1 0

    # Easiest way of representing a graph in Python
    Use a dictionary to represent a graph
    Ex)
        A -> B
        A -> C
        B -> C
        B -> D
        C -> D
        D -> C
        E -> F
        F -> C
    Let's code it below!!
    """

    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

    def generate_edges(graph):
        """ Convert the dict representation of a graph into a list one
            - https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/
        """
        edges = []

        # for each node in graph
        for node in graph:

            # for each neighbour node of a single node
            for neighbour in graph[node]:
                # if edge exists then append
                edges.append((node, neighbour))
        return edges

    a = generate_edges(graph=graph)
    print(a)


if __name__ == '__main__':
    array()
    linked_list()
    stack()
    queue()
    binary_tree()
    binary_search_tree()
    binary_heap()
    graph()
