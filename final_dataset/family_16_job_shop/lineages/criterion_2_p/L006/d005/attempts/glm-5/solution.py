import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(input_data[idx]); idx += 1
    
    pos = []  # p2 >= p1
    neg = []  # p2 < p1
    total_p1 = 0
    
    for _ in range(j):
        p1 = int(input_data[idx]); idx += 1
        p2 = int(input_data[idx]); idx += 1
        total_p1 += p1
        if p2 >= p1:
            pos.append((p1, p2))
        else:
            neg.append((p1, p2))
    
    pos.sort(key=lambda x: x[0])  # by p1 ascending
    neg.sort(key=lambda x: x[1], reverse=True)  # by p2 descending
    
    battery = 0
    deficit = 0
    
    for p1, p2 in pos:
        if battery < p1:
            deficit += p1 - battery
            battery = 0
        else:
            battery -= p1
        battery += p2
    
    for p1, p2 in neg:
        if battery < p1:
            deficit += p1 - battery
            battery = 0
        else:
            battery -= p1
        battery += p2
    
    print(total_p1 + battery)

main()