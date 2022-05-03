from collections import defaultdict
from queue import LifoQueue, Queue, PriorityQueue
from re import Match

from py_wikiracer.internet import Internet
from typing import List
import re
import heapq
import random
import sys


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
        # TODO - change this to not use regex and to do it in few operations as possible.
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

        path = self._bfs(source, goal)

        if path is None or (len(path) == 1 and path[0] == source):
            return None

        path.append(goal)
        return path  # if no path exists, return None

    def _bfs(self, source, goal):
        if source == goal:  # if source and goal are the same return
            return None
        Q = Queue()  # let Q be a queue
        prev = defaultdict(list)  # store the previous nodes in the path
        discovered = {source}  # label root as visited
        Q.put(source)
        count = 0
        while not Q.empty():
            v = Q.get()

            if v == goal:  # Search goal node, check for our goal and if we met it return our path
                prev[v].append(v)
                return prev[v]

            v_source_html = self.internet.get_page(v)
            edges = Parser.get_links_in_page(v_source_html)
            for w in edges:

                if w == goal:  # Search goal node, check for our goal and if we met it return our path
                    prev[v].append(v)
                    return prev[v]

                if w not in discovered:
                    discovered.add(w)
                    Q.put(w)
                    prev[w].append(v)
            count = count + 1
        return None


class DFSProblem:
    def __init__(self):
        self.internet = Internet()

    # Links should be inserted into a stack as they are located in the page. Do not add things to the visited list until they are taken out of the stack.
    def dfs(self, source="/wiki/Calvin_Li", goal="/wiki/Wikipedia"):
        path = [source]

        path = self._dfs(source, goal)

        if path is None or (len(path) == 1 and path[0] == source):
            return None

        path.append(goal)
        return path  # if no path exists, return None

    def _dfs(self, source, goal):
        if source == goal:  # source and goal are the same
            return None
        S = LifoQueue()  # let S be a stack
        prev = defaultdict(list)  # store the previous nodes in the path
        visited = {source}  # label root as visited
        S.put(source)
        count = 0
        while not S.empty():
            v = S.get()
            if v == goal:  # Search goal node, check for our goal and if we met it return our path
                prev[v].append(v)
                return prev[v]
            v_source_html = self.internet.get_page(v)
            edges = Parser.get_links_in_page(v_source_html)
            for w in edges:
                if w == goal:  # Search goal node, check for our goal and if we met it return our path
                    prev[v].append(v)
                    return prev[v]

                if w not in visited:
                    visited.add(w)
                    S.put(w)
                    prev[w].append(v)
            count = count + 1
        return None


