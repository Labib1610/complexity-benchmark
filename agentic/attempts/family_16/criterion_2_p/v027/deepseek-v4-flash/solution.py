import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    idx = 1
    ins_times = []
    chan_times = []
    for _ in range(j):
        p1 = int(data[idx]); p2 = int(data[idx+1])
        idx += 2
        ins_times.append(p1)
        chan_times.append(p2)
    
    ins_finish = 0
    chan_finish = 0
    for i in range(j):
        ins_finish += ins_times[i]
        if chan_finish < ins_finish:
            chan_finish = ins_finish
        chan_finish += chan_times[i]
    
    print(chan_finish)

if __name__ == "__main__":
    main()