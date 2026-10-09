# Problem B — Interlock Configuration

Time limit: 1 s
Memory limit: 256 MB

## Description
An industrial facility relies on $n$ independent fluid routing nodes. Each node must be configured into exactly one of two operational states, denoted as state 1 and state 0.

The facility's safety system consists of $m$ mechanical interlocks. Each interlock is wired to exactly two specific node-states. A node-state is defined as a particular node operating in a particular state (for example, "node 4 in state 1" or "node 7 in state 0").

The internal mechanism of an interlock ensures that it remains stable as long as at least one of its two wired node-states is active. Consequently, if a given configuration causes one of the wired node-states to be inactive, the interlock strictly mandates that the other wired node-state must be active to prevent a system halt.

Determine if there is a global configuration for all $n$ nodes that stabilizes all $m$ interlocks simultaneously. If such a configuration is possible, provide one. Otherwise, report that no valid configuration exists.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).

Each of the following $m$ lines describes an interlock using two non-zero integers $l_1$ and $l_2$ ($|l_i| \le n$). An integer $l$ represents a node-state: its absolute value $|l|$ specifies the node index (from $1$ to $n$), and its sign specifies the required state. A positive integer requires the node to be in state 1, while a negative integer requires the node to be in state 0.

For each interlock, at least one of the two represented node-states must be active in a valid configuration.

## Output
If no valid configuration exists, print `NO` on a single line.

Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ separated by spaces, where each $s_i \in \{0, 1\}$ represents the state of the $i$-th node. If multiple valid configurations exist, you may output any of them.

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
