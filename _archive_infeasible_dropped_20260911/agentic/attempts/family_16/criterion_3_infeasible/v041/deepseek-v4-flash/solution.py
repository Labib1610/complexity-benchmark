j, T = map(int, input().split())
total_p1 = 0
total_p2 = 0

for i in range(1, j + 1):
    p1, p2 = map(int, input().split())
    total_p1 += p1
    total_p2 += p2
    if p1 + p2 > T:
        print(f"JOB {i}")
        break
else:
    if total_p1 > T:
        print("LOAD 1")
    else:
        print("LOAD 2")