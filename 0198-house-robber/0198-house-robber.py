class Solution:
    def rob(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        if len(nums) <= 2:
            return max(nums) # 배열이 2칸일 때 가장 큰 값 하나 반환
        
        dp = [0]*len(nums) # dp 리스트 초기화
        dp[0] = nums[0] # 첫 번째 집을 털 경우
        dp[1] = max(nums[0], nums[1]) # 첫 번째와 두 번째 집 중에서 더 많은 돈을 가진 집을 털 경우

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]) # 이전 집을 털었을 경우와 이전 이전 집을 털고 현재 집을 털 경우 중 큰 값을 선택

        return dp[-1]
        
# input = [2,7,9,3,1]
            
# i= 2     7, 2+ 9 
# i=3      11, 73
# i=4      11, 11,1

# dp[2, 7, 11, 11, 12]

# dp[i-1] = 이전 집을 털었을 때 얻을 수 있는 돈의 최대합
# dp[i-2] + nums[i] 현재 집과 이전 집을 털었을 때 최대합

# dp[i-1]는 도둑이 이전 집을 털고 현재 집을 털지 않는 선택을, 
# dp[i-2] + nums[i]는 도둑이 이전 집을 털지 않고 이전의 이전 집과 현재 집을 털어 더 많은 돈을 얻는 선택