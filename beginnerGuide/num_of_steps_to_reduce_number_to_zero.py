import sys


class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        iteration = 0
        while num > 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num - 1
            iteration = iteration + 1
        
        return iteration
if __name__ == "__main__":
    # The first argument (sys.argv[0]) is the script name itself, so we ignore it.
    # The second argument (sys.argv[1]) is the number we want to process.

    # Check if exactly one argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <integer>")
        sys.exit(1)

    # Convert the command-line argument to an integer
    nums = int(sys.argv[1])

    # Create an instance of the Solution class
    solution = Solution()

    # Call the numberOfSteps method on the instance
    result = solution.numberOfSteps(nums)

    # Print the result
    print(result)