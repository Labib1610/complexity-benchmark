# Phase 2: Configuration Synthesis

Time limit: 2 s   Memory limit: 256 MB

## Description

The automated maintenance cycle of an orbital array operates in three distinct phases.

**Phase 1: Data Aggregation**
The telemetry firmware scans $n$ hardware sensors and compiles a list of $m$ redundancy templates based on current thermal readings. This phase is fully automated and provides the raw data for the next step.

**Phase 2: Configuration Synthesis (Your Task)**
You must process the templates generated in Phase 1. Each sensor $i$ (from $1$ to $n$) must be assigned exactly one operating mode: `1` (primary) or `0` (auxiliary). Every template consists of three fallback parameters, represented by non-zero integers. A parameter $x > 0$ indicates a requirement that sensor $x$ be placed in primary mode (`1`). A parameter $x < 0$ indicates a requirement that sensor $|x|$ be placed in auxiliary mode (`0`). 

For a template to be considered stable, the assigned configuration must fulfill at least one of its three parameters. Your objective is to determine if there exists a single global configuration for all $n$ sensors that stabilizes all $m$ templates simultaneously.

**Phase 3: Hardware Flashing**
The deployment engine reads the output from Phase 2. If a valid configuration is provided, it flashes the sensors and resumes operation. If no such configuration is possible, it triggers an emergency shutdown. Your program is solely responsible for executing Phase 2.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$).
The following $m$ lines each contain three non-zero integers $p_1, p_2, p_3$ ($|p_i| \le n$), representing the three parameters of a redundancy template. 

## Output
If the templates cannot all be stabilized simultaneously, output a single line with `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers $c_1, c_2, \dots, c_n$ (each either `0` or `1`), where $c_i$ is the mode assigned to sensor $i$. If multiple valid configurations exist, any of them is acceptable.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```

## Note
Each redundancy template contains exactly three parameters. The same sensor index may be repeated within a single template.
