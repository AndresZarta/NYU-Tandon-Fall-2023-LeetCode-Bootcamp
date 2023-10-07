class Solution:
    def maxArea(self, height: List[int]) -> int:
        ## Strategy: Start with boundaries at the edges of the array and converge towards the center to find improvement.
        left_boundary = 0
        right_boundary = len(height) - 1
        left_boundary_val = height[left_boundary]
        right_boundary_val = height[right_boundary]
        max_water = 0

        while left_boundary < right_boundary:
            distance = right_boundary - left_boundary
            current_max_water = (distance * left_boundary_val) if left_boundary_val < right_boundary_val else (distance * right_boundary_val)

            if current_max_water > max_water:
                max_water = current_max_water

            ## Insight: it is safe to move the boundary that has the lowest height towards the center because if it is indeed involved
            ## in the solution, that movement would only reduce the water the newly formed container could hold.
            if left_boundary_val < right_boundary_val:
                left_boundary += 1
                left_boundary_val = height[left_boundary]
            else:
                right_boundary -= 1
                right_boundary_val = height[right_boundary]

        return max_water
