# Redundant Sensor Calibration

Time limit: 2 s   Memory limit: 256 MB

## Description

An array of $n$ sensors must be calibrated. Each sensor $i$ (from 1 to $n$) can be placed in exactly one of two modes: Active (1) or Standby (0).

The system's health is tracked by $m$ diagnostic routines. To ensure robust fault tolerance, each routine is designed with triple redundancy: it monitors exactly three specific sensor states. A state condition is represented by a non-zero integer $x$: if $x > 0$, it requires sensor $x$ to be Active (1); if $x < 0$, it requires sensor $|x|$ to be Standby (0). A routine is considered "healthy" if at least one of the three sensor states it monitors is currently engaged. 

Because every routine offers three independent pathways to success, the system is designed to be highly flexible. A routine only fails if all three of its fallback conditions are simultaneously violated. Given this generous 3-to-1 redundancy ratio, one might expect that a simple greedy strategy—such as tallying the most requested mode for each sensor, or iteratively relaxing conflicting routines—would easily yield a globally healthy state. However, a heuristic is not enough: your task is to definitively determine whether there exists a single global calibration for all $n$ sensors that leaves every single diagnostic routine healthy at the same time. If such a calibration exists, you must provide it.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$).
Each of the next $m$ lines contains three non-zero integers $l_1, l_2, l_3$ ($|l_i| \le n$). These represent the three sensor states monitored by that diagnostic routine. At least one of the three stated conditions must hold for the routine to be healthy.

## Output
If no valid calibration exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$), where $s_i$ is the mode of sensor $i$. Any valid calibration is accepted.

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
Each diagnostic routine has exactly three entries. The same sensor index may appear more than once in a routine.
