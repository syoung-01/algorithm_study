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