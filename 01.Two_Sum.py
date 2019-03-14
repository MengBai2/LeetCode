# Two Sum

# return indices of the two numbers with summation equals to a specific target.

class Solution:
	def twoSum(self, nums,target):

		"""
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum_map = {}
        for index,value in enumerate(nums):
        	sum_map[value] = index

        for index1,value in enumerate(nums):
        	if target - value in sum_map:
        		index2 = sum_map[target - value]
        		if index1 ! = index2:
        			return [index1,index2]

        			