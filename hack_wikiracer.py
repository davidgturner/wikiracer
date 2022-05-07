from py_wikiracer.wikiracer import DijkstrasProblem, BFSProblem, DFSProblem, WikiracerProblem

wr_problem = WikiracerProblem()


def process_race(src, goal):
    if src and not src.startswith("/wiki/"):
        src = "/wiki/" + src

    if goal and not goal.startswith("/wiki/"):
        goal = "/wiki/" + goal

    wr_path = wr_problem.wikiracer(src, goal)
    num_downloads = len(wr_problem.internet.requests)
    return wr_path, num_downloads


# tests = [
# ('Jesus', 'Adolf_Hitler') 6
# ('Jesus', 'Mao_Zedong') 5
# ('Jesus', 'Johnny_Damon') 44
# ('Jesus', 'Chicago_Blackhawks') 10
#     ]

tests = [
    ("/wiki/Waakirchen", "/wiki/A"),
    # ('Jesus', 'Adolf_Hitler'),
    # ('Jesus', 'Mao_Zedong'),
    # ('Jesus', 'Johnny_Damon'),
    # ('Jesus', 'Chicago_Blackhawks'),
]

for t in tests:
    wp, nd = process_race(t[0], t[1])
    print(t, ": ", nd, wp)
