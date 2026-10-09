j, T = map(int, input().split())
d1 = []
d2 = []
for i in range(j):
    a, b = map(int, input().split())
    d1.append(a)
    d2.append(b)
    if a + b > T:
        print(f"JOB {i+1}")
        exit()

if sum(d1) > T:
    print("LOAD 1")
elif sum(d2) > T:
    print("LOAD 2")