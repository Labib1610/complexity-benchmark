j, T = map(int, input().split())
p1 = []
p2 = []
for _ in range(j):
    a, b = map(int, input().split())
    p1.append(a)
    p2.append(b)

# Check JOB certificates
for i in range(j):
    if p1[i] + p2[i] > T + 1:
        print(f"JOB {i+1}")
        exit()

# Check LOAD certificates
if sum(p1) > T + 1:
    print("LOAD 1")
    exit()
if sum(p2) > T + 1:
    print("LOAD 2")
    exit()