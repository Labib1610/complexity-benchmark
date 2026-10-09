import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    j = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    sessions = []
    for _ in range(j):
        o = int(data[idx]); idx += 1
        segments = []
        for _ in range(o):
            instrument = int(data[idx]); idx += 1
            duration = int(data[idx]); idx += 1
            segments.append((instrument, duration))
        sessions.append(segments)
    
    # Track when each instrument becomes available
    instrument_free = [0] * (m + 1)
    
    total_time = 0
    
    for segments in sessions:
        current_time = 0
        for instrument, duration in segments:
            # Wait until instrument is free and previous segment done
            start_time = max(current_time, instrument_free[instrument])
            end_time = start_time + duration
            instrument_free[instrument] = end_time
            current_time = end_time
        total_time = max(total_time, current_time)
    
    print(total_time)

if __name__ == "__main__":
    solve()