# Problem A — RTOS Stage Allocation

Time limit: 2 s   Memory limit: 256 MB

A real-time operating system (RTOS) is being configured to run $n$ concurrent tasks, numbered $1$ to $n$. Each task must be assigned exactly one execution stage: $1$, $2$, or $3$.

During static analysis, the compiler identified $m$ pairs of tasks that read and write to the same shared memory registers. To guarantee deterministic preemption and prevent race conditions, the RTOS arbiter enforces a strict separation rule. For any two tasks $u$ and $v$ that share memory registers, their assigned execution stages $s_u$ and $s_v$ must satisfy the condition $|s_u - s_v| \ge 1$. This separation ensures the arbiter can resolve access requests without a system fault.

The configuration file requires the stage assignment to be listed as a sequence of $n$ integers, where the $i$-th integer is the stage of task $i$. To ensure the configuration is reproducible, if there are multiple valid assignments that satisfy all arbiter rules, the compiler must generate the sequence that is lexicographically smallest.

If it is impossible to assign stages to all tasks without violating the arbiter's rules, the compiler must abort the build.

## Input
The first line contains two integers $n$ and $m$ — the number of tasks and the number of pairs sharing memory registers ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — representing a pair of tasks that share memory registers and therefore must satisfy the separation condition.

## Output
If no valid stage assignment is possible, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the stage assigned to task $i$. Among all valid assignments, output the sequence that is lexicographically smallest (compare $s_1$ first, then $s_2$, and so on).

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