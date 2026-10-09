# Problem A — Production Coordination

Time limit: 5 s   Memory limit: 256 MB

## Description

A manufacturing facility utilizes **m** workstations to fulfill **j** commissions. The company employs exactly 10 project managers and 10 workstation technicians. Each commission is overseen by a unique project manager, and at least one commission is always accepted. Each workstation requires exactly one dedicated technician, with at least one workstation always operational.

Each commission consists of a sequence of procedural steps. Every step requires a specific workstation and a certain number of minutes. The following operational rules apply:
- The steps of a commission must be executed in their provided sequence. A step can only commence once the preceding step for that same commission has fully concluded.
- A workstation can accommodate only one step at any given time.
- Once a step begins at a workstation, it must proceed without interruption until it is completely finished.

Every step across all commissions requires exactly one line in the daily logbook. The logbook has exactly 50 blank lines remaining, which strictly limits the total number of steps that can be scheduled. Furthermore, a step takes at least one minute. To prevent overheating, an automatic shutoff engages after 1000 minutes of continuous operation, effectively capping the maximum duration of any single step.

Your task is to coordinate all procedural steps to minimize the time at which the final step of the final commission finishes. Report this earliest possible completion time.

## Input

The first line contains two integers **j** and **m**.
Each of the next **j** lines describes one commission: an integer **o** (the number of procedural steps in this commission) followed by **o** pairs of integers `workstation duration`, listing the commission's steps in their required sequence. Workstations are numbered from 1 to **m**.

## Output

Print a single integer: the earliest possible time at which all commissions are completely finished.

## Examples

### Example 1

**Input**
```
2 3
3 1 2 2 2 3 2
3 1 2 2 2 3 2
```

**Output**
```
8
```

### Example 2

**Input**
```
1 3
3 1 5 2 3 3 2
```

**Output**
```
10
```

### Example 3

**Input**
```
2 3
1 1 4
1 2 3
```

**Output**
```
4
```

## Note

In Example 1, two identical commissions each pass through workstations 1, 2, and 3 (2 minutes each); the second commission trails the first through the pipeline and finishes at minute 8. In Example 3 the two commissions use different workstations and run in parallel, finishing at minute 4.
