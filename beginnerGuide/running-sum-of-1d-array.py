class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sumList = 0
        for index in range(0, len(nums)):
            sumList +=  nums[index]
            nums[index] = sumList
        return nums