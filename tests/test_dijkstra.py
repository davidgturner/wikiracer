import unittest

from py_wikiracer.wikiracer import BFSProblem, DijkstrasProblem


class DijkstraTests(unittest.TestCase):

    # this tests dijkstras with a cost function of 1 which should behave exactly like Dijkstras
    def test_dijkstra_as_bfs(self):

        src = "/wiki/Calvin_Li"
        goal = "/wiki/Wikipedia"

        b = BFSProblem()
        bfs_path = b.bfs(src, goal)
        print("got bfs path as: ", bfs_path)

        dijk = DijkstrasProblem()
        cost_func = lambda y, x: 1
        dijkstra_path = dijk.dijkstras(src, goal, cost_func)

        self.assertEqual(bfs_path, dijkstra_path)


if __name__ == '__main__':
    unittest.main()
