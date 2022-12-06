from dataclasses import dataclass, field
from typing import Any


@dataclass
class BinaryTree:
    data: Any
    left: "BinaryTree" = field(default=None)
    right: "BinaryTree" = field(default=None)
