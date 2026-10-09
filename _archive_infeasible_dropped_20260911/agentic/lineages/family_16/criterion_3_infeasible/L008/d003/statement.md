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
- `JOB i` (where **i** is the 1-based job index). This asserts that if all other observation jobs were canceled, the strict ordering of Subsystem 1 and Subsystem 2 for job **i** alone still forces its completion to occur strictly after $t=\mathbf{T}$.
- `LOAD c` (where **c** is 1 or 2). This asserts that if the strict ordering between Subsystem 1 and Subsystem 2 were removed, the non-overlapping hardware restriction on Subsystem **c** alone still forces its operations to conclude strictly after $t=\mathbf{T}$.

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

In Example 1, `JOB 1` is valid because even if observation 1 is the only job processed, its Subsystem 1 phase requires 70 milliseconds, and its strictly subsequent Subsystem 2 phase requires 60 milliseconds. The minimum required time is 130 milliseconds, which forces completion strictly after the window of 100.

In Example 2, `LOAD 1` is valid because even if the ordering between subsystems is ignored, Subsystem 1 must process four non-overlapping blocks of 50 milliseconds each. This requires 200 milliseconds of dedicated uptime, forcing completion strictly after the window of 150.