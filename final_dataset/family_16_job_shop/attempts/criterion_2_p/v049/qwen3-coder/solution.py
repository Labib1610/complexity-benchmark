import sys
import threading

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    manuscripts = []
    index = 1
    for i in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        manuscripts.append((p1, p2))
        index += 2
    
    # Sort using Johnson's rule
    # Split into two groups:
    # Group1: p1 <= p2
    # Group2: p1 > p2
    group1 = []  # p1 <= p2, sort by p1 ascending
    group2 = []  # p1 > p2, sort by p2 descending
    
    for i in range(j):
        p1, p2 = manuscripts[i]
        if p1 <= p2:
            group1.append((p1, p2, i))
        else:
            group2.append((p1, p2, i))
    
    group1.sort(key=lambda x: x[0])  # Sort by transcription time ascending
    group2.sort(key=lambda x: x[1], reverse=True)  # Sort by binding time descending
    
    # Combine the groups: group1 first, then group2
    ordered = group1 + group2
    
    # Calculate the minimum completion time
    time_transcription = 0
    time_completion = 0
    
    for p1, p2, idx in ordered:
        time_transcription += p1
        time_completion = max(time_completion, time_transcription) + p2
    
    print(time_completion)

# Use threading to increase recursion limit if needed, though not necessary for this implementation
threading.Thread(target=main).start()