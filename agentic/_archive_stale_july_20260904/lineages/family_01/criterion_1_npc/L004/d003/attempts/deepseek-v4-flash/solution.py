import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    edges = []
    idx = 2
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    # We'll use backtracking
    freq = [0] * n
    
    def backtrack(pos):
        if pos == n:
            return True
        for f in (1, 2, 3):
            # Check constraints with already assigned neighbors
            ok = True
            for nb in adj[pos]:
                if nb < pos and freq[nb] == f:
                    ok = False
                    break
            if ok:
                freq[pos] = f
                if backtrack(pos + 1):
                    return True
                freq[pos] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, freq)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()