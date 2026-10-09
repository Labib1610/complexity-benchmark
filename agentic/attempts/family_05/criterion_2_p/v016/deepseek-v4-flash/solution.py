import sys
sys.setrecursionlimit(1000000)

def main():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    
    # For each transmitter, store possible frequencies
    freq_for_transmitter = [[] for _ in range(k + 1)]
    # Also store the module for each transmitter (should be unique per transmitter)
    module_for_transmitter = [0] * (k + 1)
    
    for _ in range(t):
        u, v, w = map(int, input().split())
        freq_for_transmitter[u].append(w)
        module_for_transmitter[u] = v  # overwrite, but should be same for same u
    
    # Bipartite matching: transmitters (1..k) to frequencies (1..k)
    match_freq = [0] * (k + 1)  # which transmitter is assigned to frequency f
    visited = [False] * (k + 1)
    
    def dfs(u):
        for w in freq_for_transmitter[u]:
            if not visited[w]:
                visited[w] = True
                if match_freq[w] == 0 or dfs(match_freq[w]):
                    match_freq[w] = u
                    return True
        return False
    
    match_count = 0
    for u in range(1, k + 1):
        visited = [False] * (k + 1)
        if dfs(u):
            match_count += 1
    
    if match_count != k:
        print("NO")
        return
    
    print("YES")
    for w in range(1, k + 1):
        u = match_freq[w]
        v = module_for_transmitter[u]
        print(u, v, w)

if __name__ == "__main__":
    main()