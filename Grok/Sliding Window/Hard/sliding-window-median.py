import heapq
class Solution(object):
    def push_heaps(self, upper, lower, num):
        heapq.heappush(lower, -heapq.heappushpop(upper, num))
        
        if len(lower) > len(upper):
            heapq.heappush(upper, -heapq.heappop(lower))
    
    def medianSlidingWindow(self, nums, k):

        left = 0
        right = 0
        upper_heap = []
        lower_heap = []
        out = []

        while right < len(nums):
            self.push_heaps(upper_heap, lower_heap, nums[right])

            if right + 1 - left == k:
                if len(upper_heap) == len(lower_heap):
                    out.append((upper_heap[0] + (-lower_heap[0]))/2.0)
                else:
                    out.append(upper_heap[0])

                if k > 1 and -nums[left] >= lower_heap[0]:
                    index = lower_heap.index(-nums[left])
                    lower_heap[index] = lower_heap[-1]
                    del lower_heap[-1]
                    if index < len(lower_heap):
                        heapq._siftup(lower_heap, index)
                        heapq._siftdown(lower_heap, 0, index)
                else:
                    index = upper_heap.index(nums[left])
                    upper_heap[index] = upper_heap[-1]
                    del upper_heap[-1]
                    if index < len(upper_heap):
                        heapq._siftup(upper_heap, index)
                        heapq._siftdown(upper_heap, 0, index)
                
                left += 1


            right += 1

        return out