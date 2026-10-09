import sys
from collections import defaultdict, deque
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n_L, n_R, m = map(int, sys.stdin.readline().split())
    
    jobs = []
    proc_jobs = defaultdict(list)
    mem_jobs = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        jobs.append((u, v))
        proc_jobs[u].append(i)
        mem_jobs[v].append(i)
    
    delta = 0
    for lst in proc_jobs.values():
        delta = max(delta, len(lst))
    for lst in mem_jobs.values():
        delta = max(delta, len(lst))
    
    if m == 0:
        print("YES")
        return
    
    # Build a graph where each job is a node
    # Two jobs are connected if they share a resource
    adj = [set() for _ in range(m)]
    
    for lst in proc_jobs.values():
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                u, v = lst[i], lst[j]
                adj[u].add(v)
                adj[v].add(u)
    
    for lst in mem_jobs.values():
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                u, v = lst[i], lst[j]
                adj[u].add(v)
                adj[v].add(u)
    
    # Now we need to color this graph with delta colors
    # Since the graph is the union of two graphs that are both delta-colorable,
    # and they are both complete graphs on their respective neighborhoods,
    # the chromatic number is at most delta.
    # We can use a greedy algorithm.
    
    color = [0] * m
    
    for i in range(m):
        forbidden = [False] * (delta + 1)
        for neighbor in adj[i]:
            if color[neighbor] != 0 and color[neighbor] <= delta:
                forbidden[color[neighbor]] = True
        for c in range(1, delta + 1):
            if not forbidden[c]:
                color[i] = c
                break
    
    print("YES")
    print(' '.join(map(str, color)))

threading.Thread(target=main).start()