import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    j = int(sys.stdin.readline())
    sectors = []
    for _ in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        sectors.append((p1, p2))
    
    # Sort sectors by p1 - p2 in descending order
    sectors.sort(key=lambda x: x[0] - x[1], reverse=True)
    
    primary_tracker = 0
    secondary_tracker = 0
    
    for p1, p2 in sectors:
        baseline = secondary_tracker - p1
        threshold = primary_tracker + p1
        target_value = max(baseline, threshold)
        primary_tracker += p1
        secondary_tracker = target_value + 2 * p2
    
    result = (primary_tracker + secondary_tracker) // 2
    print(result)

threading.Thread(target=main).start()