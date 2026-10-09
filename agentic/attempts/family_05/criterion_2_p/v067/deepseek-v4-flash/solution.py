import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    k = int(input_data[0])
    t = int(input_data[1])
    
    # Map from drone ID -> list of frequencies available for that drone
    freqs_for_drone = [[] for _ in range(k + 1)]
    
    idx = 2
    for _ in range(t):
        d = int(input_data[idx])
        c = int(input_data[idx + 1])
        f = int(input_data[idx + 2])
        idx += 3
        freqs_for_drone[d].append(f)
    
    # If a drone has no frequencies => impossible
    for d in range(1, k + 1):
        if not freqs_for_drone[d]:
            print("NO")
            return
    
    # bipartite matching: drones -> frequencies
    # Left: drones, Right: frequencies (1..k)
    # DFS-based augmenting path
    
    match_freq = [-1] * (k + 1)  # which drone is matched to frequency j
    
    def dfs(drone, seen):
        for f in freqs_for_drone[drone]:
            if not seen[f]:
                seen[f] = True
                if match_freq[f] == -1 or dfs(match_freq[f], seen):
                    match_freq[f] = drone
                    return True
        return False
    
    for d in range(1, k + 1):
        seen = [False] * (k + 1)
        if not dfs(d, seen):
            print("NO")
            return
    
    # Build output
    print("YES")
    # We need drone, station, frequency. Station for a drone is fixed.
    # We need to know station for each drone. It's given in input.
    station_for_drone = [0] * (k + 1)
    idx = 2
    for _ in range(t):
        d = int(input_data[idx])
        c = int(input_data[idx + 1])
        f = int(input_data[idx + 2])
        idx += 3
        station_for_drone[d] = c
    
    for f in range(1, k + 1):
        d = match_freq[f]
        print(f"{d} {station_for_drone[d]} {f}")

if __name__ == "__main__":
    main()