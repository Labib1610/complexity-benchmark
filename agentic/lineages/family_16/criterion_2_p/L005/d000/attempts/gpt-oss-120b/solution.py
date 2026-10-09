import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    front = []   # a <= b
    back = []    # a >  b
    for _ in range(n):
        a = int(next(it))
        b = int(next(it))
        if a <= b:
            front.append((a, b))
        else:
            back.append((a, b))

    front.sort(key=lambda x: x[0])          # increasing a
    back.sort(key=lambda x: x[1], reverse=True)   # decreasing b

    draft = 0
    render = 0
    for a, b in front:
        draft += a
        render = max(render, draft) + b
    for a, b in back:
        draft += a
        render = max(render, draft) + b

    sys.stdout.write(str(render))

if __name__ == "__main__":
    solve()