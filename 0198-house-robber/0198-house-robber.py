class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums) # 배열이 2칸일 때 가장 큰 값 하나 반환
        
        dp = [0]*len(nums) # dp 리스트 초기화
        dp[0] = nums[0] # 첫 번째 집을 털 경우
        dp[1] = max(nums[0], nums[1]) # 첫 번째와 두 번째 집 중에서 더 많은 돈을 가진 집을 털 경우

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]) # 이전 집을 털었을 경우와 이전 이전 집을 털고 현재 집을 털 경우 중 큰 값을 선택

        return dp[-1]
        