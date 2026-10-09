j, T = map(int, input().split())
sum_p1 = 0
sum_p2 = 0

for i in range(1, j + 1):
    p1, p2 = map(int, input().split())
    if p1 + p2 > T:
        print(f"JOB {i}")
        break
    sum_p1 += p1
    sum_p2 += p2
else:
    if sum_p1 > T:
        print("LOAD 1")
    elif sum_p2 > T:
        print("LOAD 2")