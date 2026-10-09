import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    files = []
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        files.append((p1, p2))
    
    # Sort by p2 descending (Johnson's rule for two-machine flow shop)
    files.sort(key=lambda x: -x[1])
    
    time_compressor_free = 0
    time_encryptor_free = 0
    
    for p1, p2 in files:
        # Compressor starts this file when it becomes free
        start_compression = time_compressor_free
        end_compression = start_compression + p1
        time_compressor_free = end_compression
        
        # Encryption starts when both compression is done and encryptor is free
        start_encryption = max(end_compression, time_encryptor_free)
        end_encryption = start_encryption + p2
        time_encryptor_free = end_encryption
    
    print(time_encryptor_free)

if __name__ == "__main__":
    solve()