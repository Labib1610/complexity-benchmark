# Problem C — Telemetry Window: Diagnostic Code

Time limit: 2 s   Memory limit: 256 MB

## Description

An orbital satellite must process $j$ observation requests before it loses contact with the ground station in exactly $T$ milliseconds.

Processing each request requires two steps in a strict sequence:
1. The targeting gimbal (Hardware Module 1) rotates to the specified coordinates. This consumes $p1$ milliseconds.
2. The imaging sensor (Hardware Module 2) captures the data. This consumes $p2$ milliseconds.

The satellite's architecture imposes the following operational rules:
- Hardware Module 1 can only rotate for a single request at any given moment.
- Hardware Module 2 can only capture data for a single request at any given moment.
- Hardware Module 2 cannot begin its capture for a specific request until Hardware Module 1 has completely finished its rotation for that exact same request.
- **Minimum Cycle Threshold:** Every request requires a minimum of 2 milliseconds of combined hardware time to prevent sensor faults.
- **Synchronization Delta:** The absolute discrepancy between the rotation and capture durations for any single request is guaranteed to never exceed 999,999 milliseconds.

Mission control has already determined that the $j$ requests cannot possibly all be completed within the $T$ millisecond communication window, no matter what scheduling order is chosen. You do not need to find a schedule. Instead, you must report a diagnostic code that formally proves the window is insufficient. The certificate can be checked directly against the input.

Exactly one of the following diagnostic conditions always applies. Print the code for the one that holds:

- **Isolated Request Violation.** If a single request's total sequential processing time (rotation plus capture) is strictly greater than the communication window $T$, this request alone makes the schedule impossible.
  Print: `JOB i` — where $i$ (1-indexed) is the ID of such a request.

- **Module Saturation.** Because each hardware module processes requests one at a time, the sum of all active times for a single module cannot exceed the window $T$. If the sum of all rotation times exceeds $T$, or the sum of all capture times exceeds $T$, the schedule is impossible.
  Print: `LOAD c` — where $c$ is the ID of the hardware module (1 or 2) whose total required active time is strictly greater than $T$.

## Input

The first line provides the number of requests $j$ and the communication window $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
The subsequent $j$ lines each provide two integers $p1$ and $p2$ ($1 \le p1, p2 \le 1000000$): the rotation time (Module 1) and the capture time (Module 2) for that request.

## Output

Output a single line containing either `JOB i` (for a request whose sequential time exceeds $T$) or `LOAD c` (for a module $c$ whose total active time exceeds $T$).

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

In Example 1, request 1 takes 70 + 60 = 130 milliseconds sequentially. Since 130 > 100, `JOB 1` proves the failure.
In Example 2, no single request exceeds 150 milliseconds. However, Hardware Module 1 must be active for 50+50+50+50 = 200 milliseconds. Since 200 > 150, `LOAD 1` is the correct diagnostic code.
