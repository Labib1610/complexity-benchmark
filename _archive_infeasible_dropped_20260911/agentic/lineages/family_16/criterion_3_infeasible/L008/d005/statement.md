# Problem C — Telemetry Window: Diagnostic Code

Time limit: 2 s   Memory limit: 256 MB

## Description

An orbital satellite is scheduled to execute **j** observation jobs within a mission window of duration **T**. 

Each job $k \in \{1 \dots \mathbf{j}\}$ requires a continuous gimbal phase of duration $\mathbf{p1}_k$ and a continuous sensor phase of duration $\mathbf{p2}_k$. 

A valid schedule must assign a start time and an end time to every phase such that all of the following conditions are simultaneously satisfied:
1. **Window Limit:** Every phase of every job must execute entirely within the mission window, starting no earlier than time $0$ and ending no later than time $\mathbf{T}$.
2. **Intra-job Dependency:** For every job, its sensor phase cannot begin until its gimbal phase has completely finished.
3. **Gimbal Exclusivity:** The gimbal subsystem can process at most one job at a time. No two jobs' gimbal phases may overlap in time.
4. **Sensor Exclusivity:** The sensor subsystem can process at most one job at a time. No two jobs' sensor phases may overlap in time.

Mission control has determined that no schedule can satisfy all four conditions simultaneously. You must output a diagnostic code that identifies the isolated source of the failure. 

The telemetry data is guaranteed to trigger exactly one of the following isolated contradictions. Print the corresponding code:
- `JOB i` (where **i** is the 1-based job index): Conditions 1 and 2 cannot be satisfied simultaneously for job **i**, even if all other jobs and conditions are completely ignored. (If multiple jobs satisfy this, you may output the code for any such job).
- `LOAD 1`: Conditions 1 and 3 cannot be satisfied simultaneously for the full set of **j** jobs, even if conditions 2 and 4 are completely ignored.
- `LOAD 2`: Conditions 1 and 4 cannot be satisfied simultaneously for the full set of **j** jobs, even if conditions 2 and 3 are completely ignored.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the duration of the gimbal phase and the duration of the sensor phase for that observation job.

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

In Example 1, `JOB 1` is valid because for job 1, Condition 1 requires both phases to fit within the 100-unit window. Condition 2 requires the 60-unit sensor phase to strictly follow the 70-unit gimbal phase. Together, they require at least 130 units of total time, which contradicts the window size of 100. Thus, Conditions 1 and 2 cannot be satisfied simultaneously for job 1.

In Example 2, `LOAD 1` is valid because Condition 1 requires all four gimbal phases to operate within the 150-unit window. Condition 3 requires them to not overlap. Four non-overlapping blocks of 50 units each require at least 200 units of total space, which contradicts the window size of 150. Thus, Conditions 1 and 3 cannot be satisfied simultaneously for the set of all jobs.