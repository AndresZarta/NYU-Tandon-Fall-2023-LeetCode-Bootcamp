from collections import deque

class Solution:
    ## Strategy: Use a double-ended queue to maintain the indices of the elements inside
    ## the sliding window. 
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximum_double_queue = deque()
        resulting_list = []
        
        start, end = 0, 0

        while end < len(nums):

            ## Remove indices of smaller elements  
            while maximum_double_queue and nums[maximum_double_queue[-1]] < nums[end]:
                maximum_double_queue.pop()

            maximum_double_queue.append(end)

            # When window size is larger than k, slide instead
            if end - start  == k - 1:
                resulting_list.append(nums[maximum_double_queue[0]])

                if maximum_double_queue and maximum_double_queue[0] == start:
                    maximum_double_queue.popleft()
                start += 1
            end += 1

        return resulting_list
