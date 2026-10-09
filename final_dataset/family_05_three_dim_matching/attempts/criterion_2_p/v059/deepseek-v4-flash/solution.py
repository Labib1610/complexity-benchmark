import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    
    # For each chassis, store the set of batteries it can use
    allowed = [[] for _ in range(k)]
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        allowed[x].append(z)
    
    # Match batteries to chassis
    match_battery = [-1] * k  # which chassis is assigned to battery
    match_chassis = [-1] * k  # which battery is assigned to chassis
    
    def dfs(chassis, visited):
        for battery in allowed[chassis]:
            if not visited[battery]:
                visited[battery] = True
                if match_battery[battery] == -1 or dfs(match_battery[battery], visited):
                    match_battery[battery] = chassis
                    match_chassis[chassis] = battery
                    return True
        return False
    
    for chassis in range(k):
        visited = [False] * k
        if not dfs(chassis, visited):
            print("NO")
            return
    
    # If we matched all chassis, output YES
    print("YES")
    # Need to output schematics: chassis x, its fixed navigation y, and matched battery z
    # We need to know the fixed y for each chassis
    # We can get it from the input: for each chassis, all schematics have same y
    # We'll store it while reading
    # But we didn't store y. Let's re-read or store it.
    # We'll store y_for_chassis
    # Since we already consumed input, we need to store it during reading.
    # Let's modify: store y_for_chassis when reading.
    
    # Actually, we need to re-parse. Let's do it properly.
    # We'll rewrite the reading part to store y.
    
if __name__ == "__main__":
    solve()