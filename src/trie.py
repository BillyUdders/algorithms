from dataclasses import dataclass, field
from typing import List


@dataclass
class TrieNode:
    char: str
    is_terminal: bool = field(default=False)
    children: List["TrieNode"] = field(default_factory=list)
    counter: int = field(default=1)


class Trie:
    def __init__(self):
        self.root: TrieNode = TrieNode("")

    def insert(self, word: str):
        node = self.root

        # Iterate the word
        for char in word:
            found_in_child = False
            # Iterate child nodes, if the current char equals
            for child in node.children:
                if child.char == char:
                    child.counter += 1
                    # we found the char, next iteration we want to start from here
                    node = child
                    found_in_child = True
                    break

            # We did not find it so add a new child
            if not found_in_child:
                new_node = TrieNode(char)
                # Append the new node to the current one
                node.children.append(new_node)
                # Start the iteration on line 24 from the new node we just added
                node = new_node

        # End of the word
        node.is_terminal = True

    def search(self, prefix: str):
        node = self.root
        if not node.children:
            return False, 0

        for char in prefix:
            char_not_found = True
            for child in node.children:
                if child.char == char:
                    char_not_found = False
                    node = child
                    break
            if char_not_found:
                return False, 0

        return True, node.counter
