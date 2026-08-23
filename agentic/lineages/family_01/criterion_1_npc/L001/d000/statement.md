# Problem A — HR Workflow Automation

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant is updating its employee onboarding workflow, which consists of four sequential stages:

1. **Recruitment:** Human resources finalizes the hiring of $n$ employees, assigning each an ID from $1$ to $n$.
2. **Vetting:** The security team conducts background checks and identifies $m$ pairs of employees who have prior disputes. These pairs are flagged as incompatible.
3. **Scheduling:** The operations department must assign every employee to exactly one of the three daily work periods (labeled 1, 2, and 3). To ensure a safe environment, no two employees flagged as incompatible in the Vetting stage can be assigned to the same work period.
4. **Badge Generation:** The IT department generates access badges based on the schedule. If a valid schedule exists, the system requires an ordered sequence of work periods for employees $1$ through $n$. To maintain a deterministic database, if multiple valid schedules are possible, the system mandates the sequence that is lexicographically smallest. If no valid schedule can be formed, the HR system must be notified to halt the onboarding process.

Your task is to implement the software module that bridges Stage 2 and Stage 4. Given the number of employees and the incompatible pairs identified in Stage 2, you must determine the work period assignments required for Stage 4, or determine that the workflow must be halted.

## Input
The first line contains two integers $n$ and $m$ — the number of employees from Stage 1 and the number of incompatible pairs from Stage 2 ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — representing a pair of employees who cannot share the same work period.

## Output
If the workflow must halt because no valid assignment is possible, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the work period of employee $i$. Among all valid assignments, output the lexicographically smallest sequence (compare $s_1$ first, then $s_2$, and so on).

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
