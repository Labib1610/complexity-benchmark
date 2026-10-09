# Problem A — Payload Selection

Time limit: 5 s   Memory limit: 256 MB

## Description

You must select exactly **k** scientific experiments from a candidate pool of **n** (numbered 1 to **n**) to form a complete rover payload.

Each experiment requires specific hardware, and some pairs of experiments require the same exclusive hardware component. Because exclusive components cannot be shared or duplicated, any two experiments requiring the same component cannot both be included in the payload.

You are provided with a list of **m** known hardware conflicts, each indicating a pair of experiments that are mutually incompatible. Determine whether it is possible to choose exactly **k** experiments such that no two selected experiments have a hardware conflict, and if so, identify one such valid set.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ **n** ≤ 46, 0 ≤ **m** ≤ **n**·(**n**−1)/2, 1 ≤ **k** ≤ **n**).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), representing a hardware conflict between experiment **u** and experiment **v**. No conflict is listed more than once.

## Output

If a valid payload of **k** experiments exists, print `YES` on the first line. On the second line, print the **k** distinct experiment numbers forming the payload, separated by spaces. If multiple valid sets of **k** experiments exist, you may output any one of them.

If no such payload can be formed, print `NO`.

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
