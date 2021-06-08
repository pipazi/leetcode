# -*- coding: utf-8 -*-
"""
Created on 2021/6/8 10:26

@author: sun shaowen
"""


class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def construct_tree(lis: list):
    root: TreeNode = TreeNode(lis.pop(0))
    queue = [root]
    while lis:
        node = queue.pop(0)

        # left child
        lchild = lis.pop(0)
        if lchild is not None:
            left = TreeNode(lchild)
            node.left = left
            queue.append(left)

        # right child
        rchild = lis.pop(0)
        if rchild is not None:
            right = TreeNode(rchild)
            node.right = right
            queue.append(right)
    return root
