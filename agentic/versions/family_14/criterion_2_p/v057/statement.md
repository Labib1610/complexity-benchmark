# Quarantine Network Assembly

Time limit: 2 s
Memory limit: 256 MB

## Description

During a critical security breach, the facility mainframe executes a four-step containment procedure. You must implement the logic for Step C.

1. **Step A (Topology Discovery)**: The mainframe maps **n** processing units (numbered 1 to n) and a fixed infrastructure of **m** bidirectional data channels. This infrastructure is minimal and fully integrated: there are exactly **n − 1** channels, and any two units can communicate via exactly one non-repeating sequence of channels.
2. **Step B (Threat Isolation)**: The intrusion detection system flags exactly **t** units that exhibit abnormal behavior.
3. **Step C (Quarantine Network Assembly - Your Task)**: To coordinate a synchronized reset, the mainframe must activate a subset of the data channels. The chosen channels must form a unified communication network that includes all **t** flagged units. Unflagged units may be part of this network to bridge connections. Each channel has a known activation latency, and the total latency is the sum of the activation latencies of all chosen channels. Your program must calculate the absolute minimum total latency required to form this network.
4. **Step D (Firmware Rollback)**: The isolated network broadcasts the reset sequence to the flagged units.

Given the infrastructure layout and the list of flagged units from Step B, calculate the minimum total latency required to complete Step C.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the identifiers of the flagged units.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a data channel connecting unit u to unit v with an activation latency of w. The channels form the infrastructure discovered in Step A.

## Output

Print a single integer: the minimum total latency required to link all flagged units.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```
