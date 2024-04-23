from tree import Tree
from tree import TestTree
from node import Node

tree = Tree()

tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
testTree = TestTree()
testTree.test_find_exists(tree)
testTree.test_find_not_exists(tree)
