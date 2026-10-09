import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    s = int(input_data[2])
    t = int(input_data[3])
    B = int(input_data[4])
    
    adj = [[] for _ in range(n + 1)]
    idx = 5
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        idx += 3
        adj[u].append((v, w, i))
        adj[v].append((u, w, i))
        
    import heapq
    
    dist_s = [float('inf')] * (n + 1)
    dist_s[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist_s[u]:
            continue
        for v, w, _ in adj[u]:
            if dist_s[v] > d + w:
                dist_s[v] = d + w
                heapq.heappush(pq, (dist_s[v], v))
                
    dist_t = [float('inf')] * (n + 1)
    dist_t[t] = 0
    pq = [(0, t)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist_t[u]:
            continue
        for v, w, _ in adj[u]:
            if dist_t[v] > d + w:
                dist_t[v] = d + w
                heapq.heappush(pq, (dist_t[v], v))
                
    min_cut = dist_s[t]
    
    if min_cut > B:
        print("NO")
        return
        
    print("YES")
    
    cut_edges = []
    idx = 5
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        idx += 3
        if dist_s[u] + w + dist_t[v] == min_cut or dist_s[v] + w + dist_t[u] == min_cut:
            cut_edges.append((u, v))
            
    print(len(cut_edges))
    for u, v in cut_edges:
        print(u, v)

if __name__ == '__main__':
    solve()