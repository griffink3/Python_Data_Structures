#!/usr/bin/python
# bintree.py

""" Binary Tree module

Implement a node-and-link based Binary Tree structure

"""

from Queue import Queue
import string

class EmptyBinTreeException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class InvalidInputException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Node:

    def __init__(self, parent, value) :
        """
        Input: Node (implicit argument), parent: Node, value: anything
        Output: a Node with a parent node and a value
        Purpose: constructor for a Node
        """
        # Note: we don't throw an invalid input exception if parent = None or value = None
        # because the root node can have no parent and a node can have no value

        # If this isn't the root node, adding this node as a child of the parent node or
        # throwing exception if the parent node is already full of children
        if not parent == None:
            if parent.hasLeft() and parent.hasRight():
                raise InvalidInputException(self)
                print "Parent node already has two children"
            # Variable to represent the node's depth
            self._nodeDepth = parent.depth() + 1
        if parent == None:
            self._nodeDepth = 0;
        # Variable to represent the node's parent
        self._nodeParent = parent
        # Variable to represent the node's value
        self._nodeValue = value
        # Variable to represent the node's left child
        self._nodeLeft = None
        # Variable to represent the node's right child
        self._nodeRight = None


    def parent(self):
        """
        Input: Node (implicit argument)
        Output: Node
        Purpose: get the parent of this Node (if possible)
        """
        # If the node is the root, we return None
        if self._nodeParent == None:
            return None
        else:
            return self._nodeParent

    def left(self):
        """
        Input: Node (implicit argument)
        Output: Node
        Purpose: get the left child of this node (if possible)
        """
        if self._nodeLeft == None:
            print "Node has no left child"
        else:
            return self._nodeLeft

    def right(self):
        """
        Input: Node (implicit argument)
        Output: Node
        Purpose: get the right child of this node (if possible)
        """
        if self._nodeRight == None:
            print "Node has no right child"
        else:
            return self._nodeRight

    def addLeft(self, value) :
        """
        Input: Node (implicit argument), value: anything
        Output: Node (the left child)
        Purpose: add a left child to this node with the given value if there isn't one already and return it.
                If there is one already, just return the current one
        """
        # !!!Since we make a node out of value if it's not a node already, user can't access the node by
        # calling value- instead they must call node.left()!!!
        if not self._nodeLeft == None:
            print "Node already has left child"
        else:
            # If value is already a node, we simply set the left node to the value
            if isinstance(value, Node):
                self._nodeLeft = value
            # However if value is not a node, we make a node and set that node's value to value
            else:
                nodeLeft = Node(self,value)
                self._nodeLeft = nodeLeft
        return self._nodeLeft

    def addRight(self, value) :
        """
        Input: Node (implicit argument), value: anything
        Output: Node (the right child)
        Purpose: add a right child to this node with the given value if there isn't one already and return it.
                 If there is one already, just return the current one
        """
        # !!!Since we make a node out of value if it's not a node already, user can't access the node by
        # calling value- instead they must call node.right()!!!
        if not self._nodeRight == None:
            print "Node already has right child"
        else:
            # If value is already a node, we simply set the right node to the value
            if isinstance(value, Node):
                self._nodeRight = value
            # However if value is not a node, we make a node and set that node's value to value
            else:
                nodeRight = Node(self,value)
                self._nodeRight = nodeRight
        return self._nodeRight

    def hasLeft(self):
        """
        Input: Node (implicit argument)
        Output: boolean
        Purpose: return whether this node has a left child
        """
        if self._nodeLeft == None:
            return False
        else:
            return True

    def hasRight(self):
        """
        Input: Node (implicit argument)
        Output: boolean
        Purpose: return whether the node has a right child
        """
        if self._nodeRight == None:
            return False
        else:
            return True

    def value(self):
        """
        Input: Node (implicit argument)
        Output: anything
        Purpose: return the value stored at this Node
        """
        # Again the node can have no value
        if self._nodeValue == None:
            print "Node has no value"
        else:
            return self._nodeValue

    def depth(self):
        """
        Input: Node (implicit argument)
        Output: int
        Purpose: return the depth of this node in the tree in O(1)
        """
        return self._nodeDepth

    def __str__(self):
        """
        Input: Node (implicit argument)
        Output: String representation of the Node
        Purpose: printing
        """
        output = ""
        output += "(val: "
        output += repr(self.value())
        output += "; L: "
        if self.hasLeft():
            output += str(self.left())
        else:
            output += "<nothing>"
        output += "; R: "
        if self.hasRight():
            output += str(self.right())
        else:
            output += "<nothing>"
        output += ")"
        return output

