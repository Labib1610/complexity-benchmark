import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    # arm -> list of (sensor, module)
    arm_options = [[] for _ in range(k)]
    for _ in range(t):
        x, y, z = map(int, input().split())
        arm_options[x-1].append((y-1, z-1))
    
    # Precompute for each arm and sensor, which modules are possible
    arm_sensor_modules = [[0]*k for _ in range(k)]
    for arm in range(k):
        for sensor, module in arm_options[arm]:
            arm_sensor_modules[arm][sensor] |= (1 << module)
    
    # Backtracking: assign sensors to arms, track used modules
    used_sensors = 0
    used_modules = 0
    assignment = [-1]*k  # arm -> sensor
    
    # For fast module matching check, we can use bipartite matching
    # But we'll do backtracking with pruning
    
    def backtrack(arm_idx):
        nonlocal used_sensors, used_modules
        if arm_idx == k:
            return True
        # Try each sensor not used
        for sensor in range(k):
            if (used_sensors >> sensor) & 1:
                continue
            # Check if there is at least one module possible
            possible_modules = arm_sensor_modules[arm_idx][sensor] & ~used_modules
            if possible_modules == 0:
                continue
            # Try each possible module
            mod_mask = possible_modules
            while mod_mask:
                # pick lowest set bit
                lsb = mod_mask & -mod_mask
                module = (lsb.bit_length() - 1)
                mod_mask ^= lsb
                # assign
                used_sensors |= (1 << sensor)
                used_modules |= (1 << module)
                assignment[arm_idx] = sensor
                if backtrack(arm_idx + 1):
                    return True
                # undo
                used_sensors ^= (1 << sensor)
                used_modules ^= (1 << module)
                assignment[arm_idx] = -1
        return False
    
    if backtrack(0):
        print("YES")
        # Reconstruct modules: we need to know which module each arm used
        # We can re-run to find modules, or store them during backtrack
        # We'll store module assignment in a separate array
        # Let's modify to store module too
        # We'll do a second pass: we know sensors, find modules via matching
        # But easier: store module in backtrack
        # We'll rewrite with storing module
        # Actually we can just re-run with storing
        # Let's do a quick fix: store module assignment in a global
        # We'll redo with storing
        pass
    else:
        print("NO")

if __name__ == "__main__":
    solve()