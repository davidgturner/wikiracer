from queue import PriorityQueue

# # Z = 0
# costFunc = lambda y, x: i + 1
# # def costFunc(Z):
# #     Z = Z + 1
# #     return Z

COUNT = 0
def increment():
    global COUNT
    tempCount = COUNT
    COUNT = COUNT + 1
    return tempCount

pq = PriorityQueue()
pq.put((increment(), "Z"))
pq.put((increment(), "A"))
pq.put((increment(), "M"))
pq.put((increment(), "N"))
pq.put((increment(), "B"))

while not pq.empty():
    value = pq.get()
    print(value[1])

# print(increment())
# print(increment())
# print(increment())
# print(increment())
# print(increment())