import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    packets = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        packets.append((p1, p2))
        idx += 2
    
    # Sort by p1 ascending, then p2 descending
    packets.sort(key=lambda x: (x[0], -x[1]))
    
    time = 0
    arrival = 0
    for p1, p2 in packets:
        arrival += p1
        if time < arrival:
            time = arrival
        time += p2
    
    print(time)

if __name__ == "__main__":
    main()