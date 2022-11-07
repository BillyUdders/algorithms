from collections import abc
from dataclasses import dataclass, field
from typing import Any, List, Iterator


@dataclass
class ListNode:
    data: Any
    next: "ListNode" = field(default=None)


class LinkedList(abc.MutableSequence):

    def __init__(self, nodes: List = None):
        self.head = None
        if nodes is not None:
            node = ListNode(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = ListNode(data=elem)
                node = node.next

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
                return
            else:
                new_node.next = node.next
                node.next = new_node

    def delete(self, target_node_data) -> None:
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
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
        counter = 0
        for _ in self:
            counter += 1
        return counter

    def __repr__(self) -> str:
        rep = []
        for i in self:
            rep.append(i.data)
        return ", ".join(rep)
