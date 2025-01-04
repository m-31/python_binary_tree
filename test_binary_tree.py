import unittest
from io import StringIO
import sys
from binary_tree import BinaryTree


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        """Set up a BinaryTree instance for each test."""
        self.tree = BinaryTree(8)

    def capture_output(self, func, *args, **kwargs):
        """Helper function to capture print output."""
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        try:
            func(*args, **kwargs)
        finally:
            sys.stdout = old_stdout
        return new_stdout.getvalue()

    def test_insert_and_get(self):
        """Test inserting and retrieving values."""
        self.tree.insert(12)
        self.tree.insert(15)
        self.tree.insert(12)
        self.tree.insert(255)

        self.assertEqual(self.tree.get(12), 2)
        self.assertEqual(self.tree.get(15), 1)
        self.assertEqual(self.tree.get(255), 1)
        self.assertEqual(self.tree.get(0), 0)  # Not inserted, should return 0

    def test_delete(self):
        """Test deleting values."""
        self.tree.insert(12)
        self.tree.insert(12)
        self.tree.insert(15)

        self.assertTrue(self.tree.delete(12))  # Value exists, should delete
        self.assertEqual(self.tree.get(12), 1)

        self.assertTrue(self.tree.delete(12))  # Deleting again
        self.assertEqual(self.tree.get(12), 0)

        self.assertFalse(self.tree.delete(12))  # No value left to delete
        self.assertFalse(self.tree.delete(0))  # Value not in tree

    def test_bit_length_exceeds_max(self):
        """Test handling of values with bit lengths exceeding max_bits."""
        with self.assertRaises(ValueError):
            self.tree.insert(300)  # Bit length exceeds 8 bits
        with self.assertRaises(ValueError):
            self.tree.delete(300)
        with self.assertRaises(ValueError):
            self.tree.get(300)

    def test_print_tree(self):
        """Test the print output of the tree."""
        self.tree.insert(12)
        self.tree.insert(15)
        self.tree.insert(255)

        expected_output = "00001100: 1\n" \
                          "00001111: 1\n" \
                          "11111111: 1\n"
        actual_output = self.capture_output(self.tree.print)
        self.assertEqual(expected_output, actual_output)

    def test_delete_nonexistent(self):
        """Test deleting a value that doesn't exist."""
        self.assertFalse(self.tree.delete(17))  # Not in tree

    def test_insert_zero(self):
        """Test inserting and deleting the value 0."""
        self.tree.insert(0)
        self.assertEqual(self.tree.get(0), 1)
        self.assertTrue(self.tree.delete(0))
        self.assertEqual(self.tree.get(0), 0)

    def test_multiple_inserts_and_deletes(self):
        """Test a sequence of inserts and deletes."""
        self.tree.insert(12)
        self.tree.insert(15)
        self.tree.insert(12)
        self.tree.insert(0)
        self.tree.insert(255)

        # Delete all values
        self.assertTrue(self.tree.delete(12))
        self.assertTrue(self.tree.delete(12))
        self.assertTrue(self.tree.delete(15))
        self.assertTrue(self.tree.delete(0))
        self.assertTrue(self.tree.delete(255))

        # Tree should now be empty
        expected_output = ""
        actual_output = self.capture_output(self.tree.print)
        self.assertEqual(expected_output, actual_output)


if __name__ == "__main__":
    unittest.main()
