​# 계단 오르기 : https://leetcode.com/problems/climbing-stairs/

```python
class Solution:
    dp = {1 : 1, 2 : 2}

    def climbStairs(self, n: int) -> int:
            if n in self.dp:
                return self.dp[n]
            
            self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.dp[n]
```

함수 내에서 클래스의 변수에 접근할 때 self 키워드를 사용하지 않으면 오류 발생 </br>
Python에서 클래스의 메소드 내부에서 클래스 변수에 접근하려면 self 키워드를 사용해야한다. </br>

</br>

이때, Soultion은 클래스 이름 </br>
climbStairs는 Solution 클래스에 속한 `메소드(함수)` = `클래스 메소드`는 해당 클래스의 인스턴스(객체)를 통해 호출 가능 </br></br>
dp는 Solution 클래스의 변수 = `클래스 변수` </br>
클래스 변수는 해당 클래스의 모든 인스턴스가 공유한다. 즉, 한 인스턴스에서 클래스 변수를 변경하면 다른 인스턴스에도 그 변경사항이 적용됨 </br></br>
`클래스 메소드`나 `클래스 변수`에 접근할 때 `self`라는 키워드를 사용해야함
