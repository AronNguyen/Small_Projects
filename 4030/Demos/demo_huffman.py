from heapq import heappush, heappop, heapify

def huffman(letters):
    heap = letters
    heapify(heap)

    while len(heap) > 1:
        y = heappop(heap)
        z = heappop(heap)
        heappush(heap, (y[0] + z[0], y, z))

    # return heap[0]
    return flatten(heap[0])

def flatten(root):
    if len(root) == 2:
        return [['', root[1]]]

    left = flatten(root[1])
    right = flatten(root[2])

    for x in left:
        x[0] = '0' + x[0]
    for x in right:
        x[0] = '1' + x[0]

    return left + right

##############################################################################

example = [(0.32, 'a'), (0.25, 'b'), (0.20, 'c'), (0.18, 'd'), (0.05, 'e')]

print(huffman(example))
