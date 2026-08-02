class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.nodes = {}
        self.head, self.tail = None, None

    def get(self, key: int) -> int:
        if key in self.cache:
            self.update_list(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.update_list(key)
            self.cache[key] = value
        else:
            # create a new node
            newNode = Node(key)
            self.cache[key] = value

            # case 1: nodes already in list
            if self.nodes:
                # update the tail
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode

                # if capacity exceeded
                if len(self.nodes) >= self.capacity:
                    # remove the node at the beginning of the list
                    oldNode = self.head

                    print("put", "key:", key, "value", value)
                    print("put" "self.nodes", self.nodes)
                    print("put", f"popping oldest node ({oldNode.val})...")
                    print()
                    
                    self.head = oldNode.next
                    self.head.prev = None

                    self.nodes.pop(oldNode.val)
                    self.cache.pop(oldNode.val)

            # case 2: no nodes in list
            else:
                # initialize head and tail
                self.head = newNode
                self.tail = newNode

            # add new node to list
            self.nodes[key] = newNode

    def update_list(self, key: int) -> None:
        currNode = self.nodes[key]
        prevNode = currNode.prev
        nextNode = currNode.next
 
        if nextNode:
            # case 1: currNode is in the middle of the list
            if prevNode:
                nextNode.prev = prevNode
                prevNode.next = nextNode

            # case 2: currNode is at the beginning of the list
            elif nextNode and not prevNode:
                self.head = nextNode
                nextNode.prev = None

            # update tail
            self.tail.next = currNode
            currNode.prev = self.tail
            currNode.next = None
            self.tail = currNode

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
