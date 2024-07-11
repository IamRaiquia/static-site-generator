import unittest

from generate_webpage import extract_title

class TestGenerateWebpage(unittest.TestCase):
    def test_generate_webpage(self):
        md = """
# This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        header = extract_title(md)
        self.assertEqual(
            header,
                "This is **bolded** paragraph",
        )


if __name__ == "__main__":
    unittest.main()