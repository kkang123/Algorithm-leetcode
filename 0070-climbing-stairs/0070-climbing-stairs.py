class Solution:
    dp = {1 : 1, 2 : 2}

    def climbStairs(self, n: int) -> int:
            if n in self.dp:
                return self.dp[n]
            
            self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.dp[n]
        
        
# 코드 최적화 / 해시테이블 대신 두 개의 변수값만 있으면 계산 가능

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n<3 :
#             return n
#         pre, cur = 1, 2
#         for _ in range(n-2):
#             pre, cur = cur, pre + cur
#         return cur