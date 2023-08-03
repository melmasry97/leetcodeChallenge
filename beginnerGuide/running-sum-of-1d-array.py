import sys

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
          # commen solution
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums

        # the other solution for [ time , space ] complaxty

        # res=[]
        # temp=0

        # for i in range(len(nums)):
        #     temp=temp+nums[i]
        #     res.append(temp)
        # return res
    
if __name__ == "__main__":
    # The first argument (sys.argv[0]) is the script name itself, so we ignore it.
    args = sys.argv[1:]


    # Convert the command-line arguments to integers
    nums = [int(arg) for arg in args]

    # Create an instance of the Solution class
    solution = Solution()

    # Call the runningSum method on the instance
    result = solution.runningSum(nums)
    print(result)