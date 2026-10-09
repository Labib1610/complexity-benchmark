# Problem A — Stable Testing Configuration

Time limit: 5 s   Memory limit: 256 MB

## Description

An automated testing facility is evaluating **n** hardware prototypes, assigned integer identifiers from 1 to **n**. 

During the initialization phase, the facility's diagnostic system records **m** instances of electromagnetic interference. Each recorded instance involves exactly two prototypes that emit conflicting frequencies when active simultaneously. 

A testing configuration consists of a subset of prototypes powered on at the same time. A configuration is deemed stable if and only if no two prototypes within the subset have a recorded instance of interference between them. 

The facility's power supply is currently calibrated to support a specific load, requiring exactly **k** prototypes to be active during the main test. 

Your task is to determine whether a stable testing configuration of exactly **k** prototypes exists, and if so, to specify the prototypes to include.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing an instance of interference between prototype **u** and prototype **v**. No interference instance is listed twice.

## Output

If a stable testing configuration of **k** prototypes exists, print `YES` on the first line, then on the second line print **k** distinct prototype identifiers forming such a configuration, separated by spaces. Any configuration in which no two prototypes interfere is accepted.

If no such configuration exists, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 3
1 2
1 3
2 3
3 4
```

**Output**
```
NO
```

### Example 2

**Input**
```
5 2 3
1 2
3 4
```

**Output**
```
YES
1 3 5
```

### Example 3

**Input**
```
3 3 1
1 2
2 3
1 3
```

**Output**
```
YES
1
```
