import sys

def main():
    data = sys.stdin.buffer.read().split()
    j = int(data[0])
    assets = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        assets.append((p1, p2))
    
    first = []
    second = []
    for p1, p2 in assets:
        if p1 < p2:
            first.append((p1, p2))
        else:
            second.append((p1, p2))
    
    first.sort(key=lambda x: x[0])
    second.sort(key=lambda x: x[1], reverse=True)
    
    order = first + second
    
    draft_end = 0
    render_end = 0
    for p1, p2 in order:
        draft_end += p1
        if render_end < draft_end:
            render_end = draft_end
        render_end += p2
    
    print(render_end)

if __name__ == "__main__":
    main()