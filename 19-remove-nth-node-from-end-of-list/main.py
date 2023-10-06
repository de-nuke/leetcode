from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    def __repr__(self):
        return str(self.val)


def make_linked_list(values: List[int]) -> ListNode:
    head = None
    for value in reversed(values):
        head = ListNode(val=value, next_=head)
    return head


TESTS = [
    {"in": (make_linked_list([1, 2, 3, 4, 5]), 2), "out": [1, 2, 3, 5]},
    {"in": (make_linked_list([1]), 1), "out": []},
    {"in": (make_linked_list([1, 2]), 1), "out": [1]},
]


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Convert linked list into regular list of nodes. Incrementing "idx_to_remove"
        while iterating over linked list and starting from "-n" will eventually give
        us index of the element to remove.

        In order to "remove" element from a linked list we simply set the "next"
        attribute of the previous node to point to the node after the one which is
        being removed.

        Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
        """
        nodes = []
        append = nodes.append  # Don't waste the time to get the attribute each time
        idx_to_remove = -n
        while head:
            append(head)
            idx_to_remove += 1
            head = head.next

        if idx_to_remove == 0:
            return nodes[0].next

        nodes[idx_to_remove - 1].next = nodes[idx_to_remove].next
        return nodes[0]


if __name__ == "__main__":
    for test_case in TESTS:
        _input = test_case["in"]
        expected_output = test_case["out"]
        result_head = Solution().removeNthFromEnd(*_input)
        actual_output = []
        while result_head is not None:
            actual_output.append(result_head.val)
            result_head = result_head.next

        if actual_output == expected_output:
            print(f"[OK] {_input} -> {actual_output}")
        else:
            print(f"[XX] {_input} -> {actual_output} (expected: {expected_output})")
