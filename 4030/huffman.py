"""
Huffman codes.
Author and copyright: Thomas Watson, 2019
License: For use only in COMP 4030: Design and Analysis of Algorithms,
         University of Memphis
"""

from heapq import heappush, heappop, heapify

def huffman(letters):
    """
    letters is a list of at least two (frequency, character) pairs.
    Returns an optimal code as a list of (binary code string, character) pairs,
    sorted in lexicographic order of the code (not the original order the
    letters were presented in).
    """

    # Create a priority queue out of the letters, sorted by frequency (which
    # is the 0-th component). Calling heapify is more efficient than
    # iteratively inserting each of the letters.
    heap = letters
    heapify(heap)

    # Iteratively take the two least frequent letters (either of which may
    # be a meta-letter) and merge them into a meta-letter, which is represented
    # as a triple (combined frequency, tuple for 1st letter, tuple for 2nd).
    # Thus we'll get nested tuples, giving an overall tree structure.
    while len(heap) > 1:
        y = heappop(heap)
        z = heappop(heap)
        heappush(heap, (y[0] + z[0], y, z))

    # heap[0] is now the root of the tree representing the code. The flatten
    # method creates a list of [binary code string, character] lists from the
    # tree---using lists instead tuples for pairs, since mutability of lists
    # makes it easier to implement. Just convert to tuples before returning.
    ret = flatten(heap[0])
    for i in range(len(ret)):
        ret[i] = tuple(ret[i])
    return ret

def flatten(root):
    """
    Flattens the tree by recursively converting it to a list. Each entry
    represents a leaf (original letter), and the binary code string is the
    concatenation of 0's representing left and 1's representing right, along
    the root-to-leaf path.
    """

    # If the tuple representing the node has length 2, then it's an original
    # letter (with 0-th component = frequency, 1-st component = character).
    if len(root) == 2:
        return [['', root[1]]]

    # Recursively flatten the left and right subtrees. By the way, root[0] is
    # the "frequency" of this meta-letter, which is not relevant anymore.
    left = flatten(root[1])
    right = flatten(root[2])

    # All leaves (original letters) in the left subtree should have 0
    # prepended to their code strings. (Similarly, 1 for right subtree.)
    for x in left:
        x[0] = '0' + x[0]
    for x in right:
        x[0] = '1' + x[0]
    return left + right

###############################################################################

example = [(0.32, 'a'), (0.25, 'b'), (0.20, 'c'), (0.18, 'd'), (0.05, 'e')]
print(huffman(example))
# Should print
# [('00', 'c'), ('010', 'e'), ('011', 'd'), ('10', 'b'), ('11', 'a')].
