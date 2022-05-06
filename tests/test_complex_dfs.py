import unittest

from py_wikiracer.wikiracer import DFSProblem, BFSProblem


class ComplexDFS(unittest.TestCase):

    # def test_bfs_basic(self):
    #     """
    #     BFS depth 2 search
    #     """
    #     bfs = BFSProblem()
    #     assert bfs.bfs(source="/wiki/Calvin_Li", goal="/wiki/Wikipedia") == ['/wiki/Calvin_Li',
    #                                                                          '/wiki/Chinese_language',
    #                                                                          '/wiki/Wikipedia']
    #     assert bfs.internet.requests == ['/wiki/Calvin_Li', '/wiki/Chinese_name', '/wiki/Chinese_surname',
    #                                      '/wiki/Li_(surname_%E6%9D%8E)', '/wiki/Wuhan', '/wiki/Hubei',
    #                                      '/wiki/Central_Academy_of_Drama', '/wiki/All_Men_Are_Brothers_(TV_series)',
    #                                      '/wiki/Chinese_language']

    # def test_dfs_basic(self):
    #     """
    #     DFS depth 2 search
    #     """
    #     dfs = DFSProblem()
    #     assert dfs.dfs(source="/wiki/Calvin_Li", goal="/wiki/Wikipedia") == ['/wiki/Calvin_Li', '/wiki/Main_Page',
    #                                                                          '/wiki/Wikipedia']
    #     assert dfs.internet.requests == ['/wiki/Calvin_Li', '/wiki/Main_Page']

    def test_dfs_complex(self):
        dfs = DFSProblem()
        assert dfs.dfs(source="/wiki/Calvin_Li", goal="/wiki/Quebecor") == ['/wiki/Calvin_Li', '/wiki/Main_Page',
                                                                            '/wiki/Wikimedia_Foundation',
                                                                            '/wiki/VIAF_(identifier)',
                                                                            '/wiki/Virtual_International_Authority_File',
                                                                            '/wiki/Interested_Parties_Information',
                                                                            '/wiki/Law', '/wiki/Human_science',
                                                                            '/wiki/Truth', '/wiki/Verstehen',
                                                                            '/wiki/Phronesis', '/wiki/Knowledge',
                                                                            '/wiki/Max_Weber',
                                                                            '/wiki/Trove_(identifier)', '/wiki/Trove',
                                                                            '/wiki/The_Sydney_Morning_Herald',
                                                                            '/wiki/OzTAM', '/wiki/Canwest',
                                                                            '/wiki/Pembroke_Daily_Observer',
                                                                            '/wiki/Postmedia_News',
                                                                            '/wiki/Postmedia_Network',
                                                                            '/wiki/Dose_(magazine)',
                                                                            '/wiki/Northern_News',
                                                                            '/wiki/Jam!',
                                                                            '/wiki/Quebecor']
        assert dfs.internet.requests == ['/wiki/Calvin_Li', '/wiki/Main_Page', '/wiki/Wikimedia_Foundation',
                                         '/wiki/VIAF_(identifier)', '/wiki/Virtual_International_Authority_File',
                                         '/wiki/Interested_Parties_Information', '/wiki/Law', '/wiki/Human_science',
                                         '/wiki/Truth', '/wiki/Verstehen', '/wiki/Phronesis', '/wiki/Knowledge',
                                         '/wiki/Max_Weber', '/wiki/Trove_(identifier)', '/wiki/Trove',
                                         '/wiki/The_Sydney_Morning_Herald', '/wiki/OzTAM', '/wiki/Canwest',
                                         '/wiki/Pembroke_Daily_Observer', '/wiki/Postmedia_News',
                                         '/wiki/Postmedia_Network', '/wiki/Dose_(magazine)', '/wiki/Northern_News',
                                         '/wiki/Jam!']


if __name__ == '__main__':
    unittest.main()
