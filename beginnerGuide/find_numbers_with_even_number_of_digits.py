import sys


class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        evenDigitsNumber = 0 
        
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0 :
                evenDigitsNumber += 1
                
            else:
                continue
        return evenDigitsNumber


if __name__ == "__main__":
    # The first argument (sys.argv[0]) is the script name itself, so we ignore it.
    # The second argument (sys.argv[1]) is the number we want to process.

    # Check if exactly one argument is provided
    if len(sys.argv) <= 2:
        print("Usage: python script_name.py <integer>")
        sys.exit(1)

    # Convert the command-line argument to an integer
    args = sys.argv[1:]

    # Convert the command-line arguments to integers
    nums = [int(arg) for arg in args]
    print(nums)
    # Create an instance of the Solution class
    solution = Solution()

    # Call the numberOfSteps method on the instance
    result = solution.findNumbers(nums)

    # Print the result
    print(result)
