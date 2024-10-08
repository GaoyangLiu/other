class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        pivot_index = random.randint(0, len(nums) - 1)
        pivot = nums[pivot_index]

        le = [x for x in nums if x < pivot]
        eq = [x for x in nums if x == pivot]
        rt = [x for x in nums if x > pivot]

        return self.sortArray(le) + eq + self.sortArray(rt)
