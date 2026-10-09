# Problem B — Pressure Regulation Network

Time limit: 1 s   Memory limit: 256 MB

## Description

A city's water distribution network contains $n$ control valves. To maintain continuous flow, each valve must be uniquely configured to draw from either the Primary reservoir (denoted by state 1) or the Secondary reservoir (denoted by state 0). 

Hydraulic engineers have evaluated the network and formulated $m$ pressure stability conditions. Each condition specifies exactly two acceptable valve configurations. To prevent pipe ruptures, the network must be set up such that every condition has at least one of its two specified configurations active. 

Because each stability condition links only a pair of configurations, a rejected configuration on one side immediately mandates the adoption of the other. The interactions between these conditions cascade through the network. Your task is to determine if there is a single, network-wide configuration of all $n$ valves that simultaneously fulfills all $m$ stability conditions.

## Input
The first line contains two integers $n$ and $m$. The number of valves $n$ is at least one and does not exceed the total number of seconds in 27 hours, 46 minutes, and 40 seconds. The number of stability conditions $m$ is non-negative and is at most double the maximum allowed number of valves.

Each of the following $m$ lines describes a stability condition using two non-zero integers $v_1$ and $v_2$. The absolute value of each integer corresponds to a valid valve identifier (from $1$ to $n$). 
- A positive integer $v$ indicates the configuration where valve $v$ draws from the Primary reservoir.
- A negative integer $v$ indicates the configuration where valve $|v|$ draws from the Secondary reservoir.

For each condition, at least one of the two configurations must be active in the final network setup.

## Output
If no valid global setup exists that fulfills all conditions, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (each either 0 or 1), representing a valid network setup. Here, $s_i = 1$ means valve $i$ is set to the Primary reservoir, and $s_i = 0$ means it is set to the Secondary reservoir. If multiple valid setups exist, you may output any of them.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid setups may exist; any one is accepted. The same valve identifier may appear in multiple stability conditions.
