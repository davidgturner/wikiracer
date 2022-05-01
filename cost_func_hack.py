costFn = lambda y, x: len(x) * 1000 + x.count("a") * 100 + x.count("u") + x.count("h") * 5 - x.count("F")

print(costFn("Fauh","uhFa"))
print(costFn("hauF","aFuh"))
print(costFn("auhF","uFah"))
print(costFn("Fuah","aFuh"))

