from py_wikiracer.internet import Internet
from py_wikiracer.wikiracer import Parser

internet = Internet()
page = internet.get_page("/wiki/Altoids")
categories = Parser.get_related_category_links(page)

for c in categories:
    print("category: ", c)

