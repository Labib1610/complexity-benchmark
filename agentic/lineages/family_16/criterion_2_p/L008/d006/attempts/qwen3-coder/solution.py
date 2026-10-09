import sys
import threading

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    sectors = []
    index = 1
    for _ in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        sectors.append((p1, p2))
        index += 2
    
    # Sort sectors based on p2 - p1 in descending order
    # If p2 - p1 is same, we can sort by p1 ascending to break ties (optional but consistent)
    sectors.sort(key=lambda x: (x[1] - x[0], x[0]))
    
    battery_charge = 0
    accumulated_cost = 0
    
    for p1, p2 in sectors:
        allocated = min(p1, battery_charge)
        battery_charge -= allocated
        battery_charge += p2
        accumulated_cost += p1 + p2 - allocated
    
    print(accumulated_cost)

threading.Thread(target=main).start()