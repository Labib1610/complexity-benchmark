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
    
    # Sort by downlink time descending
    packets.sort(key=lambda x: x[1], reverse=True)
    
    up_time = 0
    down_time = 0
    
    for p1, p2 in packets:
        up_time += p1
        if down_time < up_time:
            down_time = up_time
        down_time += p2
    
    print(down_time)

if __name__ == "__main__":
    main()