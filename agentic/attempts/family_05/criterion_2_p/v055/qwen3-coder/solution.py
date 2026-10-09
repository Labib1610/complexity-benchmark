from collections import defaultdict

def solve():
    import sys
    import threading
    
    def main():
        input = sys.stdin.read
        data = input().split()
        
        k = int(data[0])
        t = int(data[1])
        
        if t < k:
            print("NO")
            return
            
        # Since each source is permanently attached to one waveplate,
        # and no two sources share the same waveplate,
        # we can think of this as a bipartite matching problem:
        # match sources to sensors, where the waveplate is determined by the source.
        
        # For each source x, there's exactly one waveplate y_x
        # So we can represent each test as (source, sensor) since waveplate is fixed
        
        # Build adjacency list: for each source, which sensors it can connect to
        adj = defaultdict(list)
        source_to_waveplate = {}
        
        idx = 2
        for _ in range(t):
            x = int(data[idx])
            y = int(data[idx+1])
            z = int(data[idx+2])
            idx += 3
            
            adj[x].append(z)
            if x not in source_to_waveplate:
                source_to_waveplate[x] = y
                
        # Check if we have exactly k sources
        if len(source_to_waveplate) < k:
            print("NO")
            return
            
        # Now we need to find a perfect matching in a bipartite graph:
        # Left side: sources 1..k
        # Right side: sensors 1..k
        # Edges: (source, sensor) if there exists a test with that combination
        
        # Use Hopcroft-Karp or similar. But since k<=1200, let's use a simpler approach:
        # Build the graph and run a maximum bipartite matching algorithm
        
        # Let's build the graph properly
        # Nodes on left: sources [1..k]
        # Nodes on right: sensors [1..k]
        # Edge exists if (source, waveplate_source, sensor) was tested
        
        # We'll use a standard augmenting path algorithm for bipartite matching
        
        # graph[sensor] = list of sources that can use this sensor
        graph_rev = defaultdict(list)
        for x in range(1, k+1):
            if x in adj:
                for z in adj[x]:
                    graph_rev[z].append(x)
        
        # Matching from sensor to source
        match_sensor = {}
        match_source = {}
        
        def dfs(u, visited):
            # Try to find an augmenting path starting from source u
            for v in adj.get(u, []):
                if v in visited:
                    continue
                visited.add(v)
                # If v is unmatched, or we can find an augmenting path from its current match
                if v not in match_sensor or dfs(match_sensor[v], visited):
                    match_sensor[v] = u
                    match_source[u] = v
                    return True
            return False
        
        # Try to match each source
        matched = 0
        for u in range(1, k+1):
            if u in adj:  # Only consider sources that have at least one test
                visited = set()
                if dfs(u, visited):
                    matched += 1
        
        if matched < k:
            print("NO")
            return
            
        print("YES")
        for u in range(1, k+1):
            if u in match_source:
                z = match_source[u]
                y = source_to_waveplate[u]
                print(u, y, z)

    threading.Thread(target=main).start()

solve()