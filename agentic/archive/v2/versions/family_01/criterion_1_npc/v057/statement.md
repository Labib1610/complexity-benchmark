# Automated Assembly Pipeline: Phase Allocation Module

Time limit: 2 s   Memory limit: 256 MB

As part of an automated smart-factory workflow, daily manufacturing runs through three consecutive operational stages (designated as Stage 1, Stage 2, and Stage 3). Prior to starting operations, the facility's supervisory control system executes a multi-step setup pipeline:

1. **Phase Allocation Module** (Your Task): Assign each of $n$ active machinery units, indexed from $1$ to $n$, to exactly one operational stage ($1, 2, \text{or } 3$). Certain pairs of units share power conduits or physical calibration lines, creating mutual interference. Two units that form an interfering pair cannot be assigned to the same operational stage.
2. **Load Balancing Module** (Downstream): Receives the phase assignments and optimizes power distribution curves.
3. **Safety Verification Module** (Downstream): Validates physical interlocks before start-up.

To maintain deterministic behavior across the factory software stack, if multiple valid stage assignment sequences $s_1, s_2, \dots, s_n$ exist, the Phase Allocation Module must select the sequence that is lexicographically smallest. If no valid stage assignment can satisfy all mutual interference conditions, the pipeline must abort.

Your task is to implement the Phase Allocation Module.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the number of active machinery units and the number of interfering unit pairs.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$) representing an interfering pair of machinery units.

## Output
If no valid stage assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$), where $s_i$ denotes the assigned operational stage for unit $i$. Among all valid assignments, print the lexicographically smallest sequence.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```
