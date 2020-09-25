class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, x):
        heap = self.heap
        heap.append(x)
        i = len(heap) - 1
        while i > 0:
            j = (i - 1) // 2
            y = heap[j]
            if y <= x:
                return
            heap[j],heap[i] = x, y
            i = j 

    def remove(self):


###########################################################################

pq = PriorityQueue()
pq.insert(4)
pq.insert(2)
pq.insert(5)
pq.insert(3)
pq.insert(2)
pq.insert(1)
pq.insert(6)
pq.insert(3)
output = []
while pq:
    output.append(pq.remove())
print(output)

###########################################################################

from heapq import heappush, heappop
heap = []
heappush(heap, 4)
heappush(heap, 2)
heappush(heap, 5)
heappush(heap, 3)
heappush(heap, 2)
heappush(heap, 1)
heappush(heap, 6)
heappush(heap, 3)
output = []
while heap:
    output.append(heappop(heap))
print(output)
