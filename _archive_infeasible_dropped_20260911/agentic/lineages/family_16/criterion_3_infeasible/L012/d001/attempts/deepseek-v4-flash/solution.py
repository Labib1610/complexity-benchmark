j, T = map(int, input().split())
p1s = []
p2s = []
for i in range(j):
    p1, p2 = map(int, input().split())
    p1s.append(p1)
    p2s.append(p2)
    if p1 + p2 > T:
        print(f"JOB {i+1}")
        exit()

if sum(p1s) > T:
    print("LOAD 1")
    exit()

if sum(p2s) > T:
    print("LOAD 2")
    exit()