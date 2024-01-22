# 동적 프로그래밍(Dynamic Programming, DP) 알고리즘 -> 메모이제이션 사용
투 포인터로 풀기는 어렵다.

이유는 왼쪽 포인터가 -2이고, 오른쪽 포인터가 4라고 하면 그 사잇값이 최대가 되기 위해서는 음수를 지나치는 방식으로 알고리즘을 구현해야하는데 연속된 서브 배열을 찾아내야하기 때문에 정렬을 할 수 없으며 다음 숫자가 뭐가 나올지 모르는 상태에서 음수를 건너 뛰는 방식으로 구현하면 어렵기 때문이다.

### 효율적인 투 포인터 풀이하기 위해서는 `정렬`이 필요하다!​

## 메모이제이션 사용
### O(n)
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 메모이제이션
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(nums[i] + (sums[i-1] if sums[i-1] > 0 else 0))

        return max(sums)


# 이때, sums에서 가장 큰 값인 6을 결과값으로 반환

# output = 6
```
앞에서 부터 계속 값을 계산하면서 누적 합을 계산 </br>
이전 값을 계속 더해나가되 0이하가 되면 버린다. </br>
어차피 최댓값을 찾을 때 0 이하가 되는 값은 굳이 서브 배열에 포함할 이유가 없기 때문 </br>
sums = [-2, 1, -2, 4, 3, 5, 6, 1, 5]

```python
sums.append(nums[i] + (sums[i-1] if sums[i-1] > 0 else 0))
# 누적된 합(sums[i - 1]이 0보다 큰지 확인하는 조건문
# sums[i-1] > 0 참이라면, 이전까지 누적된 합(sums[i-1])이 양수
# nums[i] + sums[i-1] -> sums에 추가

# sums[i-1] > 0 거짓이라면, 이전까지의 누적된 합(sums[i-1])은 0 이하
# 누적된 합을 현재요소(nums[i])에 더하는 것이 전체 합을 줄이기 때문에 -> (nums[i])만 sums에 추가
```

## 똑같은 동적 프로그래밍(Dynamic Programming, DP) 알고리즘
### O(n)
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_sum =dp[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            max_sum = max(max_sum, dp[i])
        
        return max_sum




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
```

## 최적화 된 코드
### O(n)
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_total = nums[0]
        total = nums[0]

        for i in range(1, len(nums)):
            total = max(nums[i], total +nums[i])
            max_total = max(total, max_total)
        return max_total
```
