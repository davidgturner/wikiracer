from collections import defaultdict
from difflib import SequenceMatcher
from queue import Queue, LifoQueue, PriorityQueue

from py_wikiracer.internet import Internet
from typing import List
import re
import random


def invalid_url_pattern(test_str: str, disallowed_chars_array: []):
    concat_str = ''.join(disallowed_chars_array)
    re1 = re.compile(r"[" + concat_str + "`]")
    return re1.search(test_str)


def get_text_portion(link):
    """ for text like this "/wiki/Athlon_Sports" will return as Athlon_Sports """
    wiki_url_prefix = "/wiki/"
    return link[len(wiki_url_prefix):]


def exclude_links(x: str):
    disallowed_list = Internet.DISALLOWED.split(",")
    if x in disallowed_list or not x.startswith("/wiki"):
        return False
    else:
        return True


def backtrack_path(source, goal, prev: dict):
    """
    backtrack the path using the prev pointers created during the path finding
    """
    page = goal
    backwards_path = [goal]
    path = []
    while page != source:
        backwards_path.append(prev[page])
        page = prev[page]

    # pop from the stack until it's emptied, reversing the backwards path list to get the forward path
    while len(backwards_path) > 0:
        path_item = backwards_path.pop()
        path.append(path_item)

    return path


def find_path(internet_obj: Internet, queue_input: Queue, source, goal, cost_fn):
    """
    a generic function that can be used for BFS, BFS, Dijkstra, etc.
    passes in an internet object, generic queue (which is be a FIFO, LIFO, or Priority queue) along with it's
    source, goal and cost function (if applicable).
    """
    queue_input.queue.clear()

    queue_input.put((0, source))
    explored = set()

    previous_page_map = {source: None}
    page_distance_cost = {source: 0}

    while not queue_input.empty():
        cost, page = queue_input.get()
        print("cost and page off the queue = ", cost, page)
        if page not in explored:
            explored.add(page)
            for neighbor in Parser.get_links_in_page(internet_obj.get_page(page)):
                if neighbor == goal:
                    p = backtrack_path(source, page, previous_page_map)
                    return p

                if cost_fn(page, neighbor) is None:
                    queue_input.put((None, neighbor))

                    if neighbor not in (source, page) and neighbor not in explored:
                        previous_page_map[neighbor] = page
                else:
                    alt_cost = cost + cost_fn(page, neighbor)
                    cost_neighbor_tuple = (alt_cost, neighbor)
                    queue_input.put(cost_neighbor_tuple)

                    # updating costs and previous page pointers
                    # never reset the source node and also never add a previous pointer back to itself
                    if neighbor not in page_distance_cost:
                        if neighbor not in (source, page) and neighbor not in explored:
                            page_distance_cost[neighbor] = alt_cost
                            previous_page_map[neighbor] = page
                    else:
                        if alt_cost <= page_distance_cost[neighbor]:
                            if neighbor not in (source, page) and neighbor not in explored:
                                page_distance_cost[neighbor] = alt_cost
                                previous_page_map[neighbor] = page

    return None  # return None since we didn't find a path

def finalize_path(path, source, goal):
    """
    does checks and balances to make sure path is correct (with edge cases) adding the goal page node, etc.
    """
    if path is None:
        return None

    # add the goal page node
    path.append(goal)

    return path

class Parser:

    @staticmethod
    def get_links_in_page(html: str) -> List[str]:
        """
        In this method, we should parse a page's HTML and return a list of links in the page.
        Be sure not to return any link with a DISALLOWED character.
        All links should be of the form "/wiki/<page name>", as to not follow external links
        """
        links = []
        disallowed = Internet.DISALLOWED

        # YOUR CODE HERE
        # You can look into using regex, or just use Python's find methods to find the <a> tags or any other identifiable features
        # A good starting place is to print out `html` and look for patterns before/after the links that you can string.find().
        # Make sure your list doesn't have duplicates. Return the list in the same order as they appear in the HTML.
        # This function will be stress tested so make it efficient!
        all_links: [] = re.findall(r'(?<=<a href=")[^"]*', html)
        for link in all_links:
            text_portion = get_text_portion(link)
            if invalid_url_pattern(text_portion, disallowed):
                continue
            else:
                if link.startswith("/wiki") and link not in links:
                    links.append(link)
        return links


