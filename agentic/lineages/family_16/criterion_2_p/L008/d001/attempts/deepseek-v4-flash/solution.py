import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    sectors = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx += 2
        sectors.append((p1, p2))
    
    first = []
    second = []
    for p1, p2 in sectors:
        if p1 <= p2:
            first.append((p1, p2))
        else:
            second.append((p1, p2))
    
    first.sort(key=lambda x: x[0])
    second.sort(key=lambda x: -x[1])
    
    order = first + second
    
    radar_time = 0
    sampling_time = 0
    for p1, p2 in order:
        radar_time += p1
        if sampling_time < radar_time:
            sampling_time = radar_time
        sampling_time += p2
    
    print(sampling_time)

if __name__ == "__main__":
    solve()