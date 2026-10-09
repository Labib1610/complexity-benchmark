# Pre-deployment Validation

Time limit: 2 s   Memory limit: 256 MB

Our automated workforce management pipeline consists of four distinct stages:

1. **Incompatibility profiling:** The system logs pairs of employees who cannot be assigned to the same operational shift due to skill overlap or equipment contention.
2. **Feasibility pre-check:** Before invoking the resource-intensive scheduling engine, the system verifies if a two-shift rotation is fundamentally possible. The pipeline is designed to immediately abort if it isolates a "deadlock triad"—a group of exactly three employees where every individual in the group is incompatible with every other individual in that same group. 
3. **Full schedule generation:** The core solver assigns all employees to shifts.
4. **Roster publication:** The final assignments are distributed to the workforce.

You are responsible for implementing the module for Stage 2. We already know from early heuristics that the current dataset is guaranteed to trigger an abort (i.e., at least one deadlock triad is present). Your module must generate the exact error log for the abort sequence by identifying such a group. 

To maintain deterministic error logs across runs, if multiple deadlock triads exist, your module must report the one that comes first lexicographically based on the employees' numerical IDs.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2\cdot 10^5)$), representing the number of employees and the number of logged incompatibilities.
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that employee $u$ and employee $v$ cannot share a shift.
It is guaranteed that at least one deadlock triad exists in the given data.

## Output
Print three integers $a$, $b$, and $c$ on a single line (sorted such that $a < b < c$), representing the IDs of the employees in the deadlock triad. Output the lexicographically smallest triad (minimize $a$; in case of ties, minimize $b$; then minimize $c$).

## Example 1
**Input:**
```
4 5
1 2
1 3
2 3
2 4
3 4
```
**Output:**
```
1 2 3
```

## Example 2
**Input:**
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
**Output:**
```
1 2 4
```
