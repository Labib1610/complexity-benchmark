# Problem A — Redundant System Commissioning

Time limit: 2 s
Memory limit: 256 MB

## Description

Engineers are configuring a control network consisting of $n$ independent modules. Prior to deployment, every module must be initialized into exactly one of two operating modes: primary (represented by 1) or standby (represented by 0). There is no neutral mode.

To guarantee safe operation, the network must pass a suite of $m$ fault-tolerance checks. The system is designed with heavy redundancy to make commissioning as flexible as possible: each check monitors exactly three specific module conditions. A check is considered successful provided that *at least one* of its three conditions evaluates to true. A check only fails in the worst-case scenario where all three of its monitored conditions are violated simultaneously.

While this three-fold redundancy offers numerous ways to satisfy any individual check, modules are interconnected and monitored by multiple checks simultaneously. A module might be requested to be in primary mode by a condition in one check, but requested to be in standby mode by a condition in another. 

Given the $m$ fault-tolerance checks and the $n$ modules, you must determine whether the system's redundancy is sufficient to allow a single, global configuration of all $n$ modules that passes every check. If such a configuration exists, output a valid mode assignment for each module. If the conflicting requirements overwhelm the redundancy and no such configuration is possible, report this.

## Input

The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$).
Each of the following $m$ lines describes a fault-tolerance check using three non-zero signed integers $l_1, l_2, l_3$, where $|l_i| \le n$. 
The absolute value $|l_i|$ indicates the module being monitored. A positive value means the condition is met if the module is in primary mode (1). A negative value means the condition is met if the module is in standby mode (0).

## Output

If no valid global configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each either 0 or 1), where $s_i$ is the mode assigned to module $i$. If multiple valid configurations exist, any of them will be accepted.

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

Every check monitors exactly three conditions. The same module index may be monitored multiple times within a single check.
