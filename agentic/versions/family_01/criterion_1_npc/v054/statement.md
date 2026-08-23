# Problem A — Shift Allocation Protocol

Time limit: 2 s
Memory limit: 256 MB

A corporate processing center is overhauling its induction pipeline. The pipeline operates in a dedicated orientation hall containing exactly 8 rows of 5 biometric scanning stations.

During the initial phase, a cohort of new hires is processed. Each individual in the cohort is assigned a unique identifier from $1$ to $n$.

Next, a background screening system cross-references the cohort to find individuals with documented prior grievances. It produces a list of conflicting pairs. 

The core requirement is to allocate each person to a daily work shift. There are exactly three available shifts, designated by the integers 1, 2, and 3. Safety regulations dictate that if two individuals are listed as a conflicting pair, they must be allocated to different shifts.

Finally, the automated credential system must receive a complete allocation. An allocation is formatted as a sequence of $n$ shift numbers, where the $i$-th number is the shift assigned to the individual with identifier $i$. When several valid allocations exist that satisfy all safety regulations, the system requires the one that is lexicographically smallest (i.e., comparing the shift of hire 1 first, then hire 2, and so on). If it is impossible to allocate the shifts without violating safety regulations, the system must abort the pipeline.

Your objective is to build the logic that processes the cohort size and the list of conflicts to produce the required shift sequence or the abort signal.

## Input
The first line contains two integers $n$ and $m$. The integer $n$ represents the cohort size; it is at least 1 and at most the total number of scanning stations in the orientation hall. The integer $m$ represents the number of conflicting pairs; it is at least 0 and at most the total number of possible distinct pairs of individuals in the cohort.
Each of the next $m$ lines contains two integers $u$ and $v$, representing the identifiers of two individuals who have a documented grievance and cannot share the same shift.

## Output
If there is no way to allocate shifts safely, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers separated by spaces, each being 1, 2, or 3, representing the shift allocation for each individual from $1$ to $n$. Among all valid allocations, output the sequence that is lexicographically smallest.

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
