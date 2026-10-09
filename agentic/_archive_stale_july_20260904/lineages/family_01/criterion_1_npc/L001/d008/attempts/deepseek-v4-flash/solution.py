import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    bands = [0] * n
    
    for i in range(n):
        used = set()
        for nb in adj[i]:
            if bands[nb] != 0:
                used.add(bands[nb])
        for b in (1, 2, 3):
            if b not in used:
                bands[i] = b
                break
        else:
            print("NO")
            return
    
    print("YES")
    print(" ".join(map(str, bands)))

if __name__ == "__main__":
    solve()