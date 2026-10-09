n, T = map(int, input().split())
total_time = 0
for i in range(1, n + 1):
    p1, p2 = map(int, input().split())
    total_time += p1 + p2
    if total_time > T:
        print(f"LOAD {i}")
        break
else:
    print("JOB 1")