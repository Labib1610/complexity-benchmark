# Problem B — Museum Calibration

Time limit: 1 s   Memory limit: 256 MB

A museum curator is setting up an exhibition featuring $n$ historical artifacts, sequentially cataloged from 1 to $n$. Each artifact requires a specific lighting calibration level, which must be set to either level 1 or level 2.

During the planning phase, the curator identified $m$ specific pairs of artifacts that are wired to the same sensitive power circuit. To maintain electrical stability and prevent surges, the safety guidelines require that for every such pair, the sum of their assigned lighting calibration levels must be exactly 3.

Your task is to assign a calibration level to each artifact in a way that respects all circuit constraints. If it is impossible to satisfy all the conditions, you must report this. In cases where multiple valid assignments exist, the museum's control system requires you to output the sequence of calibration levels that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of artifacts and the number of circuit-sharing pairs.
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that artifact $u$ and artifact $v$ share a circuit.

## Output
If no valid assignment is possible, output a single line containing `NO`.
Otherwise, output a line containing `YES`. On the following line, output $n$ space-separated integers $h_1, h_2, \dots, h_n$ (where each $h_i \in \{1, 2\}$) representing the assigned calibration level for each artifact. This sequence must be the lexicographically smallest among all valid assignments.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```