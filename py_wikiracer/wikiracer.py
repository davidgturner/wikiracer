from collections import defaultdict
from queue import LifoQueue, Queue, PriorityQueue

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


def backtrack_path(page_graph: defaultdict, prev_parent: dict, page):
    print("starting a backtrack path with this ", page, prev_parent, page_graph)
    # return []

    current_ptr = page
    path_backwards = [current_ptr]
    page_index = 1

    # this is looking for a trip back to the source node which should be null for parent.
    # this loop is the min distance to lead back to the source node
    while current_ptr is not None:
        pointers_backwards_from_current_node = page_graph[current_ptr]

        filter_use = defaultdict(list) # deepCopy(pointers_backwards_from_current_node)
        for p in pointers_backwards_from_current_node:
            text_link_from_tuple_element = p[1]
            if current_ptr in page_graph[text_link_from_tuple_element]:
                filter_use[current_ptr].append(p)

        print("original JAM ", page_graph["/wiki/Jam!"])
        print("original northern news ", page_graph["/wiki/Northern_News"])

        print('/wiki/Jam! prev parent ', prev_parent['/wiki/Jam!'])
        print('/wiki/Northern_News prev parent ', prev_parent['/wiki/Northern_News'])
        print('/wiki/Dose_(magazine) prev parent ', prev_parent['/wiki/Dose_(magazine)'])

        print("Filtered down entry ", filter_use["/wiki/Jam!"])
        return []
        # pointers_backwards = page_graph[current_ptr]  # the graph entry lets say for /wiki/Jam! and it's list of tuples
        # filtered_pointers_backwards = defaultdict(list)  # the filtered version that just has the links that lead to pointer backwards
        #
        # for element in pointers_backwards:  ## this is canwest, northern news, etc. some of which do not lead to jam
        #     if page_graph[element]
        #     # pointers_backwards[element]
        #     # if element in pointers_backwards[current_ptr]:
        #         filtered_pointers_backwards[element] = pointers_backwards[element]
        #
        # if [page_index] is not None:  #
        smallest_parent = min(filter_use[current_ptr])[page_index]
        print("smallest parent back ", smallest_parent, " page graph of ", filter_use[current_ptr])
        if prev_parent[smallest_parent] is None:
            break
        else:
            next_parent = prev_parent[smallest_parent]
            path_backwards.append(next_parent)

        current_ptr = next_parent

    backwards_path_reversed = list(reversed(path_backwards))  # reverse the backwards path to forwards now
    return backwards_path_reversed

def backtrack_path2(page_graph: defaultdict, prev_parent: dict, cost_dist: dict, page, source):
    print("starting a backtrack path with this ", page, prev_parent, page_graph)
    current = page
    path_backwards = [current]
    while current is not None:
        if current in prev_parent:
            first_prev = prev_parent[current]
            if first_prev is not None and first_prev != source:
                path_backwards.append(first_prev)
                print("adding next next prev parent - ", first_prev)
            current = first_prev

    backwards_path_reversed = list(reversed(path_backwards))  # reverse the backwards path to forwards now
    print("the returned list out ", backwards_path_reversed)
    return backwards_path_reversed


