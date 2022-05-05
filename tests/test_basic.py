import unittest

from py_wikiracer.internet import Internet
from py_wikiracer.wikiracer import Parser


class BasicTests(unittest.TestCase):

    # make sure links do not contain links to themselves
    def test_get_links_in_page_avoid_self(self):
        internet = Internet()

        html = internet.get_page("/wiki/Northern_News")  # internet.get_page("/wiki/Henry_Krumrey")
        links_page = Parser.get_links_in_page(html)

        self.assertNotIn("/wiki/Northern_News", links_page)

    def test_get_links_in_page(self):
        # test_site_location_1 = "test_site/henry_kumrey/start.html"
        internet = Internet()
        html = internet.get_page("/wiki/Henry_Krumrey") # internet.get_page("/wiki/Henry_Krumrey")

        # clean_links[
        #     '/wiki/Wisconsin_State_Senate',
        #     '/wiki/Wisconsin_Senate,_District_20',
        #     '/wiki/Wisconsin_State_Assembly',
        #     '/wiki/Plymouth,_Sheboygan_County,_Wisconsin',
        #     '/wiki/Republican_Party_(United_States)',
        #     '/wiki/Plymouth,_Sheboygan_County,_Wisconsin',
        #     '/wiki/Sheboygan_County,_Wisconsin',
        #     '/wiki/Republican_Party_(United_States)'
        #     , '/wiki/United_States_presidential_election_in_Wisconsin,_1900',
        #     '/wiki/Wisconsin_State_Assembly',
        #     '/wiki/Wisconsin_State_Senate',
        #     '/wiki/Crystal_Lake,_Illinois',
        #     '/wiki/Wisconsin_State_Senate',
        #     '/wiki/Wisconsin_State_Assembly',
        #     '/wiki/Henry_Krumrey',
        #     '/wiki/Henry_Krumrey',
        #     '/wiki/Main_Page']

        assert Parser.get_links_in_page(html) == ['/wiki/Wisconsin_State_Senate',
                                                  '/wiki/Wisconsin_Senate,_District_20',
                                                  '/wiki/Wisconsin_State_Assembly',
                                                  '/wiki/Plymouth,_Sheboygan_County,_Wisconsin',
                                                  '/wiki/Republican_Party_(United_States)',
                                                  '/wiki/Sheboygan_County,_Wisconsin',
                                                  '/wiki/United_States_presidential_election_in_Wisconsin,_1900',
                                                  '/wiki/Crystal_Lake,_Illinois',
                                                  '/wiki/Henry_Krumrey',
                                                  '/wiki/Main_Page']
        # self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
