# Phase II: Containment Synthesis

Time limit: 2 s   Memory limit: 256 MB

## Description
The startup sequence for a deep-space fusion reactor involves three distinct phases. In Phase I, the automated diagnostics probe the reactor's geometry and output a list of structural dependencies. In Phase II, the control software must process these dependencies to determine a valid polarity configuration for the reactor's primary field emitters. Finally, in Phase III, the hardware applies this configuration to ignite the plasma.

You are responsible for implementing the Phase II synthesis module.

The reactor contains $n$ field emitters. Each emitter must be locked into one of two discrete polarities: active (1) or dormant (0). 

The structural dependencies generated in Phase I consist of $m$ safety interlocks. To prevent a containment breach during Phase III, every single interlock must be satisfied. An interlock monitors exactly three specific emitter conditions. A condition specifies an emitter and its required polarity. An interlock is considered satisfied as long as at least one of its three monitored conditions matches the actual configuration of the emitters. If an interlock finds that all three of its conditions are violated by the configuration, the startup sequence will abort.

Given the list of interlocks from Phase I, determine if there is a global configuration for the $n$ emitters that satisfies all $m$ interlocks, allowing Phase III to proceed.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$), representing the number of field emitters and the number of safety interlocks, respectively.

Each of the following $m$ lines contains three non-zero integers $c_1, c_2, c_3$ ($|c_i| \le n$) representing the conditions for one interlock. The absolute value $|c_i|$ denotes the emitter index. A positive value indicates that the interlock requires emitter $|c_i|$ to have an active polarity (1). A negative value indicates that the interlock requires emitter $|c_i|$ to have a dormant polarity (0). An interlock is satisfied if at least one of its three conditions is met. The same emitter may be referenced multiple times within a single interlock.

## Output
If there is no valid configuration that satisfies all interlocks, print a single line containing NO.
Otherwise, print YES on the first line. On the second line, print $n$ integers $p_1 \ p_2 \ \dots \ p_n$ (each either 0 or 1), where $p_i$ is the polarity assigned to emitter $i$. If multiple valid configurations exist, any of them will be accepted for Phase III.

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