def find_path(internet_obj: Internet, queue_input: Queue, source, goal, cost_fn):
    queue_input.queue.clear()

    queue_input.put((0, source))
    explored = set()

    page_graph = defaultdict(list)
    prev_parent = {source: None}
    dist = {source: 0}

    while not queue_input.empty():
        cost, page = queue_input.get()
        print("cost = ", cost, " page off queue= ", page)
        if page not in explored:
            explored.add(page)

            links_page = Parser.get_links_in_page(internet_obj.get_page(page))
            # links_page.remove(page)
            for neighbor in links_page:
                if neighbor == page:
                    continue
                print("processing neighbor = ", neighbor)
                if neighbor == goal:
                    path = backtrack_path2(page_graph, prev_parent, dist, page, source)
                    return path

                alt_cost = cost + cost_fn(page, neighbor)
                cost_neighbor_tuple = (alt_cost, neighbor)
                queue_input.put(cost_neighbor_tuple)

                # keep track of the page graph
                page_graph[neighbor].append(cost_neighbor_tuple)

                # never reset the source node and don't add neighbor if already explored
                if neighbor not in dist:
                    dist[neighbor]= 0

                if alt_cost <= dist[neighbor]:
                    if neighbor not in (source, page) and neighbor not in explored:
                        dist[neighbor] = alt_cost
                        prev_parent[neighbor] = page

    return None  # return None since we didn't find a path


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
    #  bfs(source = "/wiki/Computer_science", goal = "/wiki/Computer_science") == ["/wiki/Computer_science"]
    #  bfs(source = "/wiki/Computer_science", goal = "/wiki/Computation") == ["/wiki/Computer_science", "/wiki/Computation"]
    # Find more in the test case file.

    # Do not try to make fancy optimizations here. The autograder depends on you following standard BFS and will check all of the pages you download.
    # Links should be inserted into the queue as they are located in the page, and should be obtained using Parser's get_links_in_page.
    # Be very careful not to add things to the "visited" set of pages too early. You must wait for them to come out of the queue first. See if you can figure out why.
    #  This applies for bfs, dfs, and dijkstra's.
    # Download a page with self.internet.get_page().
    def bfs(self, source="/wiki/Calvin_Li", goal="/wiki/Wikipedia"):
        path = [source]

        dummy_cost_fn = lambda x, y: 1
        found_path = find_path(self.internet, self.myqueue, source, goal, dummy_cost_fn)

        if found_path is None:
            return None

        if found_path[0] != path[0]:
            path.extend(found_path)

        path.append(goal)
        return path  # if no path exists, return None


class DFSProblem:
    def __init__(self):
        self.internet = Internet()
        self.myqueue = LifoQueue()

    # Links should be inserted into a stack as they are located in the page. Do not add things to the visited list until they are taken out of the stack.
    def dfs(self, source="/wiki/Calvin_Li", goal="/wiki/Wikipedia"):

        path = [source]

        dummy_cost_fn = lambda x, y: 1
        found_path = find_path(self.internet, self.myqueue, source, goal, dummy_cost_fn)

        if found_path is None:
            return None

        if found_path is not None and found_path[0] != path[0]:
            path.extend(found_path)

        path.append(goal)

        print("RIGHT BEFORE THE RETURN DFS!!!!!! ", path)
        return path  # if no path exists, return None


class DijkstrasProblem:
    def __init__(self):
        self.internet = Internet()
        self.count = 0
        self.myqueue = PriorityQueue()

    def increment(self):
        temp_count = self.count
        self.count = self.count + 1
        return temp_count

    # Links should be inserted into the heap as they are located in the page.
    # By default, the cost of going to a link is the length of a particular destination link's name. For instance,
    #  if we consider /wiki/a -> /wiki/ab, then the default cost function will have a value of 8.
    # This cost function is overridable and your implementation will be tested on different cost functions. Use costFn(node1, node2)
    #  to get the cost of a particular edge.
    # You should return the path from source to goal that minimizes the total cost. Assume cost > 0 for all edges.
    def dijkstras(self, source="/wiki/Calvin_Li", goal="/wiki/Wikipedia", costFn=lambda x, y: len(y)):

        self.myqueue.queue.clear()

        path = [source]
        found_path = find_path(self.internet, self.myqueue, source, goal, costFn)

        if found_path is None:
            return None

        if found_path[0] != path[0]:
            path.extend(found_path)

        path.append(goal)
        return path  # if no path exists, return None


class WikiracerProblem:
    def __init__(self):
        self.internet = Internet()

    # Time for you to have fun! Using what you know, try to efficiently find the shortest path between two wikipedia pages.
    # Your only goal here is to minimize the total amount of pages downloaded from the Internet, as that is the dominating time-consuming action.

    # Your answer doesn't have to be perfect by any means, but we want to see some creative ideas.
    # One possible starting place is to get the links in `goal`, and then search for any of those from the source page, hoping that those pages lead back to goal.

    # Note: a BFS implementation with no optimizations will not get credit, and it will suck.
    # You may find Internet.get_random() useful, or you may not.

    def wikiracer(self, source="/wiki/Calvin_Li", goal="/wiki/Wikipedia"):
        path = [source]
        # YOUR CODE HERE
        # ...
        path.append(goal)
        return path  # if no path exists, return None


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
