# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head_group = tail_group = ListNode()
        head_sequence = tail_sequence = None
        checkpoint = head
        prev = None

        count = 0
        while head is not None:
            head_sequence = ListNode(head.val)
            head_sequence.next = prev

            if count == 0: 
                    tail_sequence = head_sequence
                    checkpoint = head

            if count == k - 1:
                count = 0
                tail_group.next = head_sequence
                tail_group = tail_sequence
                prev = None
                head_sequence = None
                checkpoint = None
            
            else:
                prev = head_sequence
                count += 1

            head = head.next

        tail_group.next = checkpoint

        return dummy_head_group.next


            

# count: 0 
# head (original): 4
# tail: 1 --> None
# prev: 3 --> 2 --> 1 --> None
# head_reversed: 3 --> 2 --> 1 --> ||  4 --> None

# None | 1 2 3 | 4 5 6 | 7 8 9

# list_total: 3 --> 2 --> 1 --> 4

# reverse sequence by sequence, then join the sequences
# need to keep last in sequence, first in sequence
# first in sequence n must join with last in sequence n+1
