j, T = map(int, input().split())
total1 = 0
total2 = 0
jobs = []
for i in range(j):
    p1, p2 = map(int, input().split())
    jobs.append((p1, p2))
    total1 += p1
    total2 += p2

# Check sequential bottleneck
for idx, (p1, p2) in enumerate(jobs, start=1):
    if p1 + p2 > T:
        print(f"JOB {idx}")
        exit()

# Check machine capacity
if total1 > T:
    print("LOAD 1")
    exit()
if total2 > T:
    print("LOAD 2")
    exit()