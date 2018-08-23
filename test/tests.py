import unittest
from tree.tree import Tree,Node

class TestPringTree(unittest.TestCase):
    def test_print_tree(self):
        b = Node(1, None, None)
        c = Node(2, b, None)
        d = Node(5, c, None)
        e = Node(7, None, d)
        a = Tree(e)

        res=[['|', '|', '|', 7, '|', '|', '|'], ['|', '|', '|', '|', 5, '|', '|'], ['|', '|', '|', 2, '|', '|', '|'], ['|', '|', 1, '|', '|', '|', '|']]
        for i in range(3):
            res[i]=''.join(list(map(str,res[i])))
        assert '\n'.join(res)==a.print_tree()