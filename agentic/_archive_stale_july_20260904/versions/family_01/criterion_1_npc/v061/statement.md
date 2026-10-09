# Problem A — Automated Fabrication Routing

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant utilizes $n$ automated fabrication modules. To maintain operational safety, you must configure the activation schedule for these modules based on the plant's physical constraints.

The plant's power grid provides exactly three distinct activation phases, labeled 1, 2, and 3. Your task is to assign each fabrication module to exactly one of these three phases.

During early testing, an interference log was generated containing $m$ records. Each record identifies a pair of modules that share a spatial trajectory. If any two modules in a recorded pair are assigned to the same activation phase, their operations will intersect and trigger a safety shutdown. Therefore, you must ensure that for every pair in the interference log, the two modules are assigned to different phases.

The master controller requires a deterministic configuration. The phase assignments for modules 1 through $n$ form a sequence of $n$ integers. Among all sequences that satisfy the safety constraints, you must output the one that is lexicographically smallest. This means you must select the valid assignment that minimizes the phase for module 1; if there are ties, minimize the phase for module 2, and so on.

If there is no way to assign the phases without violating the interference log, the system must abort the sequence.

## Input
The first line contains two integers $n$ and $m$ (1 ≤ $n$ ≤ 40, 0 ≤ $m$ ≤ $n \cdot (n-1)/2$) — the number of fabrication modules and the number of interference records. 
Each of the next $m$ lines contains two integers $u$ and $v$ (1 ≤ $u, v$ ≤ $n$, $u \neq v$), representing a pair of modules that share a spatial trajectory.

## Output
If no safe phase assignment is possible, output a single line containing `NO`. 
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $p_1, p_2, \dots, p_n$ (each being 1, 2, or 3), where $p_i$ is the activation phase assigned to module $i$. The sequence $p_1, \dots, p_n$ must be the lexicographically smallest valid assignment.

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
