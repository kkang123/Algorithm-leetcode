class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 메모이제이션
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(nums[i] + (sums[i-1] if sums[i-1] > 0 else 0))

        return max(sums)






        
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # max_sum =dp[0]

        # for i in range(1, len(nums)):
        #     dp[i] = max(nums[i], dp[i-1] + nums[i])
        #     max_sum = max(max_sum, dp[i])
        
        # return max_sum




# 다이나믹 프로그래밍
# 반복된 부분 찾기
# nums 배열이 [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# dp 배열 생성
# dp[0]에 nums[0] 초기화 -> dp = [-2, 0, 0, 0, 0, 0, 0, 0, 0]
# for문을 사용하여 두 번째 인덱스부터 반복
# dp[1] = max(nums[1](1), -2 + 1) ->nums[1]과 계산한 것 중 큰 값을 dp에 할당 dp[1] = 1
# dp[2] = max(nums[2](-3), -1 + -3] dp[2] = -2
# dp[3] = max(num[3](4), -2 + 4) = 4

# dp = [-2, 1, -2, 4, 3, 5, 6, 1, 5]

# 1, 1, 4, 4, 5, 6, 6, 6 - > 6