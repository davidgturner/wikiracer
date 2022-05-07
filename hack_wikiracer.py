from py_wikiracer.wikiracer import DijkstrasProblem, BFSProblem, DFSProblem, WikiracerProblem

# source = "/wiki/Calvin_Li"
# goal = "/wiki/Wikipedia"

# source = "/wiki/Calvin_Li"
# goal = "/wiki/Quebecor"

source =  "/wiki/Computer_science"
goal = "/wiki/Richard_Soley"


# source = "/wiki/ASDF"
# goal = "/wiki/ASDF"

# == ["/wiki/ASDF", "/wiki/ASDF"]
wr_problem = WikiracerProblem()
wr_path = wr_problem.wikiracer(source, goal)
print("WikiRacer path=", wr_path)

# dummy_cost_func = lambda y, x: 1
# cost_func = lambda y, x: len(x) * 1000 + x.count("a") * 100  + x.count("u") + x.count("h") * 5 - x.count("F")

# expected Dijkstra
# ['/wiki/Calvin_Li', '/wiki/Main_Page', '/wiki/Wikipedia']
# dij_path = dij.dijkstras(source, goal, cost_func)


# expected DFS
# ['/wiki/Calvin_Li', '/wiki/Main_Page', '/wiki/Wikipedia']
# dfs_path = dfs.dfs(source, goal)
# print("DFS Path= ", dfs_path)

# expected BFS
# ['/wiki/Calvin_Li', '/wiki/Chinese_language', '/wiki/Wikipedia']
# bfs_path = bfs.bfs(source, goal)
# print("BFS Path ", bfs_path)

# DFS complex
# assert dfs.dfs(source = "/wiki/Calvin_Li", goal = "/wiki/Quebecor") == ['/wiki/Calvin_Li', '/wiki/Main_Page', '/wiki/Wikimedia_Foundation', '/wiki/VIAF_(identifier)', '/wiki/Virtual_International_Authority_File', '/wiki/Interested_Parties_Information', '/wiki/Law', '/wiki/Human_science', '/wiki/Truth', '/wiki/Verstehen', '/wiki/Phronesis', '/wiki/Knowledge', '/wiki/Max_Weber', '/wiki/Trove_(identifier)', '/wiki/Trove', '/wiki/The_Sydney_Morning_Herald', '/wiki/OzTAM', '/wiki/Canwest', '/wiki/Pembroke_Daily_Observer', '/wiki/Postmedia_News', '/wiki/Postmedia_Network', '/wiki/Dose_(magazine)', '/wiki/Northern_News', '/wiki/Jam!', '/wiki/Quebecor']
# assert dfs.internet.requests == ['/wiki/Calvin_Li', '/wiki/Main_Page', '/wiki/Wikimedia_Foundation', '/wiki/VIAF_(identifier)', '/wiki/Virtual_International_Authority_File', '/wiki/Interested_Parties_Information', '/wiki/Law', '/wiki/Human_science', '/wiki/Truth', '/wiki/Verstehen', '/wiki/Phronesis', '/wiki/Knowledge', '/wiki/Max_Weber', '/wiki/Trove_(identifier)', '/wiki/Trove', '/wiki/The_Sydney_Morning_Herald', '/wiki/OzTAM', '/wiki/Canwest', '/wiki/Pembroke_Daily_Observer', '/wiki/Postmedia_News', '/wiki/Postmedia_Network', '/wiki/Dose_(magazine)', '/wiki/Northern_News', '/wiki/Jam!']

# source2 = "/wiki/Calvin_Li"
# goal2 = "/wiki/Quebecor"
# dfs_complex_path = dfs.dfs(source2, goal2)
# print("DFS Complex Path ", dfs_complex_path)