# In these methods, we are given a source page and a goal page, and we should return
#  the shortest path between the two pages. Be careful! Wikipedia is very large.

# These are all very similar algorithms, so it is advisable to make a global helper function that does all of the work, and have
#  each of these call the helper with a different data type (stack, queue, priority queue, etc.)

class BFSProblem:
    def __init__(self):
        self.internet = Internet()
        self.myqueue = Queue()  # use a simple FIFO queue here

    # Example in/outputs:
    #  bfs(source = "/wiki/Computer_science", goal = "/wiki/Computer_science") == ["/wiki/Computer_science", "/wiki/Computer_science"]
    #  bfs(source = "/wiki/Computer_science", goal = "/wiki/Computation") == ["/wiki/Computer_science", "/wiki/Computation"]
    # Find more in the test case file.

    # Do not try to make fancy optimizations here. The autograder depends on you following standard BFS and will check all of the pages you download.
    # Links should be inserted into the queue as they are located in the page, and should be obtained using Parser's get_links_in_page.
    # Be very careful not to add things to the "visited" set of pages too early. You must wait for them to come out of the queue first. See if you can figure out why.
    #  This applies for bfs, dfs, and dijkstra's.
    # Download a page with self.internet.get_page().
    def bfs(self, source="/wiki/Calvin_Li", goal="/wiki/Wikipedia"):
        dummy_cost_fn = lambda x, y: 1
        path = find_path(self.internet, self.myqueue, source, goal, dummy_cost_fn)
        path = finalize_path(path, source, goal)
        return path  # if no path exists, return None

class DFSProblem:
    def __init__(self):
        self.internet = Internet()
        self.myqueue = LifoQueue()

    # Links should be inserted into a stack as they are located in the page. Do not add things to the visited list until they are taken out of the stack.
    def dfs(self, source="/wiki/Calvin_Li", goal="/wiki/Wikipedia"):
        dummy_cost_fn = lambda x, y: None
        path = find_path(self.internet, self.myqueue, source, goal, dummy_cost_fn)
        path = finalize_path(path, source, goal)
        return path  # if no path exists, return None


class DijkstrasProblem:
    def __init__(self):
        self.internet = Internet()
        self.count = 0
        self.myqueue = PriorityQueue()

    # Links should be inserted into the heap as they are located in the page.
    # By default, the cost of going to a link is the length of a particular destination link's name. For instance,
    #  if we consider /wiki/a -> /wiki/ab, then the default cost function will have a value of 8.
    # This cost function is overridable and your implementation will be tested on different cost functions. Use costFn(node1, node2)
    #  to get the cost of a particular edge.
    # You should return the path from source to goal that minimizes the total cost. Assume cost > 0 for all edges.
    def dijkstras(self, source="/wiki/Calvin_Li", goal="/wiki/Wikipedia", costFn=lambda x, y: len(y)):
        self.myqueue.queue.clear()
        path = find_path(self.internet, self.myqueue, source, goal, costFn)
        path = finalize_path(path, source, goal)
        return path  # if no path exists, return None


