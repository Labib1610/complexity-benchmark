n, T = map(int, input().split())
total = 0
for i in range(1, n + 1):
    a, b = map(int, input().split())
    if a > T:
        print(f"JOB {i}")
        exit()
    total += a

if total > T:
    print("LOAD 1")
else:
    print("LOAD 2")