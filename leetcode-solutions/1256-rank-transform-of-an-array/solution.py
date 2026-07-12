class Solution(object):
    def arrayRankTransform(self, arr):
        sorted_unique = sorted(set(arr))
        rank_map = {val: idx + 1 for idx, val in enumerate(sorted_unique)}
        return [rank_map[val] for val in arr] 
        
