import heapq
from typing import List


def merge_k_lists(lists: List[List[int]]) -> List[int]:
    min_heap = []

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))

    result = []

    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        result.append(value)

        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))

    return result

