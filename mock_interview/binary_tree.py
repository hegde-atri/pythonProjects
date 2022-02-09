# check if a given tree structure is a binary tree?
class node:
    def __init__(self, right, left):
        self.right = right
        self.left = left


def is_binary_tree(n):
    if node.left > node.right:
        is_binary_tree(node.left)
        is_binary_tree(node.right)
    if node.right > node.left:
        return False
    return True


# Answer approved!
