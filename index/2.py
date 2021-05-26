from util.ListNode import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = l3 = ListNode(0)
        quo = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            res = x + y + quo
            rem = res if res < 10 else res - 10
            quo = 0 if res < 10 else 1

            l3.next = ListNode(rem)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            l3 = l3.next

        if quo:
            l3.next = ListNode(quo)
        return a.next
