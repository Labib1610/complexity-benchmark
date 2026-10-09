# Problem C — Telemetry Window: Diagnostic Code

Time limit: 2 s   Memory limit: 256 MB

## Description

An orbital satellite is scheduled to execute **j** observation jobs within a mission window of duration **T**. 

A schedule assigns a gimbal start time $G_k$ and a sensor start time $S_k$ to each job $k \in \{1 \dots \mathbf{j}\}$. All start times must be real numbers. A schedule is considered valid only if it simultaneously satisfies all of the following rules:

- **Rule A (Window Limits):** Every phase must execute entirely within the mission window. For all $k$, $0 \le G_k$ and $G_k + \mathbf{p1}_k \le \mathbf{T}$, and $0 \le S_k$ and $S_k + \mathbf{p2}_k \le \mathbf{T}$.
- **Rule B (Intra-job Dependency):** For each job $k$, its sensor phase must not begin until its gimbal phase has completed. That is, $G_k + \mathbf{p1}_k \le S_k$.
- **Rule C (Gimbal Exclusivity):** The gimbal subsystem can only process one job at a time. For any two distinct jobs $k$ and $m$, their gimbal phases must not overlap (i.e., either $G_k + \mathbf{p1}_k \le G_m$ or $G_m + \mathbf{p1}_m \le G_k$).
- **Rule D (Sensor Exclusivity):** The sensor subsystem can only process one job at a time. For any two distinct jobs $k$ and $m$, their sensor phases must not overlap (i.e., either $S_k + \mathbf{p2}_k \le S_m$ or $S_m + \mathbf{p2}_m \le S_k$).

Mission control has determined that no schedule can satisfy all four rules simultaneously. You must output a diagnostic code that identifies the isolated source of the failure. 

The telemetry data is guaranteed to trigger exactly one of the following isolated contradictions. Print the corresponding code:
- `JOB i` (where **i** is the 1-based job index): Rules A and B cannot be satisfied simultaneously for job **i**, even if all other jobs are completely ignored.
- `LOAD 1`: Rules A and C cannot be satisfied simultaneously for the full set of **j** jobs, even if Rules B and D are completely ignored.
- `LOAD 2`: Rules A and D cannot be satisfied simultaneously for the full set of **j** jobs, even if Rules B and C are completely ignored.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the duration of the gimbal block and the duration of the sensor block for that observation job.

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

In Example 1, `JOB 1` is valid because for job 1, Rule A requires $G_1 \ge 0$ and $S_1 + 60 \le 100$ (which implies $S_1 \le 40$). However, Rule B requires $G_1 + 70 \le S_1$. Combining these gives $70 \le G_1 + 70 \le S_1 \le 40$, which is a mathematical contradiction. Thus, Rules A and B cannot be satisfied simultaneously for job 1.

In Example 2, `LOAD 1` is valid because Rule A requires all four gimbal phases to operate within the 150-millisecond window. Rule C requires them to not overlap. Four non-overlapping blocks of 50 milliseconds each require at least 200 milliseconds of total space, which contradicts the window size of 150. Thus, Rules A and C cannot be satisfied simultaneously for the set of all jobs.