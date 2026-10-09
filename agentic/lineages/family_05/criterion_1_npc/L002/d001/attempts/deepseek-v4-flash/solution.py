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
    
    # Group edges by input port
    by_input = [[] for _ in range(k)]
    for idx, (u, v, w) in enumerate(edges):
        by_input[u].append((v, w, idx))
    
    used_output = [False] * k
    used_freq = [False] * k
    chosen = []
    
    # Precompute for each input, the list of (output, freq) pairs
    # We'll do DFS over input ports
    def dfs(in_port):
        if in_port == k:
            return True
        for v, w, idx in by_input[in_port]:
            if not used_output[v] and not used_freq[w]:
                used_output[v] = True
                used_freq[w] = True
                chosen.append((in_port + 1, v + 1, w + 1))
                if dfs(in_port + 1):
                    return True
                chosen.pop()
                used_output[v] = False
                used_freq[w] = False
        return False
    
    if dfs(0):
        print("YES")
        for u, v, w in chosen:
            print(u, v, w)
    else:
        print("NO")

if __name__ == "__main__":
    solve()