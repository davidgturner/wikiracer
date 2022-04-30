from collections import defaultdict

from py_wikiracer.internet import Internet
from py_wikiracer.wikiracer import DijkstrasProblem
from py_wikiracer.wikiracer import Parser, BFSProblem, DFSProblem, DijkstrasProblem, WikiracerProblem


# d = DijkstrasProblem()
# ll = d.dijkstras("/wiki/Calvin_Li", "/wiki/Wikipedia")
# print("LL = ", ll)

# test_parser()

# internet = Internet()
# source = "/wiki/Richard_Soley"
#
# html = internet.get_page(source)
# print(html[:2000])
#
# links = []
# pos = 0
#
# while True:
#     pos = html.find('/href="/wiki/', pos)
#     if pos < 0:
#         break
#     end = html.find('"', pos + 6)
#     page_name = html[pos + 6:end]
#     # not any ch
#     links.append(page_name)
#     pos = end

# source = "/wiki/A"


# class Graph:
#     def __init__(self, n):
#         self.nodes = set(range(n))
#         self.edges = defaultdict(list)
#         self.weights = {}
#
#     def add_edge(self, from_node, to_node, distance):
#         self.edges[from_node].append(to_node)
#         self.weights[from_node, to_node] = distance

# ## BFS ###
# def bfs(src, goal):
#     # let Q be a queue
#     Q = []  # [source]
#
#     # label root as explored
#     explored = { source }
#
#     # Q.enqueue(root)
#     Q.append(source)
#
#     # while Q is not empty do
#     while Q:
#         # v := Q.dequeue()
#         v = Q.pop(0)
#         # if v is the goal then
#         if v == goal:
#             return v
#         # for all edges from v to w in G.adjacentEdges(v) do
#         # for n in
#         for w in neighbors:
#             if w is not labeled as explored then
#                 label w as explored
#                 # Q.enqueue(w)
#                 Q.append(w)


def bfs_search(source_node, goal_node):
    prev = dict()
    path = []  # this path is what we need to return
    Q = [source_node]  # let Q be a queue initialized with source
    visited = {source_node } # {source_node}  # label root as explored

    # visited.add(source_node)
    v_source_html = internet.get_page(source_node)
    neighbors_of_visited = Parser.get_links_in_page(v_source_html)

    while len(Q) > 0:  # while Q is not empty do
        print("in loop ")
        v = Q.pop(0)  # v := Q.dequeue()
        print("popped off v ", v)

        # if v in visited:  # if v is the goal then
        #     print("v is already in explored. continuing.", "")
        #     continue  # return v

        visited.add(v)  # add to visited / explored set
        print("now visiting: ", v)

        v_source_html = internet.get_page(v)
        neighbors_of_visited = Parser.get_links_in_page(v_source_html)
        print("neighbors_of_visited ", neighbors_of_visited)
        for n in neighbors_of_visited:
            # print("neighbor ", n)
            if n == goal_node:
                print("hit goal node of ", n)
                prev[n] = v
                visited.add(goal_node)
                return visited
            if n not in visited:
                Q.append(n)
                prev[n] = v


if __name__ == '__main__':
    # g = Graph(5) # holds 1, 2, 3, 4
    # g.add_edge("1", "2", 10)
    # g.add_edge("1", "5", 100)
    # g.add_edge("1", "4", 30)
    # g.add_edge("2", "3", 50)
    # g.add_edge("3", "5", 10)
    # g.add_edge("4", "5", 60)
    # g.add_edge("4", "3", 20)

    internet = Internet()

    # source_1 = "/wiki/A"
    # source_2 = "/wiki/Richard_Soley"
    source = "/wiki/Calvin_Li"  # "/wiki/Reese_Witherspoon" # "/wiki/Henry_Krumrey"
    # source_html = internet.get_page(source)  # internet.get_page("/wiki/Henry_Krumrey")
    # print("source html ", source_html)
    # source_html = internet.get_page(source_2)
    # print(html[:2000])
    goal = "/wiki/Wikipedia"  # "/wiki/Academy_Award" # "/wiki/Adolf_Hitler"

    # src_links = Parser.get_links_in_page(source_html)
    # print("source links ", src_links)

    visited_nodes = bfs_search(source, goal)

    # print("prev: ", prev)
    print("explored: ", visited_nodes)
