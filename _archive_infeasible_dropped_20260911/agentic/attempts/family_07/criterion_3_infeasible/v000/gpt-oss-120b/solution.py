import sys

def solve() -> None:
    data = sys.stdin.read().splitlines()
    if not data:
        return
    k = int(data[0])
    fragments = data[1:1 + k]
    F = data[1 + k] if 1 + k < len(data) else ''
    for idx, frag in enumerate(fragments, 1):
        if F in frag:
            print(idx)
            return

if __name__ == "__main__":
    solve()