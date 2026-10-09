import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    p1 = [0] * j
    p2 = [0] * j
    idx = 2
    for i in range(j):
        p1[i] = int(data[idx])
        p2[i] = int(data[idx + 1])
        idx += 2

    # JOB check: precedence alone for each subsystem
    for i in range(j):
        if p1[i] + p2[i] > T:
            print(f"JOB {i + 1}")
            return

    # LOAD 1 check: capacitor grid serial + precedence, init grid ignored (p2=0, infinite capacity)
    if sum(p1) > T:
        print("LOAD 1")
        return

    # LOAD 2 check: init grid serial + precedence, capacitor grid ignored (p1=0, infinite capacity)
    if sum(p2) > T:
        print("LOAD 2")
        return

    # Fallback (should not happen given problem guarantees)
    print("LOAD 1")

if __name__ == "__main__":
    solve()