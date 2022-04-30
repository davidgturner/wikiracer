from collections import deque, defaultdict
from queue import Queue, LifoQueue, PriorityQueue

from py_wikiracer.internet import Internet
from py_wikiracer.wikiracer import Parser

internet = Internet()


def bfs_search(source_rel_url, goal_rel_url):
    if source_rel_url == goal_rel_url:  # source and goal are the same
        return

    prev = defaultdict(list)  # store the previous nodes in the path

    visited = {source_rel_url}  # label root as visited

    queue = deque([])
    queue.append(source_rel_url)

    while queue:
        v = queue.popleft()  # dequeue from the queue
        print("popping off ", v)
        if v == goal_rel_url:  # Search goal node, check for our goal and if we met it return our path
            print("found. goal is met ", v)
            return prev[v]

        v_source_html = internet.get_page(v)
        edges = Parser.get_links_in_page(v_source_html)
        # print("edges of ", v, " are ", edges)
        edges = set(edges)

        for w in edges:

            if v == goal_rel_url:  # Search goal node, check for our goal and if we met it return our path
                print("found. goal is met ", v)
                return prev[v]

            if w not in visited:
                # print("v, getting page for it ", v)
                print("not visited yet adding w = ", v)
                visited.add(w)
                queue.append(w)
                # prev[w] = v
                prev[w].append(v)
                # print("printing state of visited set = ", visited)
                # print("printing state of queue = ", queue)

    return []  # no path is found


source = "/wiki/Calvin_Li"
goal = "/wiki/Meteor_Garden"

# bfs_path = bfs_search(source, goal)
# print(bfs_path)

# v_source_html = internet.get_page(source)
# edges = Parser.get_links_in_page(v_source_html)
#
# for e in edges:
#     print("edges 1st page: ", e)

