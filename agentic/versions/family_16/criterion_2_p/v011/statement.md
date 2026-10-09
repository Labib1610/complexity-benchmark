# Problem B — Museum Restoration

Time limit: 1 s   Memory limit: 256 MB

## Description

A museum has received a collection of **j** antique artifacts that require immediate restoration. The restoration process for each artifact consists of exactly two sequential phases:
1. Chemical cleaning, performed by the Chief Chemist.
2. Structural repair, performed by the Master Sculptor.

The restoration strictly follows these protocols:
- The Chemist works on only one artifact at a time.
- The Sculptor works on only one artifact at a time.
- The Sculptor cannot begin repairing a specific artifact until the Chemist has completely finished cleaning that same artifact.
- To maintain an orderly workflow, the artifacts must be processed in the exact same sequence by both experts. You must choose this sequence.

Assume the Chemist begins working on the first artifact at time 0. When an expert finishes an artifact, they can immediately start their work on the next one in the sequence, provided it is available to them. Choose the sequence of artifacts to minimize the time at which the Sculptor finishes the final artifact. Report this minimum completion time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **c** and **r** (1 ≤ c, r ≤ 1000000): the time required for cleaning and the time required for repairing the artifact, respectively.

## Output

Print a single integer: the earliest possible time at which all artifacts are fully restored (i.e., the Sculptor finishes the final artifact).

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

In Example 2 the single artifact takes 5 units of time to clean and then 3 units to repair, finishing at time 8.
