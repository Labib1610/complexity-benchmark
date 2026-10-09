import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N_T = int(data[0])
    N_R = int(data[1])
    M = int(data[2])
    
    if M == 0:
        print("YES")
        return

    edges = []
    deg_T = [0] * (N_T + 1)
    deg_R = [0] * (N_R + 1)
    
    idx = 3
    for _ in range(M):
        u = int(data[idx])
        v = int(data[idx+1])
        edges.append((u, v))
        deg_T[u] += 1
        deg_R[v] += 1
        idx += 2
    
    K = max(max(deg_T), max(deg_R))
    
    # Create adjacency list for transmitters and receivers
    adj_T = [[] for _ in range(N_T + 1)]
    adj_R = [[] for _ in range(N_R + 1)]
    
    for i, (u, v) in enumerate(edges):
        adj_T[u].append((v, i))
        adj_R[v].append((u, i))
    
    # Assign time windows using a greedy approach with BFS-like coloring
    result = [0] * M
    used_T = [set() for _ in range(N_T + 1)]
    used_R = [set() for _ in range(N_R + 1)]
    
    # For each connection, assign the smallest available time window
    for i, (u, v) in enumerate(edges):
        win = 1
        while win in used_T[u] or win in used_R[v]:
            win += 1
        result[i] = win
        used_T[u].add(win)
        used_R[v].add(win)
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()