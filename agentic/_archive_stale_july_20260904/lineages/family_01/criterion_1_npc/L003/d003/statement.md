# Problem A — Shift Distribution

Time limit: 2 s
Memory limit: 256 MB

A manufacturing plant employs $n$ workers. To maintain continuous production, the plant operates on three daily shifts, labeled 1, 2, and 3. Each worker must be scheduled for exactly one of these three shifts. 

Due to historical disagreements, certain pairs of distinct workers cannot be scheduled together. You are given a log of these incompatibilities. If two workers appear together in a conflict record, they are forbidden from sharing the same shift. The conflict logs can form dense, highly interconnected webs of restrictions. The evaluation tests include full-capacity scenarios with intricate conflict structures designed to test the efficiency of your scheduling method, so your approach must be capable of processing demanding configurations.

Your task is to determine whether it is possible to schedule all $n$ workers into the three shifts without violating any conflict restrictions. If a valid schedule exists, you must find the one that minimizes the objective function $\sum_{i=1}^n s_i \cdot 4^{n-i}$, where $s_i$ is the shift number assigned to worker $i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$). The workforce size $n$ is at least 1 and is bounded by the plant's maximum capacity of exactly 40 workstations. The integer $m$ represents the total number of conflict records.

Each of the following $m$ lines contains two integers $u$ and $v$ — a pair of distinct workers who cannot be assigned to the same shift.

## Output
If there is no valid way to assign the shifts, output a single line containing `NO`.

If a valid assignment is possible, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$), where $s_i$ is the shift assigned to worker $i$. If multiple valid assignments exist, output the sequence $s_1, s_2, \dots, s_n$ that minimizes the value of $\sum_{i=1}^n s_i \cdot 4^{n-i}$.

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