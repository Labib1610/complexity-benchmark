# Problem A — Studio Sessions

Time limit: 5 s   Memory limit: 256 MB

## Description

An audio studio is producing **j** compositions using **m** distinct instruments. Each composition requires recording a sequence of audio segments. Every segment dictates that a specific instrument be played for a precise number of minutes.

The studio operates under these physical constraints:
- Within any single composition, the segments must be recorded in their given sequence. A segment cannot begin until the immediately preceding segment of that composition has fully concluded.
- Any given instrument can only be involved in one segment at a time.
- Once a segment starts recording, it must run continuously until its required duration is met. It cannot be paused or split.

Find the earliest possible minute by which the final segment of every composition can be completely recorded.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines describes one composition: an integer **o** (the number of segments) followed by **o** pairs of integers `instrument duration` (1 ≤ instrument ≤ m, 1 ≤ duration ≤ 1000), listing the composition's segments in their mandatory sequence.
The total number of segments across all compositions is at most 50.

## Output

Print a single integer: the minimum total number of minutes required to finish recording all compositions.

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
