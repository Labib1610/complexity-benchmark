# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A software firm is rolling out an update comprising **j** independent components. The rollout involves two stages: compilation on a dedicated build machine (Stage 1), followed by validation on a dedicated testing machine (Stage 2). A machine handles exactly one component at a time. A component is eligible for the testing machine only when its compilation has completely finished.

The firm has allocated a strict release window of exactly **T** minutes. All components must be fully validated before this window closes at minute **T**.

Every provided scenario represents an impossible timeline—there is no valid scheduling order that can complete all components within the release window. Instead of scheduling, your task is to identify a bottleneck that proves the timeline is unachievable, providing a short certificate the system can verify.

Exactly one of the following bottlenecks will always be present. Output the applicable certificate:

- **Component Delay.** A valid schedule requires a component's compilation and validation phases to be executed as two sequential intervals within the release window. If it is mathematically impossible to fit these two sequential intervals for a specific component inside the window [0, **T**] with lengths equal to its required compilation and validation durations, output `JOB i`, where **i** is the 1-based index of the component.
- **Machine Saturation.** A valid schedule requires a machine to execute its phase for all components using non-overlapping intervals within the release window. If it is mathematically impossible to place one non-overlapping interval per component on machine **c** inside the window [0, **T**] such that each interval's length equals the component's required duration for that machine, output `LOAD c`, where **c** is 1 for the build machine or 2 for the testing machine.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the compilation duration and validation duration of a component.

## Output

Print a single line: `JOB i` (for a component bottleneck) or `LOAD c` (for a machine bottleneck).

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

In Example 1, for component 1, its compilation and validation take 70 and 60 minutes respectively. It is impossible to fit two sequential intervals of lengths 70 and 60 within the 100-minute window, making `JOB 1` the correct proof of impossibility. In Example 2, no single component requires sequential intervals exceeding 150 minutes in total, but the build machine requires intervals of lengths 50, 50, 50, and 50. It is impossible to place these four non-overlapping intervals inside the 150-minute window. Thus `LOAD 1` is the correct output.