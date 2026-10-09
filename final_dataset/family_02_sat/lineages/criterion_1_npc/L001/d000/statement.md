# Problem A — Beam Alignment Calibration

Time limit: 2 s   Memory limit: 256 MB

## Description

A high-energy particle accelerator contains $n$ magnetic lenses along its primary ring. During calibration, the control system must lock each lens into exactly one of two operational modes: focusing (represented by 1) or defocusing (represented by 0). There are no intermediate states.

To verify the integrity of the magnetic field, the system fires $m$ diagnostic laser paths across the ring. A single diagnostic path interacts with three specific lens conditions. A condition is defined by a lens index and a required mode (either focusing or defocusing). For a diagnostic path to remain stable and register on the sensors, at least one of its three conditions must be satisfied. If all three conditions are violated, the path destabilizes, triggering a calibration failure.

You are given the stability requirements for all $m$ diagnostic paths. Determine whether there is a single global configuration for all $n$ lenses that keeps every diagnostic path stable simultaneously.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$), representing the number of magnetic lenses and diagnostic paths, respectively.

Each of the following $m$ lines contains three non-zero integers $l_1, l_2, l_3$ ($|l_i| \le n$) describing the conditions for one diagnostic path. The absolute value $|l_i|$ indicates the lens index. A positive value means the condition requires lens $|l_i|$ to be focusing (1). A negative value means the condition requires lens $|l_i|$ to be defocusing (0). A path is stable if at least one of the three conditions is met.

## Output
If no valid configuration exists that stabilizes all paths, print a single line NO.
Otherwise, print YES on the first line. On the second line, print $n$ integers $s_1 \ s_2 \ \dots \ s_n$ (each either 0 or 1), where $s_i$ is the mode assigned to lens $i$. Any valid configuration is accepted.

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
Every diagnostic path lists exactly three conditions. The same lens index may appear more than once within the same path's requirements.
