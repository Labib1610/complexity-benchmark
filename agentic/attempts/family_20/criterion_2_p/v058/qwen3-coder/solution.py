import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n_L = int(data[idx])
    idx += 1
    n_R = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    sessions = []
    degree_L = [0] * (n_L + 1)
    degree_R = [0] * (n_R + 1)
    
    for i in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        sessions.append((u, v))
        degree_L[u] += 1
        degree_R[v] += 1
    
    peak_load = max(max(degree_L[1:]), max(degree_R[1:]))
    
    # Build adjacency list for the graph (sessions as nodes)
    adj = [[] for _ in range(m)]
    session_index = {}
    
    # Create a mapping from (u,v) to index
    for i in range(m):
        u, v = sessions[i]
        session_index[(u, v)] = i
    
    # For each presenter and reviewer, connect their sessions
    presenter_sessions = [[] for _ in range(n_L + 1)]
    reviewer_sessions = [[] for _ in range(n_R + 1)]
    
    for i in range(m):
        u, v = sessions[i]
        presenter_sessions[u].append(i)
        reviewer_sessions[v].append(i)
    
    # Connect sessions that share a presenter
    for u in range(1, n_L + 1):
        s_list = presenter_sessions[u]
        for i in range(len(s_list)):
            for j in range(i+1, len(s_list)):
                adj[s_list[i]].append(s_list[j])
                adj[s_list[j]].append(s_list[i])
    
    # Connect sessions that share a reviewer
    for v in range(1, n_R + 1):
        s_list = reviewer_sessions[v]
        for i in range(len(s_list)):
            for j in range(i+1, len(s_list)):
                adj[s_list[i]].append(s_list[j])
                adj[s_list[j]].append(s_list[i])
    
    # Graph coloring with at most peak_load colors
    color = [0] * m
    for i in range(m):
        if color[i] == 0:
            # Available colors (1 to peak_load)
            used = [False] * (peak_load + 1)
            for neighbor in adj[i]:
                if color[neighbor] != 0:
                    used[color[neighbor]] = True
            for c in range(1, peak_load + 1):
                if not used[c]:
                    color[i] = c
                    break
    
    print("YES")
    print(' '.join(map(str, color)))

if __name__ == "__main__":
    main()