import sys


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cons = 0
        maxCons = 0
        # nums = [1,1,0,1,1,1]
        for i in range(0,len(nums)):
            if nums[i] == 1:
                cons += 1
                maxCons = max(cons, maxCons)
            else:
                cons = 0
        return maxCons


if __name__ == "__main__":
    # The first argument (sys.argv[0]) is the script name itself, so we ignore it.
    # The second argument (sys.argv[1]) is the number we want to process.

    # Check if exactly one argument is provided
    if len(sys.argv) <= 2:
        print(len(sys.argv))
        print("Usage: python script_name.py <integer>")
        sys.exit(1)

    # Convert the command-line argument to an integer
    args = sys.argv[1:]

    # Convert the command-line arguments to integers
    nums = [int(arg) for arg in args]

    # Create an instance of the Solution class
    solution = Solution()

    # Call the numberOfSteps method on the instance
    result = solution.findMaxConsecutiveOnes(nums)

    # Print the result
    print(result)