class DijkstrasProblem:
    def __init__(self):
        self.internet = Internet()
        self.count = 0

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
        path = [source]
        # path = self._dijkstras(source, goal, costFn)
        path = self._find_path(source, goal, costFn, path)
        print("THIS IS THE RETURNED PATH = ", path)

        if path is None or (len(path) == 1 and path[0] == source):
            return None

        path.append(goal)
        return path  # if no path exists, return None

    # distances[start] = 0
    # vertices_to_explore = [(0, start)]
    #
    # while vertices_to_explore:
    #     current_distance, current_vertex = heappop(vertices_to_explore)
    #     for neighbor, edge_weight in graph[current_vertex]:
    #         new_distance = current_distance + edge_weight
    #         if new_distance < distances[neighbor]:
    #             distances[neighbor] = new_distance
    #             heappush(vertices_to_explore, (new_distance, neighbor))

    def _dijkstras(self, source, goal, cost_function):
        if source == goal:  # if source and goal are the same return
            return None

        pq = PriorityQueue()

        total_costs = {source: 0}
        prev = defaultdict(list)  # store the previous nodes in the path

        visited = {source}  # visited nodes set label root as visited
        pq.put((0, self.increment(), source))  # # setting the start node cost to zero add the starting node to the priority queue

        count = 0
        while not pq.empty() or count < 2:  # until the queue is empty we continue processing
            cost_new_smallest, _, new_smallest = pq.get()  # removes the smallest item from the queue
            print("element popped off of min pq: ", new_smallest, " cost of element: ", cost_new_smallest)

            if new_smallest == goal:  # Search goal node, check for our goal and if we met it return our path
                print("found goal! ", goal)
                return prev[new_smallest]

            for neighbor in Parser.get_links_in_page(self.internet.get_page(new_smallest)):  # check on the neighbors
                # if neighbor == goal:  # Search goal node, check for our goal and if we met it return our path
                #     print("found goal! ", new_smallest, neighbor, prev[neighbor])
                #     return prev[neighbor]
                if neighbor not in visited:  # check if the node has been visited already
                    edge_weight = cost_function(new_smallest, neighbor)
                    alt = cost_new_smallest + edge_weight
                    dist_neighbor = self.get_dist(neighbor, total_costs)
                    # dist_neighbor = max(dist_neighbor, alt)
                    # print("checking neighbor of ", neighbor, " with a cost of ", edge_weight, " alt dist ",
                    #       alt, "dist_neighbor ", dist_neighbor)
                    if alt < dist_neighbor or dist_neighbor == 0:
                        # print("visiting neighbor ", neighbor)
                        visited.add(neighbor)
                        total_costs[neighbor] = alt
                        prev[neighbor].append(new_smallest)
                        print("adding the neighbor", neighbor, " to the min pq with cost of ", alt)
                        pq.put((alt, self.increment(), neighbor))

                    # pq_cost_neighbor_tuple = (edge_weight, self.increment(), neighbor)
                    # pq.put(pq_cost_neighbor_tuple)
                    #
                    # cost_of_new_smallest = total_costs[new_smallest]
                    # if not cost_of_new_smallest:
                    #     cost_of_new_smallest = 0
                    #
                    # alt_path_distance = cost_of_new_smallest + edge_weight  # make a path containing the new path distance
                    #
                    # if neighbor not in total_costs.keys():
                    #     total_costs[neighbor] = 0
                    #
                    # if alt_path_distance < total_costs[neighbor]:  # check if new path is better than existing
                    #     total_costs[neighbor] = alt_path_distance  # updates the path length of the neighbor
                    #     prev[neighbor].append(new_smallest)

                    # if neighbor == goal:  # Search goal node, check for our goal and if we met it return our path
                    #     print("found goal! ", new_smallest, neighbor, prev[new_smallest])
                    #     return prev[new_smallest]
                    # visited.add(neighbor)
                    # pq_cost_neighbor_tuple = (cost_f_value, self.increment(), neighbor)
                    # # if (w in expected_result):
                    # pq.put(pq_cost_neighbor_tuple)

            count = count + 1
            # print("popped off the queue! ", v, count)
            # if v == goal:  # Search goal node, check for our goal and if we met it return our path
            #     prev[v].append(v)
            #     return prev[v]
            #
            # # TODO - do something here before we

        # sys.stdout.close()
        return None

    def get_dist(self, neighbor, total_costs):
        total_cost_neighbor = 0
        if neighbor in total_costs:
            total_cost_neighbor = total_costs[neighbor]
        return total_cost_neighbor

    def _find_path(self, source, goal, cost_fn, path: []):
        pq : Queue = PriorityQueue()
        pq.put((0, source))
        explored = set()

        # cost_table = dict()
        page_graph = defaultdict(list)
        prev_parent = dict()
        prev_parent[source] = None

        while not pq.empty():
            cost, page = pq.get()
            if page not in explored:
                explored.add(page)
                for neighbor in Parser.get_links_in_page(self.internet.get_page(page)):
                    if neighbor == goal:
                        path = self.backtrack_path(page_graph, prev_parent, page, path)
                        return path

                    # keep track of the cost in the page graph
                    page_graph[neighbor].append((cost + cost_fn(page, neighbor), page))

                    # never reset the source node
                    if neighbor != source:
                        prev_parent[neighbor] = page

                    pq.put((cost + cost_fn(page, neighbor), neighbor))

        return path

    def backtrack_path(self, page_graph: defaultdict, prev_parent: dict, page, path: []):
        current_ptr = page
        path_backwards = [current_ptr]
        PAGE_INDEX = 1
        while current_ptr is not None:
            smallest_parent = min(page_graph[current_ptr])[PAGE_INDEX]
            if prev_parent[smallest_parent] is None:
                break
            next_parent = prev_parent[smallest_parent]
            path_backwards.append(next_parent)
            current_ptr = next_parent

        # reverse the backwards path to forwards now
        path.extend(list(reversed(path_backwards)))
        print("final final final ", path)
        return path




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
