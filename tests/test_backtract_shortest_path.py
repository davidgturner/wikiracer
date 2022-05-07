import unittest

from py_wikiracer.wikiracer import backpedal


class BacktrackTest(unittest.TestCase):

    # def backpedal(source, target, searchResult):
    #     node = target
    #     backpath = [target]
    #     path = []
    #     while node != source:
    #         backpath.append(searchResult[node])
    #         node = searchResult[node]
    #     for i in range(len(backpath)):
    #         path.append(backpath[-i - 1])
    #     return path

    # def backtrack(self, source, goal, prev_array):
    #
    #     S = list() # stack
    #     u = goal
    #
    #     if prev_array[u] is None or u == source:  # do something only if the vertex is reachable
    #         while u is not None:
    #             S.append(u)

    def test_reverse_path(self):
        prev = {}

        prev["A"] = None

        prev["G"] = "N"
        prev["C"] = "A"

        prev["N"] = "Z"
        prev["R"] = "J"

        prev["Z"] = "P"
        prev["M"] = "C"

        prev["Q"] = "M"

        p = backpedal("A","Q", prev)

        self.assertEqual(["A", "C", "M", "Q"], p)


if __name__ == '__main__':
    unittest.main()
