# Problem A — Production Cycle Integration

Time limit: 2 s   Memory limit: 256 MB

The manufacturing division of a large corporation has recently completed its annual recruitment phase, hiring $n$ specialists. During onboarding, HR conducted compatibility assessments and identified several pairs of specialists who have interpersonal friction.

As the scheduling coordinator, your job is the second phase of the integration process: cycle allocation. The factory operates on a continuous schedule broken into three daily production cycles, designated as Cycle 1, Cycle 2, and Cycle 3. You must allocate every specialist to exactly one of these three cycles. To maintain productivity, your allocation must ensure that no two specialists who have interpersonal friction are assigned to the same cycle. 

If this phase is completed successfully, the process moves to the third phase: payroll configuration, where specialists are compensated based on their assigned cycle. To standardize the payroll system, company policy dictates a strict tie-breaking rule for the cycle allocation. If there are multiple valid ways to allocate the specialists without violating the friction constraints, you must choose the one that minimizes the cycle designations when read in order from specialist 1 to specialist $n$ (i.e., comparing the cycle of specialist 1 first, then specialist 2, and so on, always preferring lower cycle numbers). If it is impossible to complete the cycle allocation phase without placing a friction pair together, the entire integration process must be halted.

## Input
The first line of the input contains two integers $n$ and $m$ — the number of specialists recruited and the number of friction pairs identified during onboarding ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
The following $m$ lines each contain two integers $u$ and $v$, representing a pair of specialists who have interpersonal friction.

## Output
If the cycle allocation phase cannot be completed without violating constraints, output a single line containing `NO`.
If a valid allocation is possible, output `YES` on the first line. On the second line, output $n$ integers $c_1, c_2, \dots, c_n$ (where each $c_i \in \{1, 2, 3\}$), representing the cycle assigned to each specialist $i$. This sequence must be the valid allocation that is lexicographically smallest.

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
