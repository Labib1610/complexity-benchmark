# Problem B — Canal Convoy

Time limit: 1 s   Memory limit: 256 MB

## Description

A fleet of **j** vessels must travel down a narrow canal. Because overtaking is impossible, you must arrange the fleet into a strict entry sequence.

The canal's automated tracking system records two milestones for every vessel: the *Bow Ping* and the *Stern Ping*. Each vessel has a specific bow parameter and a specific stern parameter.

Once the entry sequence is chosen, the timeline of events unfolds strictly as follows:
- The first vessel in the sequence registers its Bow Ping at a time equal to its bow parameter. It registers its Stern Ping at a time equal to its bow parameter plus its stern parameter.
- Each subsequent vessel registers its Bow Ping exactly its own bow parameter units of time after the preceding vessel's Bow Ping.
- Each subsequent vessel registers its Stern Ping exactly its own stern parameter units of time after the later of the following two events: its own Bow Ping, and the preceding vessel's Stern Ping.

You are given the bow and stern parameters for each vessel. Determine the arrangement of the fleet that minimizes the time at which the final vessel registers its Stern Ping. Output this minimum possible time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains exactly 2 integers **t1** and **t2** (1 ≤ t1, t2 ≤ 1000000): the bow parameter and the stern parameter of a vessel.

## Output

Print a single integer: the smallest possible time at which the last vessel registers its Stern Ping.

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

In Example 2, the single vessel has a bow parameter of 5 and a stern parameter of 3. It registers its Bow Ping at time 5, and its Stern Ping at time 5 + 3 = 8.