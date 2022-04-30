from py_wikiracer.wikiracer import DijkstrasProblem, BFSProblem

dijk = DijkstrasProblem()
b = BFSProblem()

src = "/wiki/Calvin_Li"
goal = "/wiki/Wikipedia"

costFunc = costFn = lambda y, x: 1
path = dijk.dijkstras(src, goal, costFunc)

print(path)



