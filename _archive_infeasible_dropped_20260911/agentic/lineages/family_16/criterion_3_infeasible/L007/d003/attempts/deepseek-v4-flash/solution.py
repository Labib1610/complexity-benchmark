n, T = map(int, input().split())
p1_sum = 0
p2_sum = 0

for i in range(1, n + 1):
    p1, p2 = map(int, input().split())
    p1_sum += p1
    p2_sum += p2
    if p1 + p2 > T:
        print(f"JOB {i}")
        exit()

if p1_sum > T:
    print("LOAD 1")
    exit()

if p2_sum > T:
    print("LOAD 2")
    exit()