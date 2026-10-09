import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    viable = [[False] * (k + 1) for _ in range(k + 1)]
    # viable[surgeon][room] = bitmask of time slots
    for _ in range(t):
        x, y, z = map(int, input().split())
        viable[x][y] |= (1 << (z - 1))
    
    # We'll try to assign each time slot a surgeon and room
    # Use backtracking with bitmasks for used surgeons and rooms
    used_surgeons = 0
    used_rooms = 0
    assignment = [None] * (k + 1)  # assignment[time] = (surgeon, room)
    
    # Precompute list of (surgeon, room) for each time slot
    options = [[] for _ in range(k)]
    for z in range(1, k + 1):
        for x in range(1, k + 1):
            for y in range(1, k + 1):
                if viable[x][y] & (1 << (z - 1)):
                    options[z - 1].append((x, y))
    
    # Sort options by size for better pruning
    order = sorted(range(k), key=lambda z: len(options[z]))
    
    def dfs(idx):
        nonlocal used_surgeons, used_rooms
        if idx == k:
            return True
        z = order[idx]
        for x, y in options[z]:
            if not (used_surgeons & (1 << (x - 1))) and not (used_rooms & (1 << (y - 1))):
                used_surgeons |= (1 << (x - 1))
                used_rooms |= (1 << (y - 1))
                assignment[z] = (x, y)
                if dfs(idx + 1):
                    return True
                used_surgeons ^= (1 << (x - 1))
                used_rooms ^= (1 << (y - 1))
        return False
    
    if dfs(0):
        print("YES")
        for z in range(1, k + 1):
            x, y = assignment[z]
            print(x, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()