#!/usr/bin/env python3

from dataclasses import dataclass, field
from typing import List


@dataclass
class TreeNode:
    bit: List = field(default_factory=lambda: [None, None])


@dataclass
class LeafNode:
    value: int = 0


class BinaryTree:
    def __init__(self, max_bits: int):
        self.max_bits = max_bits
        self.root = TreeNode()

    def print(self):
        self._print_tree_part(self.root)

    def insert(self, word: int):
        if word.bit_length() > self.max_bits:
            raise ValueError(f"bit length {word.bit_length()} exceeds {self.max_bits}")
        binary = f"{word:0{self.max_bits}b}"  # Format to fixed-length binary
        node = self.root
        for i in range(len(binary) - 1, -1, -1):
            b = int(binary[i])
            if node.bit[b] is None:  # new entry
                if i > 0:
                    node.bit[b] = TreeNode()
                else:
                    node.bit[b] = LeafNode()
            node = node.bit[b]
        if not isinstance(node, LeafNode):
            raise AssertionError(f"should be of type LeafNode, not {type(node)}")
        node.value += 1

    def delete(self, word):
        if word.bit_length() > self.max_bits:
            raise ValueError(f"bit length {word.bit_length()} exceeds {self.max_bits}")
        binary = f"{word:0{self.max_bits}b}"  # Format to fixed-length binary
        node = self.root
        for i in range(len(binary) - 1, -1, -1):
            b = int(binary[i])
            if node.bit[b] is None:
                return False
            node = node.bit[b]
        if not isinstance(node, LeafNode):
            raise AssertionError(f"should be of type LeafNode, not {type(node)}")
        if node.value > 0:
            node.value -= 1
            return True
        else:
            return False

    def get(self, word):
        if word.bit_length() > self.max_bits:
            raise ValueError(f"bit length {word.bit_length()} exceeds {self.max_bits}")
        binary = f"{word:0{self.max_bits}b}"  # Format to fixed-length binary
        node = self.root
        for i in range(len(binary) - 1, -1, -1):
            b = int(binary[i])
            if node.bit[b] is None:
                return 0
            node = node.bit[b]
        if not isinstance(node, LeafNode):
            raise AssertionError(f"should be of type LeafNode, not {type(node)}")
        return node.value

    def _print_tree_part(self, node: [None, LeafNode, TreeNode], prefix=""):
        if node is None:
            print("", end='')
        if isinstance(node, LeafNode) and node.value > 0:
            print(f"{prefix}: {node.value}")
        if isinstance(node, TreeNode):
            for index in range(len(node.bit)):
                n = node.bit[index]
                if n is not None:
                    self._print_tree_part(n, f"{index}{prefix}")


if __name__ == "__main__":
    bt = BinaryTree(8)
    bt.insert(12)
    bt.insert(15)
    bt.insert(12)
    bt.insert(255)
    bt.insert(0)
    bt.print()
    print()
    print(bt.get(12))

    bt.delete(12)
    bt.print()

    print()
    bt.delete(12)
    bt.print()

    print()
    bt.delete(12)
    bt.print()

    print()
    bt.delete(17)
    bt.print()
