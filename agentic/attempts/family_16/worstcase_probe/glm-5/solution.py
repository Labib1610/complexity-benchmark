import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    j = int(next(iterator))
    m = int(next(iterator))
    T = int(next(iterator))
    
    jobs = []
    for _ in range(j):
        o = int(next(iterator))
        ops = []
        for _ in range(o):
            machine = int(next(iterator)) - 1
            duration = int(next(iterator))
            ops.append((machine, duration))
        jobs.append(ops)
        
    # 1. Check if total duration of any job exceeds T
    for ops in jobs:
        if sum(d for _, d in ops) > T:
            print("NO")
            return
            
    # 2. Build the graph for longest path (critical path method)
    # Nodes:
    # 0: Super Source
    # 1 to j: Job Source nodes
    # j+1 to j+m: Machine Source nodes
    # j+m+1 to j+m+j: Job Sink nodes
    # j+m+j+1: Super Sink
    
    N = j + m + j + 2
    S = 0
    t = N - 1
    
    adj = [[] for _ in range(N)]
    
    def add_edge(u, v, w):
        adj[u].append((v, w))
        
    # Super Source to Job Sources (weight 0)
    for i in range(1, j + 1):
        add_edge(S, i, 0)
        
    # Job Sources to Machine Sources (weight duration)
    for i in range(j):
        for k, (machine, duration) in enumerate(jobs[i]):
            u = i + 1
            v = j + 1 + machine
            add_edge(u, v, duration)
            
    # Machine Sources to Job Sources (weight duration)
    for i in range(j):
        for k, (machine, duration) in enumerate(jobs[i]):
            u = j + 1 + machine
            v = i + 1
            add_edge(u, v, duration)
            
    # Job Sources to Job Sinks (weight 0)
    for i in range(1, j + 1):
        add_edge(i, j + m + i, 0)
        
    # Job Sinks to Super Sink (weight -T)
    for i in range(1, j + 1):
        add_edge(j + m + i, t, -T)
        
    # 3. Bellman-Ford to find longest path
    dist = [-10**18] * N
    dist[S] = 0
    
    for _ in range(N - 1):
        updated = False
        for u in range(N):
            if dist[u] > -10**17:
                for v, w in adj[u]:
                    if dist[u] + w > dist[v]:
                        dist[v] = dist[u] + w
                        updated = True
        if not updated:
            break
        
    # 4. Check for positive cycles
    for u in range(N):
        if dist[u] > -10**17:
            for v, w in adj[u]:
                if dist[u] + w > dist[v]:
                    print("NO")
                    return
                    
    # 5. Extract start times
    res = []
    for i in range(j):
        job_res = []
        for machine, duration in jobs[i]:
            # start time = dist[Machine Source] - dist[Job Source]
            start = dist[j + 1 + machine] - dist[i + 1]
            job_res.append(start)
        res.append(job_res)
        
    print("YES")
    for job_res in res:
        print(" ".join(map(str, job_res)))

if __name__ == '__main__':
    solve()