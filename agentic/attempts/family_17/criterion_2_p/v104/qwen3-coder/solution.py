from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    if t < q:
        print("NO")
        return
    
    # Build graph for bipartite matching
    # Left side: collectors (1 to q)
    # Right side: processors (q+1 to 2*q)
    graph = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        graph[a].append(b)
        edges.append((a, b))
    
    # Try to find a perfect matching using BFS-based algorithm (Hopcroft-Karp like approach)
    # But we'll use a simpler approach with DFS for this implementation
    
    # For each collector, try to find an augmenting path
    match_processor = {}  # processor -> collector
    match_collector = {}  # collector -> processor
    
    def dfs(collector, visited):
        for processor in graph[collector]:
            if processor in visited:
                continue
            visited.add(processor)
            
            # If processor is unmatched or we can find augmenting path
            if processor not in match_processor or dfs(match_processor[processor], visited):
                match_processor[processor] = collector
                match_collector[collector] = processor
                return True
        return False
    
    # Try to match each collector
    matched = 0
    for collector in range(1, q + 1):
        if dfs(collector, set()):
            matched += 1
    
    if matched == q:
        print("YES")
        for collector in range(1, q + 1):
            print(collector, match_collector[collector])
    else:
        print("NO")

solve()