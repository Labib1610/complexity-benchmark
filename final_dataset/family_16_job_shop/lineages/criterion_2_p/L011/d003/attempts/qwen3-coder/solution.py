import sys
import threading

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    performances = []
    index = 1
    for i in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        performances.append((p1, p2))
        index += 2
    
    # Sort by p2 descending (earliest deadline first for review room)
    # For same p2, sort by p1 ascending (shorter main stage first)
    performances.sort(key=lambda x: (-x[1], x[0]))
    
    current_time_main_stage = 0
    current_time_review_room = 0
    
    for p1, p2 in performances:
        # Main stage finishes at current_time_main_stage + p1
        current_time_main_stage += p1
        # Review room starts when both main stage is done AND previous review is done
        current_time_review_room = max(current_time_review_room, current_time_main_stage) + p2
    
    print(current_time_review_room)

threading.Thread(target=main).start()