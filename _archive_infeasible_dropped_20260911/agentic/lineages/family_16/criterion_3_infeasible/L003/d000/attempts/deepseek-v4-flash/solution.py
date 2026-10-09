j, T = map(int, input().split())
jobs = [tuple(map(int, input().split())) for _ in range(j)]

for i, (p1, p2) in enumerate(jobs, 1):
    if p1 + p2 > T:
        print(f"JOB {i}")
        break
else:
    total1 = sum(p1 for p1, _ in jobs)
    total2 = sum(p2 for _, p2 in jobs)
    if total1 > T:
        print("LOAD 1")
    else:
        print("LOAD 2")