# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)   # 哑节点，指向真正的头节点
        fast = slow = dummy
        
        # 阶段1：快指针先走n步
        for _ in range(n):
            fast = fast.next
        
        # 阶段2：快慢指针同步前进，直到快指针到达链表末尾
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # 此时slow停在"待删除节点的前一个"，删除slow.next
        slow.next = slow.next.next
        
        return dummy.next