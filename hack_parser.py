import re

from py_wikiracer.internet import Internet
from py_wikiracer.wikiracer import Parser, invalid_url_pattern, get_text_portion, WikiracerProblem

internet = Internet()

# topic_message = "AMGParade"
#
# invalid = [":", "#", "/", "?"]
# concat_str = ''. join(invalid)
# re1 = re.compile(r"[" + concat_str + "`]")
# if re1.search(topic_message):
#     print ("RE1: Invalid char detected. ")


source = "/wiki/Computer_science"  # "/wiki/Calvin_Li" # "/wiki/Nashville,_Tennessee" # "/wiki/Athlon_Sports"  # "/wiki/Fiji"
text_test = get_text_portion(source)
goal = "/wiki/Richard_Soley"

v_goal_html = internet.get_page(goal)
goal_edges = Parser.get_links_in_page(v_goal_html)

# /wiki/Richard_Soley

# print(text_test)
#
# # text_test = "Athlon_Sports"
#
# if invalid_url_pattern(text_test, Internet.DISALLOWED):
#     print("disallowed")
# else:
#     print("allowed")

v_source_html = internet.get_page(source)
edges = Parser.get_links_in_page(v_source_html)



# print(edges[0])

# costFn = lambda y, x: len(x) * 1000 + x.count("a") * 100 + x.count("u") + x.count("h") * 5 - x.count("F")

wr = WikiracerProblem()
wr.populate_goal_links(goal)

#h = wr.h_cost

# edges = sorted(edges)

tuple_list = []

for e in edges:
    # print("edge ", e, " cost: ", )
    tuple_list.append((wr.h_score(source, e, source, goal), e))

tuple_list = sorted(tuple_list)
for t in tuple_list:
    print("cost score / page link ", t)
    # tuple_list.append((wr.h_score(source, e, source, goal), e))
