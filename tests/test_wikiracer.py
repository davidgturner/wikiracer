import unittest

from py_wikiracer.wikiracer import WikiracerProblem


class WikiracerTests(unittest.TestCase):

    def process_race(self, wr_problem, src, goal):
        if src and not src.startswith("/wiki/"):
            src = "/wiki/" + src

        if goal and not goal.startswith("/wiki/"):
            goal = "/wiki/" + goal

        wr_path = wr_problem.wikiracer(src, goal)
        num_downloads = len(wr_problem.internet.requests)
        return wr_path, num_downloads

    def check_wiki_race(self, wr_problem, s, g, largest_tolerated_downloads):
        p, dl = self.process_race(wr_problem, s, g)
        print("s: ", s, " g: ", g, " # of downloads= ", dl)
        self.assertLessEqual(dl, largest_tolerated_downloads)

    def test_race_hops(self):
        wr_problem = WikiracerProblem()
        self.check_wiki_race(wr_problem, 'Johnny_Damon', 'Brazil', 80)
        self.check_wiki_race(wr_problem, 'Chicago_Blackhawks', 'United_Nations', 80)
        # self.check_wiki_race(wr_problem, 'Madonna', 'Altoids', 80)
        self.check_wiki_race(wr_problem, 'Mao_Zedong', 'Brazil', 80)
        self.check_wiki_race(wr_problem, 'Jesus', 'Brazil', 80)


if __name__ == '__main__':
    unittest.main()
