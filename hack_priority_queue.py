from queue import PriorityQueue

# # Z = 0
# costFunc = lambda y, x: i + 1
# # def costFunc(Z):
# #     Z = Z + 1
# #     return Z

# COUNT = 0
# def increment():
#     global COUNT
#     tempCount = COUNT
#     COUNT = COUNT + 1
#     return tempCount

costFn = lambda y, x: len(x) * 1000 + x.count("a") * 100 + x.count("u") + x.count("h") * 5 - x.count("F")

pq = PriorityQueue()
pq.put((costFn("a","b"), "Z"))
pq.put((costFn("a","b"), "A"))
pq.put((costFn("a","b"), "M"))
pq.put((costFn("a","b"), "N"))
pq.put((costFn("a","b"), "B"))

while not pq.empty():
    value = pq.get()
    print(value[1])

# print(increment())
# print(increment())
# print(increment())
# print(increment())
# print(increment())