import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    k = int(input_data[0])
    t = int(input_data[1])
    modules = []
    idx = 2
    for _ in range(t):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        z = int(input_data[idx+2])
        modules.append((x, y, z))
        idx += 3

    if k == 0:
        print("YES")
        return

    if t < k:
        print("NO")
        return

    if k == 1:
        print("YES")
        print(f"{modules[0][0]} {modules[0][1]} {modules[0][2]}")
        return

    freq_to_mods = {}
    for m in modules:
        freq_to_mods.setdefault(m[0], []).append(m)

    freqs = sorted(freq_to_mods.keys(), key=lambda f: len(freq_to_mods[f]))

    chosen = []
    used_amps = set()
    used_phases = set()

    def dfs(i):
        if i == k:
            return True
        f = freqs[i]
        for m in freq_to_mods[f]:
            amp = m[1]
            phase = m[2]
            if amp not in used_amps and phase not in used_phases:
                chosen.append(m)
                used_amps.add(amp)
                used_phases.add(phase)
                if dfs(i + 1):
                    return True
                chosen.pop()
                used_amps.remove(amp)
                used_phases.remove(phase)
        return False

    if dfs(0):
        print("YES")
        for m in chosen:
            print(f"{m[0]} {m[1]} {m[2]}")
    else:
        print("NO")

solve()