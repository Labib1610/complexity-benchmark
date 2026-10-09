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
B.sort(key=lambda x: -x[1])

order = A + B

time_m1 = 0
time_m2 = 0
for p1, p2 in order:
    time_m1 += p1
    if time_m2 < time_m1:
        time_m2 = time_m1
    time_m2 += p2

print(time_m2)