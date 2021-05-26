# -*- coding: utf-8 -*-
"""
Created on 2021/5/24 12:56

@author: sun shaowen
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def construct_listNode(lis: list):
    head = ListNode(lis.pop(0))
    current = head
    for item in lis:
        current.next = ListNode(item)
        current = current.next
    return head
