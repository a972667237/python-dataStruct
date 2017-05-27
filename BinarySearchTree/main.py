
class TreeNode:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
    def hasLeft(self):
        return self.leftChild
    def hasRight(self):
        return self.rightChild
    def isLeft(self):
        return self.parent and self.parent.leftChild is self
    def isRight(self):
        return self.parent and self.parent.rightChild is self
    def isRoot(self):
        return not self.parent
    def isLeaf(self):
        return (not self.rightChild) and (not self.leftChild)
    def hasOneChild(self):
        return ((not self.rightChild) and self.leftChild) or ((not self.leftChild) and self.rightChild)

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.nodeNum = 0
    def __len__(self):
        return self.nodeNum
    def __iter__(self):
        return self.root.__iter__()
    def put(self, value):
        if self.root:
            self._put(value, self.root)
        else:
            self.root = TreeNode(value)
        self.nodeNum = self.nodeNum + 1
    def _put(self, value, parentNode):
        if value < parentNode.value:
            if parentNode.hasLeft():
                self._put(value, parentNode.leftChild)
            else:
                parentNode.leftChild = TreeNode(value, parent=parentNode)
        else:
            if parentNode.hasRight():
                self._put(value, parentNode.rightChild)
            else:
                parentNode.rightChild = TreeNode(value, parent=parentNode)
    def search(self, value): # return how step can find it
        if self.root:
            result = self._search(value, self.root, 0)
            return result
        else:
            return None
    def _search(self, value, parentNode, rank):
        if not parentNode:
            return None
        #print ("value: {}, now: {}".format(value, parentNode.value))
        if parentNode.value is value:
            return rank
        else:
            rank = rank + 1
            if parentNode.value > value:
                return self._search(value, parentNode.leftChild, rank)
            else:
                return self._search(value, parentNode.rightChild, rank)
    def __contains__(self, value): # to make if 1 in self can return something
        value = int(value)
        if isinstance(self._search(value, self.root, 0), int):
            return True
        else:
            return False
    def inOrderPrint(self):
        if self.root:
            self._inOrder(self.root)
        else:
            print ("empty tree...orz")
    def _inOrder(self, current):
        if not current:
            return
        if current.hasLeft():
            self._inOrder(current.leftChild)
        print (current.value)
        if current.hasRight():
            self._inOrder(current.rightChild)
    def deleteValue(self, value):
        delNode = self._findNode(value, self.root)
        if delNode: # "do this will use logn to search it"
            self._deleteValue(delNode)
        else:
            print ("no such node...and what wrong with you?")
    def _deleteValue(self, delNode):
        if delNode.isLeaf():
            if delNode.isRoot():
                self.root = None
            elif delNode.isLeft():
                delNode.parent.leftChild = None
            else:
                delNode.parent.rightChild = None
        elif delNode.hasOneChild():
            #get the only one child
            child = None
            if delNode.leftChild:
                child = delNode.leftChild
            else:
                child = delNode.rightChild
            if delNode.isRoot():
                self.root = child
                self.root.parent = None
            else:
                if delNode.isLeft():
                    child.parent = delNode.parent
                    delNode.parent.leftChild = child
                else:
                    child.parent = delNode.parent
                    delNode.parent.rightChild = child
        else:
            '''两边都有点咯= =、'''
            minNode = self._findMin(delNode.rightChild)
            temp = delNode.value
            delNode.value = minNode.value
            minNode.value = temp
            self._deleteValue(minNode)

    def _findNode(self, value, parentNode):
        if not parentNode:
            return None
        if value is parentNode.value:
            return parentNode
        if value > parentNode.value:
            return self._findNode(value, parentNode.rightChild)
        else:
            return self._findNode(value, parentNode.leftChild)
    def _findMin(self, parentNode):
        if parentNode.hasLeft():
            return self._findMin(parentNode.leftChild)
        else:
            return parentNode
