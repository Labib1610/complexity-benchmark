# Rejection Certificate: Shift Quota

Time limit: 2 s   Memory limit: 256 MB

## Description

A planetary customs authority processes a queue of commercial transports (historically designated in the system as "jobs"). Each transport must first undergo a biological scan at Facility 1, and immediately upon clearance, a cargo inspection at Facility 2. A single facility can only handle one transport at a time. A transport cannot begin Facility 2's inspection until its Facility 1 scan is complete.

The authority is mandated to clear the entire queue within a continuous operational window of $T$ seconds. 

However, the schedules submitted to this system are always physically impossible to complete within the window, regardless of the processing order. Rather than attempting to find a schedule, your task is to generate a standardized rejection certificate that proves the queue cannot be cleared. The certificate must be verifiable by directly checking the submitted times.

For every input, it is guaranteed that exactly one of the following two failure states applies. Print the certificate for the one that holds:

- **Individual Transport Violation:** If a specific transport requires a combined time across both facilities that strictly exceeds $T$, it cannot be processed even if it were the only transport present.
  Print: `JOB i` — where $i$ (1-based) is the index of the violating transport.

- **Facility Bottleneck:** Since each facility processes transports sequentially, it requires an active time equal to the sum of its respective phase durations for all transports. If the total active time required for Facility 1 (or Facility 2) strictly exceeds $T$, the queue cannot be cleared.
  Print: `LOAD c` — where $c$ is the facility number (1 or 2) whose total required active time exceeds $T$.

## Input

The first line provides two integers: the number of transports $j$ and the window $T$. The database is provisioned with exactly two hundred thousand manifest slots, strictly capping the number of transports $j$ (which is at least one). The operational window $T$ is a strictly positive integer bounded by a system maximum of one billion seconds.

The subsequent $j$ lines detail the transports in order. Each line provides two integers: the duration required at Facility 1, followed by the duration required at Facility 2. Due to hardware safety limits, each phase duration is a strictly positive integer capped at one million seconds.

## Output

Print a single line: `JOB i` (if transport $i$'s combined duration exceeds $T$) or `LOAD c` (if facility $c$'s total load exceeds $T$).

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

In Example 1, transport 1 needs 70 + 60 = 130 > 100 seconds in sequence, so `JOB 1` proves the queue cannot be cleared. In Example 2, no single transport exceeds 150 seconds, but Facility 1 must process 50+50+50+50 = 200 > 150 seconds of work in total, so `LOAD 1` is the certificate.
