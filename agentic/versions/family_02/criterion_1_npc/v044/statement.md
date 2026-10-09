# Problem A — Build Configuration Check

Time limit: 2 s   Memory limit: 256 MB

## Description

A large-scale build system is governed by $n$ configuration toggles, each of which must be resolved to either an active (1) or inactive (0) state. The system is designed with high redundancy to ensure builds rarely fail: an integration run consists of $m$ independent subsystem checks. Each subsystem check specifies exactly three fallback options (toggles that should be active, or toggles that should be inactive). Because of this redundancy, a check passes as long as *at least one* of its three fallback options is correctly matched by the global configuration. The other two options are completely ignored.

Because each check provides three independent alternatives, one might expect to satisfy them by simply choosing the most common requirements. The configuration space appears highly forgiving, as many toggles can be set without breaking a check that is already satisfied by another toggle. Your task is to process the list of $m$ subsystem checks and determine if there is a single, consistent global configuration of the $n$ toggles that allows all $m$ checks to pass simultaneously.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$).
Each of the next $m$ lines describes a subsystem check using three non-zero integers $c_1, c_2, c_3$, where $|c_i| \le n$. A positive integer $x$ indicates a fallback option requiring toggle $x$ to be active. A negative integer $-x$ indicates a fallback option requiring toggle $x$ to be inactive.

## Output
If no valid configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each either 0 or 1), where $s_i$ is the state of toggle $i$ (1 for active, 0 for inactive). Any valid configuration is accepted.

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
Each check has exactly three options. The same toggle index may appear more than once in a single check.
