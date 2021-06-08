# -*- coding: utf-8 -*-
"""
Created on 2021/6/8 10:34

@author: sun shaowen
"""
from util.TreeNode import *


def preorder(root: TreeNode):
    if root is None:
        return
    print(root.value)
    preorder(root.left)
    preorder(root.right)


def inorder(root: TreeNode):
    if root is None:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)


def postorder(root: TreeNode):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value)
