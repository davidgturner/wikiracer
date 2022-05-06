import unittest

from py_wikiracer.wikiracer import BFSProblem, DijkstrasProblem

COUNT = 0
def increment():
    global COUNT
    temp_count = COUNT
    COUNT = COUNT + 1
    return temp_count

class DijkstraTests(unittest.TestCase):

    # this tests ties in dijkstra
    # @unittest.skip('skipped test')
    def test_dijkstra_cost_func_ties(self):
        dijk = DijkstrasProblem()
        c = lambda y, x: len(x) * 1000 + x.count("a") * 100 + x.count("u") + x.count("h") * 5 - x.count("F")
        expected_result = ['/wiki/Calvin_Li', '/wiki/Main_Page', '/wiki/Wikipedia']
        dijkstra_path = dijk.dijkstras(source="/wiki/Calvin_Li", goal="/wiki/Wikipedia", costFn=c)
        print(dijkstra_path)
        self.assertEqual(expected_result, dijkstra_path)

    # this tests dijkstras with a cost function of 1 which should behave exactly like Dijkstras
    # @unittest.skip('skipped test')
    def test_dijkstra_as_bfs(self):
        src = "/wiki/Calvin_Li"
        goal = "/wiki/Wikipedia"

        b = BFSProblem()
        bfs_path = b.bfs(src, goal)
        print("got bfs path as: ", bfs_path)

        dijk = DijkstrasProblem()
        cost_func = lambda y, x: increment()
        dijkstra_path = dijk.dijkstras(src, goal, cost_func)

        self.assertEqual(bfs_path, dijkstra_path)


if __name__ == '__main__':
    unittest.main()
