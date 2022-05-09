from py_wikiracer.wikiracer import DijkstrasProblem, BFSProblem, DFSProblem, WikiracerProblem

wr_problem = WikiracerProblem()
# wr_problem.build_ignore_pages_set(5)
# print(wr_problem.ignore_pages)


def process_race(src, goal):
    if src and not src.startswith("/wiki/"):
        src = "/wiki/" + src

    if goal and not goal.startswith("/wiki/"):
        goal = "/wiki/" + goal

    wr_path = wr_problem.wikiracer(src, goal)
    num_downloads = len(wr_problem.internet.requests)
    return wr_path, num_downloads

tests = [
    #("Willard_Boyle", "Light-dragging_effects"),
    ("Computer_science", "Richard_Soley"),
]

for t in tests:
    wp, nd = process_race(t[0], t[1])
    print(t, ": ", nd, wp)
