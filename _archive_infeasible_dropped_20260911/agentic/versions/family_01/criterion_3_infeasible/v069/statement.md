# Problem C — Phase 2: Roster Evaluation

Time limit: 2 s   Memory limit: 256 MB

The factory's annual shift allocation system operates in three distinct phases. In Phase 1, the automated scheduling software generates a baseline roster based purely on availability and skill requirements, completely ignoring personal incompatibilities. 

You are responsible for executing Phase 2: Roster Evaluation. The system provides you with the number of personnel and a comprehensive log of known interpersonal incompatibilities. Your objective in this phase is to scan the Phase 1 data to identify a triad of distinct employees where every individual in the triad is incompatible with both of the others. The preceding phase's generator guarantees that at least one such triad exists in the provided data.

Once you isolate this group, their details are passed to Phase 3. In this final step, the Human Resources department schedules a mandatory mediation session for those specific employees before the final roster is published. To ensure the automated HR system processes the earliest-indexed employees first, you must report the triad that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of personnel and the number of logged incompatibilities, respectively. Personnel are numbered from $1$ to $n$.

Each of the following $m$ lines contains two integers $u$ and $v$, indicating that employee $u$ and employee $v$ are incompatible.

It is guaranteed that the data contains at least one triad of employees who are all mutually incompatible.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the identified triad of employees where $a$ is incompatible with $b$, $a$ is incompatible with $c$, and $b$ is incompatible with $c$. You must output the lexicographically smallest such triad (the one with the smallest $a$; in case of ties, the smallest $b$; and then the smallest $c$).

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
