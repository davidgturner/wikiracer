import unittest

from py_wikiracer.wikiracer import DFSProblem


class DFSComplex(unittest.TestCase):

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
                                                                            '/wiki/Northern_News', '/wiki/Jam!',
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
