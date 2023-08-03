from ast import List


class Solution(object):

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0

        for customer in accounts:
            wealth = sum(customer)
            max_wealth = max(max_wealth, wealth)

        return max_wealth
    

main = '__main__':
    maxWealth =  Solution.maximumWealth([1,2,3], [1,2,3])
