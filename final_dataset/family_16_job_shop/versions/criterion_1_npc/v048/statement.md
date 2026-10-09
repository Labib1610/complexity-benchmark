# Problem A — Production Pipeline

Time limit: 5 s   Memory limit: 256 MB

## Description
You are building a production management tool for a record label. The label's workflow consists of three distinct phases: pre-production, tracking, and mastering.

During the pre-production phase, the musical director prepares **j** songs, deciding exactly which studio equipment (from a pool of **m** items) is needed. For each song, they create an ordered itinerary of recording tasks. Each task specifies the required equipment and the exact number of minutes it will take to record. 

Your software is responsible for scheduling the tracking phase. You must schedule all tasks subject to the studio's physical limitations:
- A song's itinerary is strictly sequential. A task for a given song cannot begin until the preceding task in that song's itinerary has completely finished.
- A piece of equipment can only be used for one task at a time.
- Once a task begins, it must run continuously until its duration is fulfilled. It cannot be split or paused.

Once the tracking phase concludes, the mastering phase begins. Mastering requires all tasks for all songs to be completely finished.

Given the pre-production itineraries, calculate the earliest possible minute that the mastering phase can begin (assuming tracking starts at minute zero).

## Input
The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines describes one song's itinerary: an integer **o** (the number of tasks) followed by **o** pairs of integers `equipment duration` (1 ≤ equipment ≤ m, 1 ≤ duration ≤ 1000), listing the song's tasks in their mandatory sequence.
The total number of tasks across all songs is at most 50.

## Output
Print a single integer: the minimum total number of minutes required to finish the tracking phase.

## Examples

### Example 1
**Input**
```
2 3
3 1 2 2 2 3 2
3 1 2 2 2 3 2
```
**Output**
```
8
```

### Example 2
**Input**
```
1 3
3 1 5 2 3 3 2
```
**Output**
```
10
```

### Example 3
**Input**
```
2 3
1 1 4
1 2 3
```
**Output**
```
4
```
