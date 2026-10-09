import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    k = int(input_data[0])
    t = int(input_data[1])
    profiles = [[] for _ in range(k)]
    idx = 2
    for _ in range(t):
        x = int(input_data[idx]) - 1
        y = int(input_data[idx+1]) - 1
        z = int(input_data[idx+2]) - 1
        idx += 3
        profiles[x].append((y, z))
    
    # If any frequency has no profiles, impossible
    for i in range(k):
        if not profiles[i]:
            print("NO")
            return
    
    # Sort profiles by (voltage, phase) to have deterministic order
    for i in range(k):
        profiles[i].sort()
    
    chosen = [None] * k
    used_voltage = 0
    used_phase = 0
    
    # Backtracking
    def dfs(freq):
        nonlocal used_voltage, used_phase
        if freq == k:
            return True
        for v, p in profiles[freq]:
            if not (used_voltage >> v) & 1 and not (used_phase >> p) & 1:
                chosen[freq] = (freq+1, v+1, p+1)
                used_voltage |= (1 << v)
                used_phase |= (1 << p)
                if dfs(freq+1):
                    return True
                used_voltage ^= (1 << v)
                used_phase ^= (1 << p)
        return False
    
    if dfs(0):
        print("YES")
        for x, y, z in chosen:
            print(f"{x} {y} {z}")
    else:
        print("NO")

if __name__ == "__main__":
    solve()