def solve():
    n = int(input().strip())
    jobs = []
    for _ in range(n):
        s, d = map(int, input().split())
        jobs.append((s, d))
    
    A = []
    B = []
    for s, d in jobs:
        if s <= d:
            A.append((s, d))
        else:
            B.append((s, d))
    
    A.sort(key=lambda x: x[0])  # ascending surface time
    B.sort(key=lambda x: x[1], reverse=True)  # descending deep time
    
    sequence = A + B
    
    surface_end = 0
    deep_end = 0
    for s, d in sequence:
        surface_end += s
        if deep_end < surface_end:
            deep_end = surface_end
        deep_end += d
    
    print(deep_end)

if __name__ == "__main__":
    solve()