# Problem A — RTOS Priority Allocation

Time limit: 2 s   Memory limit: 256 MB

A real-time operating system (RTOS) is being configured to run $n$ concurrent tasks, numbered $1$ to $n$. Each task must be assigned exactly one static priority tier: $1$ (low), $2$ (medium), or $3$ (high).

During static analysis, the compiler identified $m$ pairs of tasks that read and write to the same shared memory registers. To guarantee deterministic preemption and prevent race conditions, the RTOS arbiter enforces a strict rule: any two tasks that share memory registers must not be assigned the same priority tier. If they were to have identical priority tiers, the arbiter could not resolve simultaneous access requests, leading to a system fault.

The configuration file requires the priority assignment to be listed as a sequence of $n$ integers, where the $i$-th integer is the priority tier of task $i$. To ensure the configuration is reproducible, if there are multiple valid assignments that satisfy all arbiter rules, the compiler must generate the sequence that is lexicographically smallest.

If it is impossible to assign priority tiers to all tasks without violating the arbiter's rules, the compiler must abort the build.

## Input
The first line contains two integers $n$ and $m$ — the number of tasks and the number of pairs sharing memory registers ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — representing a pair of tasks that share memory registers and therefore cannot have the same priority tier.

## Output
If no valid priority assignment is possible, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $p_1, p_2, \dots, p_n$ (where each $p_i \in \{1, 2, 3\}$), representing the priority tier assigned to task $i$. Among all valid assignments, output the sequence that is lexicographically smallest (compare $p_1$ first, then $p_2$, and so on).

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