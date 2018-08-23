class Tree(object):
    def __init__(self, root):
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
        self.value = value
        self.right = right
        self.left = left

    def get_height(self):
        if self.value is None:
            return 0
        else:
            if self.left != None:
                left = self.left.get_height()
            else:
                left = 0

            if self.right != None:
                right = self.right.get_height()
            else:
                right = 0

            return 1 + max(left, right)


if __name__ == "__main__":
    b = Node(1, None, None)
    c = Node(2, b, None)
    d = Node(5, c, None)
    e = Node(7, None, d)
    a = Tree(e)

    print a.print_tree()
