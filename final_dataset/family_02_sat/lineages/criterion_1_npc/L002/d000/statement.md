# Problem A — Litho-Print Pipeline Configuration

Time limit: 2 s   Memory limit: 256 MB

## Description

The Litho-Print V system relies on a three-stage automated pipeline to manufacture smart materials. You are responsible for programming the central stage, which bridges raw sensor data with the physical actuation hardware.

**Stage 1: Topography Scan (Upstream)**
The raw substrate is placed in the chamber. The optical scanner identifies $n$ independent calibration nodes across the material. To prevent thermal fracturing during printing, the scanner also generates $m$ stress-relief templates based on the substrate's geometry. This data is passed directly to your module.

**Stage 2: Phase Resolution (Your Task)**
You must configure the global state of the calibration nodes before the lasers can fire. Every node must be strictly assigned to either Phase 0 or Phase 1. 

Each of the $m$ stress-relief templates contains exactly three trigger conditions. A template is safely resolved if **at least one** of its three trigger conditions becomes active under your chosen phase assignment. A single trigger condition is represented by a non-zero integer $k$:
- If $k > 0$, the condition is active if node $k$ is assigned to Phase 1.
- If $k < 0$, the condition is active if node $|k|$ is assigned to Phase 0.

You must find a single global assignment of phases to all $n$ nodes such that every single template is safely resolved simultaneously.

**Stage 3: Beam Actuation (Downstream)**
The physical emitters lock into your chosen phases and the printing beam is engaged. If you provide a valid configuration, the print succeeds. If your configuration leaves even one template unresolved, the material fractures. If the upstream data contains conflicting requirements such that no valid phase assignment exists, your module must abort the pipeline.

## Input
The first line of input provides two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$), representing the number of calibration nodes and the number of stress-relief templates from Stage 1.
Each of the next $m$ lines contains three non-zero integers $l_1, l_2, l_3$ ($|l_i| \le n$), representing the three trigger conditions for that template.

## Output
If the pipeline must be aborted because no valid phase assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each either 0 or 1), where $s_i$ is the phase assigned to node $i$. If multiple valid assignments exist, any of them will be accepted by Stage 3.

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
Each template provides exactly three trigger conditions. The same calibration node may be referenced multiple times within the same template.
