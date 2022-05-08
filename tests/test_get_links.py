import unittest

from py_wikiracer.internet import Internet
from py_wikiracer.wikiracer import Parser

class GetLinksTestCase(unittest.TestCase):

    def test_link_counts(self):
        internet = Internet()

        html = internet.get_page("/wiki/Henry_Krumrey")
        self.assertEqual(10, len(Parser.get_links_in_page(html)))

        html = internet.get_page("/wiki/One_Direction")
        self.assertEqual(906, len(Parser.get_links_in_page(html)))

        html = internet.get_page("/wiki/University_of_Texas_at_Austin")
        self.assertEqual(925, len(Parser.get_links_in_page(html)))

        html = internet.get_page("/wiki/United_States")
        self.assertEqual(1757, len(Parser.get_links_in_page(html)))

        html = internet.get_page("/wiki/Data_science")
        self.assertEqual(206, len(Parser.get_links_in_page(html)))


if __name__ == '__main__':
    unittest.main()
