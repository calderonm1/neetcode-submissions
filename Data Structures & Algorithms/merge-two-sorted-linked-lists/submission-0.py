# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode()
        while list1 is not None or list2 is not None:
            minVal = 0
            if list1 is not None and list2 is not None:
                if list1.val < list2.val:
                    minVal = list1.val
                    list1 = list1.next
                else:
                    minVal = list2.val
                    list2 = list2.next
            elif list1 is not None:
                minVal = list1.val
                list1 = list1.next
            else:
                minVal = list2.val
                list2 = list2.next

            head.next = ListNode(minVal)
            head = head.next

        return dummy.next