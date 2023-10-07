class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_of_nums = {}
        for num in nums:
            if num in dict_of_nums:
                return True
            else:
                dict_of_nums[num] = None

        return False
