# Problem C — Telemetry Window: Diagnostic Code

Time limit: 2 s   Memory limit: 256 MB

## Description

An orbital satellite executes **j** observation jobs within a mission window of **T** seconds. 

For each job $k \in \{1 \dots \mathbf{j}\}$, the telemetry system tracks the cumulative gimbal processing $G_k(t)$ and cumulative sensor processing $S_k(t)$ completed by time $t$. Both $G_k(t)$ and $S_k(t)$ are continuous, non-decreasing real-valued functions defined for $t \in [0, \mathbf{T}]$.

A physically valid execution must satisfy all of the following differential constraints:
1. **Boundary Limits:** For every job $k$, $G_k(0) = 0$ and $G_k(\mathbf{T}) = \mathbf{p1}_k$. Similarly, $S_k(0) = 0$ and $S_k(\mathbf{T}) = \mathbf{p2}_k$.
2. **Sequential Dependency:** For every job $k$, and for any time $t \in [0, \mathbf{T}]$, if $G_k(t) < \mathbf{p1}_k$, then $S_k(t) = 0$.
3. **Gimbal Bandwidth:** For any two times $t_a < t_b$ in $[0, \mathbf{T}]$, the total gimbal processing across all jobs is bounded by real time: $\sum_{k=1}^{\mathbf{j}} (G_k(t_b) - G_k(t_a)) \le t_b - t_a$.
4. **Sensor Bandwidth:** For any two times $t_a < t_b$ in $[0, \mathbf{T}]$, the total sensor processing across all jobs is bounded by real time: $\sum_{k=1}^{\mathbf{j}} (S_k(t_b) - S_k(t_a)) \le t_b - t_a$.

Mission control has determined that no valid execution functions $G_k(t)$ and $S_k(t)$ can exist for the current schedule. You must output a diagnostic code that identifies the isolated source of the failure. 

The telemetry data is guaranteed to trigger exactly one of the following isolated contradictions. Print the corresponding code:
- `JOB i` (where **i** is the 1-based job index): It is mathematically impossible to define functions $G_i(t)$ and $S_i(t)$ for job **i** that simultaneously satisfy Conditions 1, 2, 3, and 4 (assuming all other jobs are ignored and contribute $0$ to the sums). If multiple jobs satisfy this, you may output the code for any such job.
- `LOAD 1`: It is mathematically impossible to define functions $G_1(t) \dots G_j(t)$ for the full set of **j** jobs that simultaneously satisfy Conditions 1 and 3 (even if Conditions 2 and 4 are completely ignored).
- `LOAD 2`: It is mathematically impossible to define functions $S_1(t) \dots S_j(t)$ for the full set of **j** jobs that simultaneously satisfy Conditions 1 and 4 (even if Conditions 2 and 3 are completely ignored).

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the required total gimbal processing and total sensor processing for that observation job.

## Output

Print a single line containing the valid diagnostic code (`JOB i` or `LOAD c`).

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```

## Note

In Example 1, `JOB 1` is triggered because Conditions 1 and 2 require $G_1(t)$ to reach $70$ before $S_1(t)$ can begin increasing from $0$. By Condition 3 (applied to job 1 alone), $G_1(t)$ can increase by at most $t_b - t_a$ over any interval, meaning it cannot reach $70$ before time $t=70$. Thus, $S_1(t)$ must remain $0$ for at least the first $70$ units of time. By Condition 4, $S_1(t)$ can increase by at most $100 - 70 = 30$ over the remainder of the window. This makes it impossible for $S_1(100)$ to reach the required $60$ (Condition 1).

In Example 2, `LOAD 1` is triggered because Condition 1 requires $G_k(150) - G_k(0) = 50$ for all four jobs. Summing this over all jobs yields a total required gimbal processing of $200$. However, Condition 3 requires that the sum of increases across all jobs over the interval $[0, 150]$ cannot exceed $150 - 0 = 150$. This contradiction makes it mathematically impossible to satisfy Conditions 1 and 3 simultaneously for the set of all jobs.