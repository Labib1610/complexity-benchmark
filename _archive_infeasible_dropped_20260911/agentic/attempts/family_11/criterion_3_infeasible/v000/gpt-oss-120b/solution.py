import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    u, s = data[0], data[1]
    present = bytearray(u + 1)          # index 0 unused
    idx = 2
    for _ in range(s):
        c = data[idx]
        idx += 1
        for _ in range(c):
            skill = data[idx]
            idx += 1
            present[skill] = 1
    for skill_id in range(1, u + 1):
        if not present[skill_id]:
            sys.stdout.write(str(skill_id))
            return

if __name__ == "__main__":
    solve()