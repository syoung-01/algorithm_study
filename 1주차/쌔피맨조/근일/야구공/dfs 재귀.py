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