class BinTree:
    """ Binary Tree class

    Implement a node-and-link based Binary Tree structure

    Author: Griffin Kao
    Date: February 25th, 2016
    """

    def __init__(self) :
        """
        Input: BinTree (implicit argument)
        Output: BinTree
        Purpose: Creates an empty binary tree
        """
        self._treeRoot = None
        self._treeSize = 0
        self._treeHeight = None

    def root(self):
        """
        Input: BinTree (implicit argument)
        Output: Node
        Purpose: return the root node
        Throw a EmptyBinTreeException if the tree is empty
        """
        if self._treeRoot == None:
            raise EmptyBinTreeException(self)
            print "Tree has no root"
        else:
            return self._treeRoot

    def parent(self, node):
        """
        Input: BinTree (implicit argument), node: Node
        Output: Node
        Purpose: return the parent node
        Exceptions: throw an InvalidInputException if input is None
        """
        # Throws an invalid input exception if the node is None or is not a node
        if node == None:
            raise InvalidInputException(self)
        elif node.parent() == None:
            print "Root node- no parent"
            return None
        else:
            return node.parent()

    def children(self, node):
        """
        Input: BinTree (implicit argument), node: Node
        Output: List of child nodes
        Purpose: returns a list of direct child nodes
        Exceptions: throw an InvalidInputException if input is None
        """
        if node == None:
            raise InvalidInputException(self)
        else:
            children = []
            if node.hasLeft():
                children.append(node.left())
            if node.hasRight():
                children.append(node.right())
            # If the list children is empty, we return None
            if len(children) == 0:
                print "Node has no children"
                return None
            else:
                return children

    def isEmpty(self):
        """
        Input: BinTree (implicit argument)
        Output: boolean
        Purpose: return true if the tree is empty, false otherwise in O(1)
        """
        if self._treeRoot == None:
            return True
        else:
            return False


    def size(self):
        """
        Input: BinTree (implicit argument)
        Output: int
        Purpose: return the size of the tree in O(1)
        """
        # Returns 0 if tree is empty
        # !!!Size is only accurate if all nodes in the tree are added using the tree's
        # addRoot, addLeft, or addRight methods!!!
        return self._treeSize


    def height(self):
        """
        Input: BinTree (implicit argument)
        Output: int
        Purpose: return the height of the tree in O(1) time
        Exceptions: throw an EmptyBinTreeException if the height is undefined
        """
        # !!!Height is only accurate if all nodes in the tree are added using the tree's
        # addRoot, addLeft, or addRight methods!!!
        if self._treeRoot == None:
            raise EmptyBinTreeException(self)
        else:
            return self._treeHeight

    def isInternal(self, node):
        """
        Input: BinTree (implicit argument), node: Node
        Output: boolean
        Purpose: return whether the node is internal.
        Exceptions: throw an InvalidInputException if input is None
        """
        if node == None:
            raise InvalidInputException(self)
        if node.hasLeft():
            return True
        elif node.hasRight():
            return True
        else:
            return False

    def isExternal(self, node):
        """
        Input: BinTree (implicit argument), node: Node
        Output: boolean
        Purpose: return whether the node is external.
        Exceptions: throw an InvalidInputException if input is None
        """
        if node == None:
            raise InvalidInputException(self)
        if node.hasLeft():
            return False
        elif node.hasRight():
            return False
        else:
            return True

    def isRoot(self, node):
        """
        Input: BinTree (implicit argument), node: Node
        Output: boolean
        Purpose: return whether the node is the root
        Exceptions: throw an InvalidInputException if input is None
        """
        if node == None:
            raise InvalidInputException(self)
        if self._treeRoot == node:
            return True
        else:
            return False

    def left(self, node):
        """
        Input: BinTree (implicit argument), node: Node
        Output: Node
        Purpose: get the left child of the node (if possible)
        Exceptions: throw an InvalidInputException if input is None
        """
        if node == None:
            raise InvalidInputException(self)
        if node.hasLeft():
            return node.left()
        else:
            print "Node has no left child"
            return None

    def right(self, node):
        """
        Input: BinTree (implicit argument), node: Node
        Output: Node
        Purpose: get the right child of the node (if possible)
        Exceptions: throw an InvalidInputException if input is None
        """
        if node == None:
            raise InvalidInputException(self)
        if node.hasRight():
            return node.right()
        else:
            print "Node has no right child"
            return None

    def hasLeft(self, node):
        """
        Input: BinTree (implicit argument), node: Node
        Output: boolean
        Purpose: return whether the node has a left child
        Exceptions: throw an InvalidInputException if input is None
        """
        if node == None:
            raise InvalidInputException(self)
        if node.hasLeft():
            return True
        else:
            return False

    def hasRight(self, node):
        """
        Input: BinTree (implicit argument), node: Node
        Output: boolean
        Purpose: return whether the node has a right child
        Exceptions: throw an InvalidInputException if input is None
        """
        if node == None:
            raise InvalidInputException(self)
        if node.hasRight():
            return True
        else:
            return False

    def addRoot(self, e):
        """
        Input: BinTree (implicit argument), e: anything
        Output: Node (the root node)
        Purpose: add a root to the tree only if there isn't one already and return it.
                 If there is one already, just return the current one
        """
        if not self._treeRoot == None:
            print "Tree already has root"
        else:
            # If e is already a node, we simply set the root to e
            if isinstance(e, Node):
                self._treeRoot = e
            # However, if e is not a node, we create a new node to be the root whose value is e
            else:
                treeRoot = Node(None,e)
                self._treeRoot = treeRoot
            self._treeSize = 1
            self._treeHeight = 0
        return self._treeRoot

    def addLeft(self, node, e):
        """
        Input: BinTree (implicit argument), node: Node, e: anything
        Output: the left child of the node
        Purpose: add a left child to the node only if there isn't one already and return it.
                 If there is one already, just return the current one
        Exceptions: throw an InvalidInputException if node input is None
        """
        if node == None:
            raise InvalidInputException(self)
        else:
            if node.hasLeft():
                print "Node already has left child"
                return node.left()
            else:
                 # If e is already a node, we simply set the left node to the value
                if isinstance(e, Node):
                    node.addLeft(e)
                # However if e is not a node, we make a node and set that node's value to value
                else:
                    nodeLeft = Node(node,e)
                    node.addLeft(nodeLeft)
                if node.left().depth() > self._treeHeight:
                    self._treeHeight = node.left().depth()
                self._treeSize += 1
                # We repeat the above process even though it occurs in the addLeft method of the node
                # so that we can return this left node as an instance rather than an instancemethod
                return nodeLeft

    def addRight(self, node, e):
        """
        Input: BinTree (implicit argument), node: Node, e: anything
        Output: the right child of the node
        Purpose: add a right child to the node only if there isn't one already and return it.
                 If there is one already, return it
        Exceptions: throw an InvalidInputException if node input is None
        """
        if node == None:
            raise InvalidInputException(self)
        else:
            if node.hasRight():
                print "Node already has right child"
                return node.right()
            else:
                 # If e is already a node, we simply set the right node to the value
                if isinstance(e, Node):
                    node.addRight(e)
                # However if e is not a node, we make a node and set that node's value to value
                else:
                    nodeRight = Node(node,e)
                    node.addRight(nodeRight)
                if node.right().depth() > self._treeHeight:
                    self._treeHeight = node.right().depth()
                self._treeSize += 1
                # We repeat the above process even though it occurs in the addRight method of the node
                # so that we can return this right node as an instance rather than an instancemethod
                return nodeRight

    def __str__(self):
        """
        Input: BinTree (implicit argument)
        Output: String representation of BinTree
        Purpose: printing
        """
        toReturn = 'Size: ' + str(self.size()) + '\n'
        toReturn += 'Height: ' + str(self.height()) + '\n'
        toReturn += str(self.root())
        return toReturn


    """ Helper methods for tree visualization.
    You DON'T need to touch these """

    def graphic(self):
        """Returns a representation of this graph as a .dot file.

        In other words, if you pass the string returned by this method into
        the program DOT (or, better yet, NEATO), you can get an image file
        of the graph."""
        strs = ["graph\n{\n"]

        def annex_vertex(v):
            strs.append("\t" + str(v.value()) + ";\n")

        def annex_edge(v):
            if v.hasLeft():
                strs.append("\t" + str(v.value()) + "--" + str(v.left().value()) + ";\n")
            if v.hasRight():
                strs.append("\t" + str(v.value()) + "--" + str(v.right().value()) + ";\n")

        self.parseVerts(annex_vertex, annex_edge)
        strs.append("}\n")
        return ''.join(strs)

    def popup(self):
        """Opens a new window with this graph rendered by DOT.
        Sequential calls to this function will show the window
        once at a time. """
        import os
        tmp = open("./.tmpgraph", "w+")
        tmp.write(self.graphic())
        tmp.close()
        os.system("dot -Tpng ./.tmpgraph | display")


    def parseVerts(self, f1, f2):
        Q = Queue()
        Q.put(self.root())
        while not Q.empty():
            v = Q.get()
            f1(v)
            f2(v)
            if v.hasLeft():
                Q.put(v.left())
            if v.hasRight():
                Q.put(v.right())
