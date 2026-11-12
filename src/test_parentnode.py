import unittest
from htmlnode import *

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        ) 

    def test_to_html_with_children_p(self):
        child_node = LeafNode("b", "child")
        child_node2 = LeafNode("i", "child2")
        parent_node = ParentNode("p", [child_node, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>child</b><i>child2</i></p>",
        )

    def test_to_html_with_props(self):
        child_node = LeafNode("a", "Click me!",props={
                        "href": "https://www.google.com",
                        "target": "_blank",
                    })
        parent_node= ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         '<div><a href="https://www.google.com" target="_blank">Click me!</a></div>'
                         )
     
if __name__ == "__main__":
    unittest.main()