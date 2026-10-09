# Problem A — Studio Coordination

Time limit: 5 s   Memory limit: 256 MB

## Description

A creative agency operates **m** facilities and has accepted **j** campaigns. Each campaign dictates a strict progression of segments. Each segment demands the exclusive use of a particular facility for a certain number of hours.

The rules of execution are as follows:
- The segments of a campaign must be undertaken precisely in the order they are provided. A segment can only be initiated after the preceding segment of that same campaign has fully concluded.
- Each facility can accommodate at most one segment at any given time.
- Once a segment is initiated at a facility, it must run continuously until its required duration is met, without being paused or interrupted.

Plan the execution of all segments so that the moment when all campaigns are fully completed is as early as possible. Output this earliest possible hour.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines details a single campaign. It begins with an integer **o** (the number of segments in this campaign), followed by **o** pairs of integers formatted as `facility duration` (1 ≤ facility ≤ m, 1 ≤ duration ≤ 1000). These pairs are given in the strict order they must be performed.
The combined number of segments across all campaigns will not exceed 50.

## Output

Print a single integer: the earliest possible hour by which every campaign is fully concluded.

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

## Note

In Example 1, two identical campaigns each progress through facilities 1, 2, and 3 (taking 2 hours per segment). The second campaign follows directly behind the first, concluding at hour 8. In Example 3, the two campaigns utilize distinct facilities and run simultaneously, concluding at hour 4.
