import unittest

from py_wikiracer.wikiracer import BFSProblem, Parser


class CustomInternet():
    def __init__(self):
        self.requests = []
    def get_page(self, page):
        self.requests.append(page)
        return f'<a href="{page}"></a>'

class MyTestCase(unittest.TestCase):

    def test_custom_get_links(self):
        bfs = BFSProblem()
        bfs.internet = CustomInternet()

        page_results = bfs.internet.get_page("/wiki/Calvin_Li")
        links = Parser.get_links_in_page(page_results)

        print("page_results = ", page_results)
        print("links = ", links)

        s = "/wiki/Calvin_Li"
        e = "/wiki/Wikipedia"

        path = bfs.bfs(source=s, goal=e)
        # if path is None or len(path) == 1 and path[0] == s or (len(path) == 2 and path[0] == s and path[1] == e):
        #     path = None

        print("# of requests ", len(bfs.internet.requests))

        self.assertEqual(None, path)


if __name__ == '__main__':
    unittest.main()
