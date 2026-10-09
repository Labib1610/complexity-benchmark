# Problem B — Canal Convoy

Time limit: 1 s   Memory limit: 256 MB

## Description

A fleet of **j** vessels must travel down a narrow canal. Each vessel requires a specific duration for its Alpha phase, and a subsequent duration for its Beta phase.

Because the canal is strictly one-lane and overtaking is physically impossible, the vessels must enter the canal one at a time. Your task is to choose the entry order of the fleet.

Once the entry order is chosen, the timeline of events is strictly determined by the canal's mechanics:
- The first vessel to enter begins its Alpha phase at time 0.
- Each subsequent vessel begins its Alpha phase at the exact moment the preceding vessel completes its Alpha phase.
- A vessel begins its Beta phase as early as possible, which occurs exactly when two conditions are met: it has finished its own Alpha phase, and the preceding vessel has entirely finished its Beta phase. (The first vessel begins its Beta phase the exact moment its Alpha phase ends).

You are given the Alpha phase duration and Beta phase duration for each vessel. Determine the entry order that minimizes the time at which the final vessel completes its Beta phase. Output this minimum possible completion time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains exactly 2 integers **t1** and **t2** (1 ≤ t1, t2 ≤ 1000000): the Alpha phase duration and the Beta phase duration of a vessel.

## Output

Print a single integer: the smallest possible time at which the last vessel completes its Beta phase.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 2, the single vessel takes 5 for its Alpha phase, finishing at time 5. It immediately begins its Beta phase, taking 3, and finishes at time 8.