n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]

A = []
B = []
for p1, p2 in jobs:
    if p1 <= p2:
        A.append((p1, p2))
    else:
        B.append((p1, p2))

A.sort(key=lambda x: x[0])
B.sort(key=lambda x: x[1], reverse=True)

order = A + B

time1 = 0
time2 = 0
for p1, p2 in order:
    time1 += p1
    if time2 < time1:
        time2 = time1
    time2 += p2

print(time2)