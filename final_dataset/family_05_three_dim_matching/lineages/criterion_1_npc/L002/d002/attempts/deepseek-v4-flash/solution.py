import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    
    edges = []
    for _ in range(t):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it)) - 1
        edges.append((u, v, w))
    
    # adjacency list per input port
    adj = [[] for _ in range(k)]
    for idx, (u, v, w) in enumerate(edges):
        adj[u].append((v, w, idx))
    
    used_out = [False] * k
    used_freq = [False] * k
    chosen = []
    
    # sort edges by degree heuristic maybe, but simple backtracking works for k<=22
    def dfs(u):
        if u == k:
            return True
        for v, w, idx in adj[u]:
            if not used_out[v] and not used_freq[w]:
                used_out[v] = True
                used_freq[w] = True
                chosen.append(edges[idx])
                if dfs(u + 1):
                    return True
                chosen.pop()
                used_out[v] = False
                used_freq[w] = False
        return False
    
    if dfs(0):
        print("YES")
        for u, v, w in chosen:
            print(u + 1, v + 1, w + 1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()