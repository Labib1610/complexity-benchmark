# Subsystem Activation Protocol

Time limit: 2 s   Memory limit: 256 MB

## Description

You are deploying a cluster of **n** sensor nodes, labeled 1 through **n**. Your goal is to activate exactly **k** nodes while leaving the rest dormant.

The cluster has **m** known interference pairs. Each pair represents two nodes that share a frequency channel; if both are activated simultaneously, their signals will jam. Your selected group of **k** nodes must be entirely free of these interference pairs.

The internal hardware dictates how interference occurs. Each node is manufactured with a specific, hidden, non-zero bias voltage. An interference pair can only exist between two nodes if their bias voltages perfectly cancel each other out (i.e., they sum to exactly zero). Nodes whose bias voltages do not sum to zero will never interfere. The exact bias voltages are proprietary and not provided, but the interference list is guaranteed to follow this physical rule.

Because you must select exactly **k** nodes from a pool of **n**, the total number of possible configurations is vast. You must determine if a safe deployment of exactly **k** nodes is possible.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), indicating an interference pair between node **u** and node **v**. No pair is listed twice, and all pairs are guaranteed to follow the bias voltage rule described above.

## Output

If a safe activation of exactly **k** nodes exists, print `YES` on the first line. On the second line, print **k** distinct node numbers to activate, separated by spaces. If multiple valid sets exist, any of them will be accepted.

If no such set is possible, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 2
1 3
1 4
2 3
2 4
```

**Output**
```
YES
1 2
```

### Example 2

**Input**
```
5 0 5
```

**Output**
```
YES
1 2 3 4 5
```

### Example 3

**Input**
```
4 4 3
1 3
1 4
2 3
2 4
```

**Output**
```
NO
```