import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    t = int(data[1])
    n = 3 * q
    triads = []
    idx = 2
    for _ in range(t):
        a = int(data[idx]); b = int(data[idx+1]); c = int(data[idx+2])
        idx += 3
        triads.append((a, b, c))
    
    adj = [[] for _ in range(n + 1)]
    for i, (a, b, c) in enumerate(triads):
        adj[a].append(i)
        adj[b].append(i)
        adj[c].append(i)
    
    used = [False] * (n + 1)
    triad_used = [False] * t
    chosen = []
    
    def dfs(cnt):
        if cnt == q:
            return True
        pivot = -1
        for v in range(1, n + 1):
            if not used[v]:
                pivot = v
                break
        if pivot == -1:
            return False
        for ti in adj[pivot]:
            if triad_used[ti]:
                continue
            a, b, c = triads[ti]
            if used[a] or used[b] or used[c]:
                continue
            used[a] = used[b] = used[c] = True
            triad_used[ti] = True
            chosen.append((a, b, c))
            if dfs(cnt + 1):
                return True
            chosen.pop()
            triad_used[ti] = False
            used[a] = used[b] = used[c] = False
        return False
    
    if dfs(0):
        out = ["YES"]
        for a, b, c in chosen:
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

solve()