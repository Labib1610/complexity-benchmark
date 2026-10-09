import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    N_alpha = int(data[idx])
    idx += 1
    N_omega = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    if m == 0:
        print("YES")
        return

    jobs = []
    alpha_graph = defaultdict(list)
    omega_graph = defaultdict(list)
    
    for i in range(m):
        u = int(data[idx]) - 1
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        jobs.append((u, v))
        alpha_graph[u].append(i)
        omega_graph[v].append(i)
    
    # Build conflict graph: edges between jobs that share alpha or omega resource
    adj = [set() for _ in range(m)]
    for u_list in alpha_graph.values():
        for i in range(len(u_list)):
            for j in range(i+1, len(u_list)):
                adj[u_list[i]].add(u_list[j])
                adj[u_list[j]].add(u_list[i])
                
    for v_list in omega_graph.values():
        for i in range(len(v_list)):
            for j in range(i+1, len(v_list)):
                adj[v_list[i]].add(v_list[j])
                adj[v_list[j]].add(v_list[i])

    # Greedy coloring with numbering from 1 to K
    color = [0] * m
    K = 0
    
    for i in range(m):
        forbidden = [False] * (m + 1)
        for neighbor in adj[i]:
            if color[neighbor] != 0:
                forbidden[color[neighbor]] = True
        c = 1
        while forbidden[c]:
            c += 1
        color[i] = c
        if c > K:
            K = c
            
    print("YES")
    print(' '.join(map(str, color)))

if __name__ == "__main__":
    main()