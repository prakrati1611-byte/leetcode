class Solution(object):
    def subarraySum(self, nums, k):
        sum=0
        count=0
        sum_counts={0:1}

        for num in nums:
            sum+=num
            if sum-k in sum_counts:
                count+=sum_counts[sum-k]
            sum_counts[sum]=sum_counts.get(sum,0)+1
        return count
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
