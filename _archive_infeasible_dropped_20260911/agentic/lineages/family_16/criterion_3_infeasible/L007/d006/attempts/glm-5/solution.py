import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    idx = 2
    p1 = [0] * j
    p2 = [0] * j
    for i in range(j):
        p1[i] = int(data[idx])
        p2[i] = int(data[idx + 1])
        idx += 2

    job = -1
    for i in range(j):
        if p1[i] + p2[i] > T:
            job = i + 1
            break

    if job != -1:
        sys.stdout.write(f"JOB {job}\n")
        return

    load = -1
    for c, p in ((1, p1), (2, p2)):
        p_sorted = sorted(p)
        total = 0
        possible = True
        for v in p_sorted:
            total += v
            if total > T:
                possible = False
                break
        if not possible:
            load = c
            break

    sys.stdout.write(f"LOAD {load}\n")

solve()