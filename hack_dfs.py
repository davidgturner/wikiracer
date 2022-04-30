from collections import defaultdict
from queue import Queue, LifoQueue, PriorityQueue

from py_wikiracer.internet import Internet
from py_wikiracer.wikiracer import Parser

internet = Internet()

# # Initialize LIFO Queue
# LIFOq = queue.LifoQueue(maxsize=3)

# procedure DFS_iterative(G, v) is
#     let S be a stack
#     S.push(iterator of G.adjacentEdges(v))
#     while S is not empty do
#         if S.peek().hasNext() then
#             w = S.peek().next()
#             if w is not labeled as discovered then
#                 label w as discovered
#                 S.push(iterator of G.adjacentEdges(w))
#         else
#             S.pop()

def dfs_search(src, goal) -> []:
    if src == goal:  # source and goal are the same
        return
    S = LifoQueue()  # let S be a stack

    prev = defaultdict(list)  # store the previous nodes in the path

    discovered = {src}  # label root as visited
    S.put(src)
    count = 0
    # path = []
    while S:  # and count < 3:
        v = S.get()
        print("next item off the top of the stack ", v)
        # path.append(v)
        if v == goal:  # Search goal node, check for our goal and if we met it return our path
            print("in first goal check. found goal ", v, " with a depth of ", count)
            # return v
            return prev[v]

        v_source_html = internet.get_page(v)
        edges = Parser.get_links_in_page(v_source_html)
        for w in edges:
            if w == goal:  # Search goal node, check for our goal and if we met it return our path
                print("in edges found goal ", w, " with a depth of ", count)
                prev[v].append(v)
                return prev[v]

            print("trying edge for ", w, " based on it being a neighbor of ", v, " count = ", count)
            if w not in discovered:
                discovered.add(w)
                S.put(w)
                # prev[w].append(v)
                prev[w].append(v)

        count = count + 1
    return []  # no path is found


source = "/wiki/Calvin_Li" # "/wiki/Athlon_Sports" # "/wiki/Yar_Mohammad_Khan_Alakozai"  # /wiki/Fiji" # "/wiki/Calvin_Li"
goal = "/wiki/Wikipedia" # "/wiki/Nashville_(disambiguation)" # "/wiki/Farsi_(disambiguation)"  # "/wiki/Main_Page"  # "/wiki/Persian_language"  # "/wiki/Fiji_(disambiguation)" # "wiki/Austronesian_languages"
path = dfs_search(source, goal)

print("path taken: ", path)