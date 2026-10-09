import sys
import threading

def main():
    import sys
    j = int(sys.stdin.readline())
    requests = []
    for _ in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        requests.append((p1, p2))
    
    # Sort by p1 ascending and p2 descending for tie-breaking
    requests.sort(key=lambda x: (x[0], -x[1]))
    
    total_p1 = sum(p1 for p1, p2 in requests)
    max_time = 0
    current_p1_time = 0
    
    for p1, p2 in requests:
        current_p1_time += p1
        finish_time = current_p1_time + p2
        max_time = max(max_time, finish_time)
    
    print(max_time)

threading.Thread(target=main).start()