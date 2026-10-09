import sys
import threading

def main():
    import sys
    j = int(sys.stdin.readline())
    files = []
    for _ in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        files.append((p1, p2))
    
    # Sort files by p2 in descending order (Johnson's rule variation for two-machine flow shop)
    # For minimizing the makespan in two-stage processing, we use the Johnson's rule:
    # - If p1 <= p2, process earlier (but among these, sort by p1 ascending)
    # - If p1 > p2, process later (but among these, sort by p2 descending)
    # However, for this specific problem where we want to minimize completion time,
    # a simpler approach works well: sort by (p2 - p1) descending.
    # But actually, let's think more carefully.
    
    # The optimal strategy here is to apply Johnson's algorithm for two-machine flow shop scheduling
    # to minimize makespan:
    # Split jobs into two groups:
    # Group1: jobs where p1 <= p2
    # Group2: jobs where p1 > p2
    # Sort Group1 by p1 ascending
    # Sort Group2 by p2 descending
    # Concatenate Group1 + Group2
    
    group1 = []  # p1 <= p2
    group2 = []  # p1 > p2
    
    for i in range(j):
        p1, p2 = files[i]
        if p1 <= p2:
            group1.append((p1, p2, i))
        else:
            group2.append((p1, p2, i))
    
    # Sort group1 by p1 ascending
    group1.sort(key=lambda x: x[0])
    # Sort group2 by p2 descending
    group2.sort(key=lambda x: x[1], reverse=True)
    
    # Final sequence: group1 + group2
    sequence = group1 + group2
    
    # Now simulate the process
    compressor_time = 0
    encryptor_finish_time = 0
    # We need to track when each file finishes compression to start encryption
    # But since we're processing in order, we can just keep track of the encryptor queue
    
    # Actually, let's think of it step by step:
    # At any time, we know when the compressor will finish current job
    # and we know the queue of files waiting for encryption
    
    # Let's simulate with events or just track times
    
    compressor_free_time = 0
    encryptor_free_time = 0
    
    for p1, p2, idx in sequence:
        # File starts compression when compressor is free
        compressor_start = compressor_free_time
        compressor_free_time += p1
        
        # File finishes compression at compressor_free_time
        # It enters the encryptor queue at that time
        # The encryptor starts this file when:
        # 1. It's its turn in the FIFO queue
        # 2. The encryptor is free
        
        # Since we process in sequence, the file starts encryption at:
        # max(encryptor_free_time, compressor_free_time) 
        # because it needs to both finish compression and wait for encryptor availability
        encryptor_start = max(encryptor_free_time, compressor_free_time)
        encryptor_free_time = encryptor_start + p2
    
    print(encryptor_free_time)

if __name__ == '__main__':
    threading.Thread(target=main).start()