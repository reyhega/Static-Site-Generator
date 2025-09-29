import unittest

from generate_page import extract_title

class TextTextractTitle(unittest.TestCase):

    def test_extract_title(self):
        md = """
# This is the title 
## This is a header

"""
        title = extract_title(md)
        self.assertEqual(title, "This is the title")