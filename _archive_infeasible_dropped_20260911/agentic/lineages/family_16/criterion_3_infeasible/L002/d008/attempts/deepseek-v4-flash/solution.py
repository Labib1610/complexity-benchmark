import sys

def solve():
    input = sys.stdin.readline
    j, T = map(int, input().split())
    p1 = []
    p2 = []
    for i in range(j):
        a, b = map(int, input().split())
        p1.append(a)
        p2.append(b)
    
    # Check JOB
    for i in range(j):
        if p1[i] + p2[i] > T:
            print(f"JOB {i+1}")
            return
    
    # Check LOAD 1
    # Sort by p1 descending
    order = sorted(range(j), key=lambda x: -p1[x])
    pos = -10**30
    ok = True
    for idx in order:
        low = p1[idx]
        high = 2*T - p1[idx]
        # Need to place at position >= pos + p1[idx] + p1[prev]? Actually we need distance >= p1_i + p1_k
        # Greedy: place at max(low, pos + p1[idx] + p1[prev]) but we don't have prev here.
        # Better: sort by p1 descending, place first at its low bound, then each next at max(low, last_pos + p1[last] + p1[current])
        # But we need to track last placed p1 value.
        if pos == -10**30:
            pos = low
            last_p1 = p1[idx]
        else:
            need = pos + last_p1 + p1[idx]
            if need > high:
                ok = False
                break
            pos = need
            last_p1 = p1[idx]
    if not ok:
        print("LOAD 1")
        return
    
    # Check LOAD 2
    order = sorted(range(j), key=lambda x: -p2[x])
    pos = -10**30
    ok = True
    for idx in order:
        low = p2[idx]
        high = 2*T - p2[idx]
        if pos == -10**30:
            pos = low
            last_p2 = p2[idx]
        else:
            need = pos + last_p2 + p2[idx]
            if need > high:
                ok = False
                break
            pos = need
            last_p2 = p2[idx]
    if not ok:
        print("LOAD 2")
        return

if __name__ == "__main__":
    solve()