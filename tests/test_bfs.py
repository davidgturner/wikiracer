import unittest

from py_wikiracer.wikiracer import BFSProblem


class BFSTest(unittest.TestCase):

    def test_bfs(self):
        bfs = BFSProblem()

        bfs_path1 = bfs.bfs(source="/wiki/Computer_science", goal="/wiki/Computer_science")
        bfs_path2 = bfs.bfs(source="/wiki/Computer_science", goal="/wiki/Computation")

        self.assertEqual(["/wiki/Computer_science", "/wiki/Computer_science"], bfs_path1)
        self.assertEqual(["/wiki/Computer_science", "/wiki/Computation"], bfs_path2)


if __name__ == '__main__':
    unittest.main()
