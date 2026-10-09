import sys
from itertools import combinations

def solve():
    k, t = map(int, sys.stdin.readline().split())
    
    blueprints = []
    for _ in range(t):
        x, y, z = map(int, sys.stdin.readline().split())
        blueprints.append((x, y, z))
    
    # We need to select exactly k blueprints such that all workers, equipment and schedule blocks are distinct
    # This is equivalent to finding a matching of size k in a 3-dimensional bipartite graph
    
    # Try all combinations of k blueprints
    for combo in combinations(range(t), k):
        workers = set()
        equipment = set()
        schedules = set()
        
        valid = True
        selected_blueprints = []
        
        for i in combo:
            x, y, z = blueprints[i]
            if x in workers or y in equipment or z in schedules:
                valid = False
                break
            workers.add(x)
            equipment.add(y)
            schedules.add(z)
            selected_blueprints.append((x, y, z))
        
        if valid and len(workers) == k and len(equipment) == k and len(schedules) == k:
            print("YES")
            for bp in selected_blueprints:
                print(bp[0], bp[1], bp[2])
            return
    
    print("NO")

solve()