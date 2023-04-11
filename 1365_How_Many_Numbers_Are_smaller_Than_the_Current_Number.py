"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ans = []
        for i in nums:
            count = 0
            for j in nums:
                if i > j:
                    count += 1
            ans.append(count)
        return ans

if __name__ == "__main__":
    test = Solution()
    ans = test.smallerNumbersThanCurrent([8,1,2,2,3])
    print(ans)
