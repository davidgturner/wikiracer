import re

from py_wikiracer.internet import Internet
from py_wikiracer.wikiracer import Parser, invalid_url_pattern, get_text_portion

internet = Internet()

# topic_message = "AMGParade"
#
# invalid = [":", "#", "/", "?"]
# concat_str = ''. join(invalid)
# re1 = re.compile(r"[" + concat_str + "`]")
# if re1.search(topic_message):
#     print ("RE1: Invalid char detected. ")


source = "/wiki/Nashville,_Tennessee" # "/wiki/Athlon_Sports"  # "/wiki/Fiji"
text_test = get_text_portion(source)

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

print(edges[0])

# for e in edges:
#     print("edge ", e)

