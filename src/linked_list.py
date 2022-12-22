from collections import abc
from dataclasses import dataclass, field
from typing import Any, Iterator


@dataclass
class ListNode:
    data: Any
    next: "ListNode" = field(default=None)


class LinkedList(abc.MutableSequence):

    def __init__(self):
        self.length = 0
        self.head = None

    def insert(self, data: Any, index: int = None, insert_before=True) -> None:
        new_node = ListNode(data)
        if not index:
            new_node.next = self.head
            self.head = new_node
        else:
            node = self[index]
            if insert_before:
                self[index - 1].next = new_node
                new_node.next = node
            else:
                new_node.next = node.next
                node.next = new_node

        self.length += 1

    def delete(self, target_node_data) -> None:
        if self.head is None:
            raise Exception("List is empty")

        if self.head.node == target_node_data:
            self.head = self.head.next
            self.length -= 1
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                self.length -= 1
                return
            previous_node = node

    def __setitem__(self, index: int, data: Any) -> None:
        self.insert(data, index)

    def __delitem__(self, index: int) -> None:
        self.delete(self[index].data)

    def __getitem__(self, index: int) -> ListNode:
        if index <= len(self) - 1:
            for pos, i in enumerate(self):
                if pos == index:
                    return i
        else:
            raise IndexError("Index out of bounds")

    def __iter__(self) -> Iterator[ListNode]:
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __len__(self) -> int:
        return self.length

    def __repr__(self) -> str:
        return ", ".join(i.data for i in self)
