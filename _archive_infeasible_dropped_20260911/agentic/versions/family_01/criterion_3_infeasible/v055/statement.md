# Problem C — Protocol Diagnostic

Time limit: 2 s   Memory limit: 256 MB

You are evaluating a communication network consisting of $n$ celestial bodies, identified by integers from 1 to $n$. The network contains $m$ bidirectional data links, each connecting a specific pair of bodies.

The ultimate goal for this network is to assign each body to one of two operating frequencies such that no two bodies connected by a data link share the same frequency. 

Before any assignment can be attempted, your task is to identify a structural block that would interfere with the frequencies. You must find exactly three distinct bodies, denoted as $a$, $b$, and $c$, where $a < b < c$, that satisfy all of the following topological conditions simultaneously:
1. A data link connects body $a$ and body $b$.
2. A data link connects body $b$ and body $c$.
3. A data link connects body $a$ and body $c$.

If there are multiple sets of three bodies that meet these conditions, you must report the one that is lexicographically first (i.e., minimizing $a$; in case of a tie, minimizing $b$; and then minimizing $c$).

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1) / 2, 2 \cdot 10^5)$).
Each of the following $m$ lines contains two integers $u$ and $v$ — a pair of celestial bodies connected by a data link. 
It is guaranteed that the network contains at least one set of three bodies satisfying all the conditions for a structural block.

## Output
Print three integers $a$ $b$ $c$ on one line with $a < b < c$ representing the lexicographically first structural block.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
