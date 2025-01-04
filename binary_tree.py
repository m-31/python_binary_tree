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
        list1 = [(self.root, "")]
        while len(list1) > 0:
            list2 = []
            for node, prefix in list1:
                if isinstance(node, LeafNode) and node.value > 0:
                    print(f"{prefix}: {node.value}")
                elif isinstance(node, TreeNode):
                    for index in range(2):  # Add children in order
                        if node.bit[index] is not None:
                            list2.append((node.bit[index], f"{prefix}{index}"))
            list1 = list2

    def insert(self, word: int):
        if word.bit_length() > self.max_bits:
            raise ValueError(f"bit length {word.bit_length()} exceeds {self.max_bits}")
        binary = f"{word:0{self.max_bits}b}"  # Format to fixed-length binary
        node = self.root
        for i in range(len(binary)):
            b = int(binary[i])
            if node.bit[b] is None:  # new entry
                if i < len(binary) - 1:
                    node.bit[b] = TreeNode()
                else:
                    node.bit[b] = LeafNode()
            node = node.bit[b]
        if not isinstance(node, LeafNode):
            raise AssertionError(f"should be of type LeafNode, not {type(node)}")
        node.value += 1

    def delete(self, word: int):
        if word.bit_length() > self.max_bits:
            raise ValueError(f"bit length {word.bit_length()} exceeds {self.max_bits}")
        binary = f"{word:0{self.max_bits}b}"  # Format to fixed-length binary
        node = self.root
        for i in range(len(binary)):
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

    def get(self, word: int):
        if word.bit_length() > self.max_bits:
            raise ValueError(f"bit length {word.bit_length()} exceeds {self.max_bits}")
        binary = f"{word:0{self.max_bits}b}"  # Format to fixed-length binary
        node = self.root
        for i in range(len(binary)):
            b = int(binary[i])
            if node.bit[b] is None:
                return 0
            node = node.bit[b]
        if not isinstance(node, LeafNode):
            raise AssertionError(f"should be of type LeafNode, not {type(node)}")
        return node.value


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

    print()
    bt = BinaryTree(990)
    bt.insert(1)
    bt.insert(2 ** 989)
    bt.print()

    print()
    bt = BinaryTree(5000)
    bt.insert(1)
    bt.insert(2 ** (5000 - 1))
    bt.insert(2 ** 2500 + 2 ** 2501 + 2 ** 2502 + 2 ** 2503)
    bt.insert(2 ** 5000 - 1)
    bt.print()
