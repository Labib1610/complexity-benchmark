# Problem C — Telemetry Window: Diagnostic Code

Time limit: 2 s   Memory limit: 256 MB

## Description

An orbital satellite is scheduled to execute **j** observation jobs before the mission window closes at $t = \mathbf{T}$ milliseconds.

Each observation job consists of two strictly ordered phases:
1. The targeting gimbal (Subsystem 1) must be dedicated to the job for a continuous block of **p1** milliseconds.
2. Only after this gimbal block has fully concluded, the imaging sensor (Subsystem 2) must be dedicated to the job for a continuous block of **p2** milliseconds.

The hardware dictates that the gimbal's blocks cannot overlap with each other, and the sensor's blocks cannot overlap with each other.

Mission control has determined that no valid schedule exists that finishes all phases by $t = \mathbf{T}$. You must output a diagnostic code that demonstrates a fundamental timeline violation.

The diagnostic code must be one of the following:
- `JOB i` (where **i** is the 1-based job index). This asserts that the earliest possible conclusion time for observation **i**'s final phase, assuming its initial phase begins at $t=0$ and experiences no delays, strictly exceeds $\mathbf{T}$.
- `LOAD c` (where **c** is 1 or 2). This asserts that the cumulative active footprint required by Subsystem **c** across the entire mission, if placed contiguously from $t=0$, would conclude strictly after $t=\mathbf{T}$.

The telemetry data is guaranteed to trigger exactly one of these fundamental timeline violations. Print the corresponding code.

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

In Example 1, `JOB 1` is valid because starting observation 1's initial phase at $t=0$ means it concludes at $t=70$. The final phase immediately follows and concludes at $t=130$, which strictly exceeds $100$.

In Example 2, `LOAD 1` is valid because placing the four gimbal blocks contiguously requires an active footprint of 200 milliseconds. Starting at $t=0$, this concludes at $t=200$, which strictly exceeds $150$.