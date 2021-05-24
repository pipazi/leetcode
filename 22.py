class Solution:
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
