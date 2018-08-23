class Tree(object):
    def __init__(self, root):
        """
        To initialize an instance
        :param root: a node belong to the class Node(). This is the root of the tree.
        """
        self.root = root

    def get_value_root(self):
        """
        This is the function to get the value for the root node.
        :return is the value for the root node
        """
        if self.root is not None:
            return self.root.value
        else:
            return None

    def print_tree(self):
        """
        This is the print tree function, the output is the printed tree as professor suggested.
        :return: a string that when printed, shows the required format
        """
        height = self.root.get_height()
        res = ["|"] * height
        for i in range(height):
            res[i] = ["|"] * (2 * height - 1)
        a = 0
        b = height - 1
        node = self.root

        def recur(res, node, a, b):
            if node is not None:
                res[a][b] = node.value
                if node.right is not None:
                    res = recur(res, node.right, a + 1, b + 1)
                if node.left is not None:
                    res = recur(res, node.left, a + 1, b - 1)
                return res
            else:
                return res

        res = recur(res, node, a, b)
        for i in range(height):
            res[i] = ''.join(list(map(str, res[i])))
        return '\n'.join(res)


class Node(object):
    def __init__(self, value, left, right):
        """
        This is to initialize an instance of node class.
        :param value: the value of the node, int
        :param left: the left node, belong to the Node() class.
        :param right:the right node, belong to the Node() class.
        """
        self.value = value
        self.right = right
        self.left = left

    def get_height(self):
        """
        This is to get height of the tree, which is defined by the length of the longest chain in the tree.
        :return: an int which is the number of nodes in the longest chain.
        """
        if self.value is None:
            return 0
        else:
            if self.left is not None:
                left = self.left.get_height()
            else:
                left = 0

            if self.right is not None:
                right = self.right.get_height()
            else:
                right = 0

            return 1 + max(left, right)