class WikiracerProblem:
    def __init__(self):
        self.internet = Internet()
        self.myqueue = PriorityQueue()
        self.num_path_steps = 0
        self.ignore_pages = set() # self.build_ignore_pages_set()
        self.ignore_pages.add("/wiki/Main_Page")

    # Time for you to have fun! Using what you know, try to efficiently find the shortest path between two wikipedia pages.
    # Your only goal here is to minimize the total amount of pages downloaded from the Internet, as that is the dominating time-consuming action.

    # Your answer doesn't have to be perfect by any means, but we want to see some creative ideas.
    # One possible starting place is to get the links in `goal`, and then search for any of those from the source page, hoping that those pages lead back to goal.

    # Note: a BFS implementation with no optimizations will not get credit, and it will suck.
    # You may find Internet.get_random() useful, or you may not.

    def wikiracer(self, source="/wiki/Calvin_Li", goal="/wiki/Wikipedia"):
        # path = [source]
        self.myqueue.queue.clear()

        goal_page_html = self.internet.get_page(goal)
        goal_page_link_neighbors = Parser.get_links_in_page(goal_page_html)

        h_score_function = lambda x, y: self.get_h_score_function(x, y, goal_page_link_neighbors)

        path = find_path(self.internet, self.myqueue, source, goal, h_score_function)
        path = finalize_path(path, source, goal)
        # path.append(goal)

        print("Path = ", path)
        print("Path Length = ", len(path))

        print("Page Downloads = ", self.internet.requests)
        print("# of Page Downloads / Lengths = ", len(self.internet.requests))

        return path  # if no path exists, return None

    def build_ignore_pages_set(self):
        # TODO - need to look at 10-20 random pages and find the intersection set among them all
        common_page_ignore_power_set = set()
        RANDOM_PAGES_TO_INSPECT = 5
        for i in range(0, RANDOM_PAGES_TO_INSPECT):
            rand_page = self.internet.get_random()
            page_links_list = Parser.get_links_in_page(rand_page)
            for p in page_links_list:
                print(p)
            page_links_set = set(page_links_list)
            if len(common_page_ignore_power_set) == 0:  # first time around we set it to the first page links set
                common_page_ignore_power_set = page_links_set
            else:
                common_page_ignore_power_set = common_page_ignore_power_set.intersection(page_links_set)
        # print("The common page links to ignore out:")
        # print(common_page_ignore_power_set)
        # print("===============================")
        self.ignore_pages = common_page_ignore_power_set

    def get_h_score_function(self, source_page, current_page, goal_page_neighbor_links):
        overall_score = 0.0
        # ignore_pages score? - give it 25% weight
        # random_ignore_pages = 0.0
        # if source_page in self.ignore_pages or current_page in self.ignore_pages:
        #     random_ignore_pages = 1.0
        # else:
        #     random_ignore_pages = 0.0

        # is a 1-2 step away goal page neighbors? - give it 25% weight
        goal_neighbor_score = 0.0
        if current_page in goal_page_neighbor_links:
            goal_neighbor_score = 1.0
        else:
            goal_neighbor_score = 0.0

        # sequence matcher - give it 60% weight
        seq = SequenceMatcher(a =source_page, b=current_page)
        seq_matcher_score = seq.quick_ratio() # seq.ratio()

        seq_matcher_score = seq_matcher_score
        # goal_neighbor_score = 1.0
        overall_score = (seq_matcher_score * 0.75) + (goal_neighbor_score * 0.25) # - (random_ignore_pages * 0.30)

        # this is because the more similar something is we want that first off the queue so need to reverse it
        return 1.0 - overall_score


# KARMA
class FindInPageProblem:
    def __init__(self):
        self.internet = Internet()

    # This Karma problem is a little different. In this, we give you a source page, and then ask you to make up some heuristics that will allow you to efficiently
    #  find a page containing all of the words in `query`. Again, optimize for the fewest number of internet downloads, not for the shortest path.

    def find_in_page(self, source="/wiki/Calvin_Li", query=["ham", "cheese"]):
        raise NotImplementedError("Karma method find_in_page")

        path = [source]

        # find a path to a page that contains ALL of the words in query in any place within the page
        # path[-1] should be the page that fulfills the query.
        # YOUR CODE HERE

        return path  # if no path exists, return None
