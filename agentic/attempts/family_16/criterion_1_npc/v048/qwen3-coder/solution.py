import heapq
from collections import defaultdict

def solve():
    j, m = map(int, input().split())
    
    # Read song itineraries
    songs = []
    for _ in range(j):
        line = list(map(int, input().split()))
        o = line[0]
        tasks = []
        for i in range(o):
            equipment = line[1 + 2*i]
            duration = line[1 + 2*i + 1]
            tasks.append((equipment, duration))
        songs.append(tasks)
    
    # For each song, calculate when each task can start
    # song_times[song_idx][task_idx] = earliest start time for this task
    song_times = [[] for _ in range(j)]
    
    # Keep track of when each equipment becomes free
    equipment_free_time = [0] * (m + 1)  # 1-indexed
    
    # Calculate start times for each song's tasks
    for song_idx in range(j):
        current_time = 0
        for equipment, duration in songs[song_idx]:
            # Task can start when both the previous task in this song is done
            # and the required equipment is free
            start_time = max(current_time, equipment_free_time[equipment])
            song_times[song_idx].append(start_time)
            end_time = start_time + duration
            equipment_free_time[equipment] = end_time
            current_time = end_time
    
    # The mastering phase can begin when all songs are completely tracked
    max_time = 0
    for song_idx in range(j):
        if song_times[song_idx]:  # If the song has tasks
            last_task_idx = len(songs[song_idx]) - 1
            last_task_end_time = song_times[song_idx][last_task_idx] + songs[song_idx][last_task_idx][1]
            max_time = max(max_time, last_task_end_time)
    
    print(max_time)

solve()