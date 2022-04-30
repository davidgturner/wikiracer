from queue import PriorityQueue

pq = PriorityQueue()

pq.put((0.99, "Z"))
pq.put((0.12, "A"))
pq.put((0.68, "M"))
pq.put((0.50, "M"))
# pq.put((0.05, "M"))

value = pq.get()
print(value[1])
print(pq.qsize())

value = pq.get()
print(pq.qsize())