# Problem B — Observatory Schedule

Time limit: 1 s   Memory limit: 256 MB

## Description

An astronomical observatory needs to process $j$ target star systems. For each target, two sequential phases must occur: 
1. The physical telescope must gather light for the target.
2. The mainframe must render the resulting data into an image.

The observatory operates under the following mechanics:
- The telescope can only gather light for one target at a time.
- The mainframe can only render data for one target at a time.
- The mainframe cannot begin rendering a target until the telescope has completely finished gathering light for that specific target.
- You must provide a single ordered list of the targets. The telescope will process the targets in this exact sequence. The mainframe will also process the targets in this exact same sequence.
- Each phase of work for a target begins as early as possible without violating the above rules.

You are guaranteed that the sum of the light-gathering durations for all targets combined will never exceed $200,000,000,000$, and the sum of the rendering durations will never exceed $200,000,000,000$. 

Determine the optimal target sequence to minimize the timestamp at which the mainframe finishes rendering the final target in the list. Report this minimum possible completion timestamp.

## Input

The first line contains a single integer $j$ ($1 \le j \le 200,000$), representing the number of target star systems.
Each of the following $j$ lines contains two integers $g$ and $r$ ($1 \le g, r \le 1,000,000$). For a given target, $g$ is the time required for the telescope to gather light, and $r$ is the time required for the mainframe to render the data.

## Output

Print a single integer: the earliest possible timestamp at which the mainframe completes the rendering of all targets.

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

In Example 2, the single target requires 5 time units for the telescope to gather light, and then 3 time units for the mainframe to render it, finishing at timestamp 8.
