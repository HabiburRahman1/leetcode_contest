# 6211. Create Components With Same Value
# There is an undirected tree with n nodes labeled from 0 to n - 1.

# You are given a 0-indexed integer array nums of length n where nums[i] represents the value of the ith node. You are also given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

# You are allowed to delete some edges, splitting the tree into multiple connected components. Let the value of a component be the sum of all nums[i] for which node i is in the component.

# Return the maximum number of edges you can delete, such that every connected component in the tree has the same value.

# Input: nums = [6,2,2,2,6], edges = [[0,1],[1,2],[1,3],[3,4]] 
# Output: 2 
# Explanation: The above figure shows how we can delete the edges [0,1] and [3,4]. The created components are nodes [0], [1,2,3] and [4]. The sum of the values in each component equals 6. It can be proven that no better deletion exists, so the answer is 2.

# Input: nums = [2], edges = []
# Output: 0
# Explanation: There are no edges to be deleted.

class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        s = sum(nums)
        if s % n != 0:
            return -1
        t = s // n
        if t in nums:
            return n - 1
        else:
            return nums.count(t) + 1
        
        