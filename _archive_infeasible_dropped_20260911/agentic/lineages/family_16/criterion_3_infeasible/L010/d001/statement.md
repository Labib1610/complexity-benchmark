# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A software firm is rolling out an update comprising **j** independent components. The rollout involves two stages: compilation on a dedicated build machine (Stage 1), followed by validation on a dedicated testing machine (Stage 2). A machine handles exactly one component at a time. A component is eligible for the testing machine only when its compilation has completely finished.

The firm has allocated a strict release window of exactly **T** minutes. All components must be fully validated before this window closes.

Every provided scenario represents an impossible timeline—there is no valid scheduling order that can complete all components within the release window. Instead of scheduling, your task is to identify a bottleneck that proves the timeline is unachievable, providing a short certificate the system can verify.

Exactly one of the following bottlenecks will always be present. Output the applicable certificate:

- **Component Delay.** Suppose a component is given absolute priority: it starts on the build machine at minute 0 and moves to the testing machine the exact moment its compilation finishes. If its validation would still remain unfinished when the release window closes at minute **T**, the overall timeline is doomed. Output `JOB i`, where **i** is the 1-based index of the component.
- **Machine Saturation.** Suppose a machine is kept busy continuously from minute 0, with no idle gaps between components. If it would still be running its required tasks after the release window closes at minute **T**, the overall timeline is doomed. Output `LOAD c`, where **c** is 1 for the build machine or 2 for the testing machine, and the machine's required active time exceeds the window.

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

In Example 1, even if component 1 is prioritized, its compilation and validation take 70 and 60 minutes respectively. Its earliest possible completion is at minute 130, which is past the 100-minute window, making `JOB 1` the correct proof of impossibility. In Example 2, no single component exceeds 150 minutes when prioritized, but the build machine requires 50+50+50+50 = 200 minutes of continuous operation to finish its tasks. Since this extends past the 150-minute window, `LOAD 1` is the correct output.