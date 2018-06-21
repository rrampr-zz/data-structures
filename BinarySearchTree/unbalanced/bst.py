class BinarySearchTree:
    class Node:
        def __init__(self, key, value, left=None, right=None):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

        def getValue(self):
            return self.value
        def set(self, value):
            self.value = value
        def getKey(self):
            return self.key
        def setKey(self, key):
            self.key = key
        def getLeft(self):
            return self.left
        def getRight(self):
            return self.right
        def setRight(self, node):
            self.right = node
        def setLeft(self, node):
            self.left = node
        def __iter__(self):
            if self.left:
                for i in self.left:
                    yield i
            yield (self.key, self.value)
            if self.right:
                for i in self.right:
                    yield i

    ## BST specific methods now
    def __init__(self, root = None):
        self.root = root
    def insert(self, key, value=None):
        self.root = self.__insert__(self.root, key, value)
    def search(self, key):
        node = self.__search__(self.root, key)
        ## First component is None if the key doesn't exist in the tree
        ## If the key is in the tree, the first component is not none
        ## the data associated w/ tree can be None or not None depending upon if you
        ## use your BST as a ordered set or ordered map
        if node is not None:
            return (node.getKey(), node.getValue())
        else:
            return (None, None)
    def delete(self, key):
        self.__delete__(self.root, key)

    #### Private methods of the BST #######
    def __iter__(self):
        return iter(self.root)
    def __insert__(self, node, key, value=None):
        if node is None:
            return self.Node(key, value)
        if node.getKey() == key:
            node.setValue(value)
            return node
        if key < node.getKey():
            node.setLeft(self.__insert__(node.getLeft(), key, value))
        else:
            node.setRight(self.__insert__(node.getRight(), key, value))
        return node

    def __search__(self, node, key):
        if node is None or node.getKey() == key:
            return node
        if key < node.getKey():
            return self.__search__(node.getLeft(), key)
        else:
            return self.__search__(node.getRight(), key)

    def __delete__(self, node, key):
        if node is None:
            return node
        if key < node.getKey():
            node.setLeft(self.__delete__(node.getLeft(), key))
        elif key > node.getKey():
            node.setRight(self.__delete__(node.getRight(), key))
        else:
            ## found node
            if node.getLeft() is None:
                return node.getRight()
            elif node.getRight() is None:
                return node.getLeft()
            else:
                ## Find the inorder successor of this current node
                succ = self.__findMin__(node.getRight())
                ret = self.Node(succ.getKey(), succ.getValue())
                self.__delete__(succ.getKey(), node.getRight())
                return ret
        return node

    def __findMin__(self, node):
        ## Non empty tree should be given as input
        if node is None:
            return None
        ## Go to the leftmost leaf node in the tree
        while node.getLeft():
            node = node.getLeft()
        return node


if __name__ == "__main__":
    a = BinarySearchTree(None)
    a.insert(3)
    a.insert(1)
    a.insert(5)
    a.insert(0)
    for i in a:
        print(i)
    foo = a.search(1)
    print("found" + str(foo))
    bar = a.search(10)
    print("found" + str(bar))
    a.delete(1)
    for i in a:
        print(i)
