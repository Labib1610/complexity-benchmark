import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    # Store viable configs as a set of (x, y, z)
    configs = set()
    for _ in range(t):
        x, y, z = map(int, input().split())
        configs.add((x-1, y-1, z-1))  # 0-index

    # For each arm and sensor, store possible modules
    arm_sensor_module = [[set() for _ in range(k)] for _ in range(k)]
    for x, y, z in configs:
        arm_sensor_module[x][y].add(z)

    # We'll try to assign each arm to a sensor, and then check if modules can be matched
    # Use backtracking with bitmask for sensors and modules
    sensor_used = 0
    module_used = 0
    assignment = [-1] * k  # assignment[arm] = (sensor, module)

    # Precompute for each arm, list of (sensor, module) pairs
    arm_options = []
    for x in range(k):
        opts = []
        for y in range(k):
            for z in arm_sensor_module[x][y]:
                opts.append((y, z))
        arm_options.append(opts)

    # Sort arms by number of options (smallest first) for pruning
    order = sorted(range(k), key=lambda x: len(arm_options[x]))
    result = None

    def dfs(idx):
        nonlocal sensor_used, module_used, result
        if idx == k:
            result = [None] * k
            for arm in range(k):
                s, m = assignment[arm]
                result[arm] = (arm+1, s+1, m+1)
            return True
        arm = order[idx]
        for y, z in arm_options[arm]:
            if not (sensor_used >> y) & 1 and not (module_used >> z) & 1:
                sensor_used |= (1 << y)
                module_used |= (1 << z)
                assignment[arm] = (y, z)
                if dfs(idx+1):
                    return True
                sensor_used ^= (1 << y)
                module_used ^= (1 << z)
                assignment[arm] = (-1, -1)
        return False

    if dfs(0):
        print("YES")
        for x, y, z in result:
            print(x, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()