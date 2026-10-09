# Problem A — System Diagnostic Resolution

Time limit: 2 s   Memory limit: 256 MB

## Description

A facility's diagnostic panel receives input from $n$ distinct data channels. Each channel operates strictly in one of two modes: ACTIVE or INACTIVE. The panel is wired with $m$ independent system checks. A check is a physical circuit that evaluates exactly three specific signal conditions. A condition specifies a channel and a target mode (ACTIVE or INACTIVE). A check passes its evaluation if at least one of its three conditions matches the actual mode of the corresponding channel. Conversely, if all three conditions contradict the actual modes of their respective channels, the check fails. Conditions can evaluate the same channel across different checks, often specifying different target modes.

Your task is to determine whether it is possible to assign a steady ACTIVE or INACTIVE mode to every one of the $n$ channels such that every system check passes. If such a configuration exists, you must provide it. If no combination of channel modes can satisfy all checks simultaneously, you must report that the system cannot be stabilized.

## Input
The first line contains two integers $n$ and $m$ (1 ≤ $n$ ≤ 90, 0 ≤ $m$ ≤ 400).
Each of the next $m$ lines contains three non-zero integers $l_1$, $l_2$, and $l_3$. The absolute value $|l_i|$ represents the channel index (1 to $n$). A positive value indicates the target mode for that condition is ACTIVE, while a negative value indicates the target mode is INACTIVE. At least one of the three stated conditions must hold for each check to pass.

## Output
If no configuration can satisfy all checks, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1 \ s_2 \ \dots \ s_n$ (each either `0` or `1`), where $s_i = 1$ if channel $i$ is assigned the ACTIVE mode, and $s_i = 0$ if it is assigned the INACTIVE mode. Any configuration that satisfies all checks is accepted.

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
Each check has exactly three entries. The same channel index may appear more than once in a single check.
