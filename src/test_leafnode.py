import unittest
from htmlnode import *

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!",props={
                "href": "https://www.google.com",
                "target": "_blank",
            })
        self.assertEqual(node.to_html(),'<a href="https://www.google.com" target="_blank">Click me!</a>')
if __name__ == "__main__":
    unittest.main()