# README



 단순 반복문이 슬라이싱까지 있음에도 불구하고 재귀보다는 20퍼센트 정도 빠릅니다. (600-700ms / 800-900ms) 역시 재귀가 자장 느리긴 한 것 같습니다. 저랑 현승님의 접근도 방법 자체는 맞았던 것 같습니다. 근데 어디서 틀렸던 걸까요... 밀어내기 ...?



## 1. DFS 재귀

```python
import sys
input = sys.stdin.readline

def dfs(cnt):
    global ans
    if cnt == 9:
        start, score = 0, 0
        for inning in a:
            out, b1, b2, b3 = 0, 0, 0, 0
            # 밀어내기
            while out <= 2:
                p = select[start]
                if inning[p] == 0:
                    out += 1
                elif inning[p] == 1:
                    score += b3
                    b1, b2, b3 = 1, b1, b2
                elif inning[p] == 2:
                    score += b2 + b3
                    b1, b2, b3 = 0, 1, b1
                elif inning[p] == 3:
                    score += b1 + b2 + b3
                    b1, b2, b3 = 0, 0, 1
                else:
                    score += b1 + b2 + b3 + 1
                    b1, b2, b3 = 0, 0, 0

                start += 1
                # 이닝이 끝날 때까지 계속 봐야하니까
                start %= 9
        # 3 out일 때
        ans = max(ans, score)
        return

    for i in range(9):
        if c[i]:
            continue
        c[i] = 1
        # 순서대로 select하기 위한 것(permutation처럼 하기)
        select[i] = cnt
        dfs(cnt + 1)
        c[i] = 0
        select[i] = 0


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
select, c = [0 for _ in range(9)], [0 for _ in range(9)]
# 방문 체크
select[3], c[3] = 0, 1
ans = 0
dfs(1)
print(ans)
```



## 2. Permutation 반복문

```python
import sys
from itertools import permutations

input = sys.stdin.readline

num = int(input())
rounds = []
for _ in range(num):
    rounds.append(list(map(int, input().split())))

max = 0
# permutation 만들기 (4번타자가 정해져 있어서 8명만)
for p in permutations(range(1, 9)):
    p = list(p)
    global order
    # 4번 타자 넣어주기
    order = p[:3] + [0] + p[3:]
    score = 0
    hitter = 0
    for round in rounds:
        first, second, third = 0, 0, 0
        out = 0
        while out < 3:
            step = round[order[hitter]]
            # 밀어내는 방법
            if step == 0:
                out += 1
            elif step == 1:
                score += first
                first, second, third = second, third, 1
            elif step == 2:
                score += first + second
                first, second, third = third, 1, 0
            elif step == 3:
                score += first + second + third
                first, second, third = 1, 0, 0
            else:
                score += first + second + third + 1
                first, second, third = 0, 0, 0
            # inning 계속 돌리기 위한 방법
            hitter = (hitter + 1) % 9
    if score > max:
        max = score
print(max)
```

