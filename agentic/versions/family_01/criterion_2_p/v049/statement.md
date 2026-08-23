# Clockwork Configuration

Time limit: 1 s
Memory limit: 256 MB

A complex clockwork mechanism is built from $n$ primary rotating components, indexed from 1 to $n$. The architecture incorporates $m$ rigid contact points. Each contact point dictates the interaction between a specific pair of rotating components. Because of how the teeth mesh at these contact points, any two components sharing a contact point cannot share the same rotation state. 

Every component must be assigned exactly one rotation state, designated as either state 1 or state 2.

Given this layout, your objective is to evaluate whether a completely valid assignment of rotation states exists for the entire mechanism without any conflicts. If there are several ways to assign the states, you must find the specific assignment that yields the lexicographically smallest sequence of states when listed from component 1 to $n$.

## Input
The first line of the input contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of components and the number of contact points.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — the indices of a pair of components that share a contact point.

## Output
If it is impossible to assign states to all components without violating the contact point rules, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $s_1, \dots, s_n$ (where each $s_i \in \{1, 2\}$) representing the lexicographically smallest valid sequence of rotation states.

## Example 1
**Input:**
```
4 4
1 2
2 3
3 4
1 4
```
**Output:**
```
YES
1 2 1 2
```

## Example 2
**Input:**
```
3 3
1 2
1 3
2 3
```
**Output:**
```
NO
```
