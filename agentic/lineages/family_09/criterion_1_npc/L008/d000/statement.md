# Orbital Payload Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description

A new satellite requires exactly **k** distinct hardware modules chosen from a catalog of **n** available modules (numbered 1 to **n**). 

During ground testing, **m** power anomalies were documented. Each anomaly is triggered if a specific pair of modules are both included in the payload, drawing incompatible currents. 

A payload is considered viable if it contains exactly **k** modules and no two modules in the payload correspond to any of the documented anomalies.

Determine whether a viable payload can be assembled, and if so, list the modules to include.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), indicating that including both module **u** and module **v** triggers a power anomaly. No pair of modules is listed more than once.

## Output

If a viable payload of **k** modules exists, print `YES` on the first line. On the second line, print the **k** distinct module numbers that form this payload, separated by spaces. If multiple such payloads exist, any of them is accepted.

If no viable payload can be assembled, print `NO`.

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
