j, T = map(int, input().split())
total1 = total2 = 0
for i in range(1, j + 1):
    p1, p2 = map(int, input().split())
    if p1 + p2 > T:
        print(f"JOB {i}")
        exit()
    total1 += p1
    total2 += p2

if total1 > T:
    print("LOAD 1")
elif total2 > T:
    print("LOAD 2")