# Artifact Conveyance

Time limit: 1 s   Memory limit: 256 MB

## Description

An enchanter's workshop needs to empower $j$ magical artifacts. The empowerment process requires two distinct rituals for each artifact:
1. The Channeler imbues the artifact with raw magic.
2. The Binder permanently seals the magic inside.

The workshop employs exactly one Channeler and exactly one Binder. An artifact can only be sealed by the Binder after it has been fully imbued by the Channeler. 

To automate the workflow, you must choose an initial sequence for the artifacts. They will be placed onto a one-way magical track in this exact order. Because the track is strictly linear and artifacts cannot pass each other, the Binder will receive and process the artifacts in the exact same sequence that they were handled by the Channeler. 

There is ample space on the track between the two workers. If the Binder is currently busy with an artifact, any newly imbued artifacts simply queue up on the track. Neither worker can handle more than one artifact at a time, and they work continuously as long as they have an artifact available.

Your task is to determine the optimal sequence of artifacts to minimize the total time until the Binder finishes sealing the final artifact. Output this minimum possible completion time.

## Input

The first line contains a single integer $j$ ($1 \le j \le 200000$).
Each of the next $j$ lines contains two integers, $c$ and $b$ ($1 \le c, b \le 1000000$), representing the time required for the Channeler to imbue the artifact and the time required for the Binder to seal it, respectively.

## Output

Print a single integer: the earliest possible time at which all artifacts have been completely sealed.

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

In Example 2, the single artifact takes 5 units of time with the Channeler and then 3 units of time with the Binder, finishing at time 8.
