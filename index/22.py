from util.ListNode import construct_listNode, ListNode


class Solution:
    """
    本题应该用快慢指针。
    其他：回文，中点，倒数k， 环链表
    """
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        nextNode = head
        l = 0
        while(nextNode):
            l += 1
            nextNode = nextNode.next
        
        nextNode = head
        l = l - k
        while(l):
            l -= 1
            nextNode = nextNode.next
        return nextNode


Solution().getKthFromEnd(construct_listNode([1, 2, 3, 4, 5]), 2)
