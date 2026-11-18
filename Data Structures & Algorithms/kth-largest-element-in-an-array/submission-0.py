class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        nums_neg= [-nums[i] for i in range(len(nums))]
        heapq.heapify(nums_neg)
        while nums_neg and k>1:
            heapq.heappop(nums_neg)
            k-=1
        return nums_neg[0]*-1 if nums_neg else 0

        