

import heapq



def kLargest(a, k):

    heap = []

    for num in a:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]


print("klargest",kLargest([1,6,2,9,10], 2))


def kSmallest(a, k):

    heap = []

    for num in a:
        heapq.heappush(heap, -num)

        if len(heap) > k:
            heapq.heappop(heap)
    

    return -heap[0]


print("ksmallest",kSmallest([1,6,2,9,10], 2))