def solve():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        c, p = map(int, input().split())
        edges.append((c, p))
    
    adj = [[] for _ in range(n + 1)]
    for c, p in edges:
        adj[p].append(c)
    
    def get_covered(sensor_locations):
        covered = set()
        for loc in sensor_locations:
            covered.add(loc)
            if loc > 1:
                covered.add(next((p for c, p in edges if c == loc), 0))
            for child in adj[loc]:
                covered.add(child)
        return covered
    
    min_sensors = float('inf')
    
    for i in range(1 << n):
        sensor_locations = []
        for j in range(n):
            if (i >> j) & 1:
                sensor_locations.append(j + 1)
        
        covered = get_covered(sensor_locations)
        
        if len(covered) == n:
            min_sensors = min(min_sensors, len(sensor_locations))
            
    print(min_sensors)

solve()