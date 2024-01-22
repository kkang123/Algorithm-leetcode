class Solution:
    dp = {1 : 1, 2 : 2}

    def climbStairs(self, n: int) -> int:
            if n in self.dp:
                return self.dp[n]
            
            self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.dp[n]