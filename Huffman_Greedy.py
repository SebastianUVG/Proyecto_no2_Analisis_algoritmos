import heapq


def huffman_greedy(freqs):

    if len(freqs) <= 1:
        return 0

    heap = freqs[:]
    heapq.heapify(heap)

    total = 0

    while len(heap) > 1:
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        z = x + y
        total += z
        heapq.heappush(heap, z)

    return total


