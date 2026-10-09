# Problem A — Regulatory Compliance in Sovereign Networks

Time limit: 5 s   Memory limit: 256 MB

## Description
A global enterprise operates a communications network of $n$ data centers, linked by $m$ bidirectional fiber connections. Each connection carries a specific termination penalty, representing the financial cost to permanently disable it.

A specific subset of $k$ data centers are classified as sovereign entities. Under strict new regulatory frameworks, no two sovereign entities are permitted to have a functional communication route between them. A route exists if data can travel between two data centers via any sequence of active connections.

Your task is to select a subset of connections to terminate so that no sovereign entity can transmit data to any other sovereign entity. Once terminated, a connection carries no information in either direction. The remaining data centers (non-sovereign) have no routing restrictions and may be grouped in any configuration, provided the primary rule regarding sovereign entities is strictly upheld. The objective is evaluated solely on the total termination penalty, calculated as the sum of the penalties of the disabled connections.

A corporate budget $B$ has been allocated for this process. You must find a set of connections to terminate whose total penalty is at most $B$ and which fulfills the regulatory requirements, or state that it is impossible within the budget.

Furthermore, your solution must satisfy the following administrative limits:
- You are strictly prohibited from terminating more than $m$ connections.
- No individual connection may be selected for termination more than once.

## Input
Line 1: four integers n, m, k, B.
Line 2: k distinct integers representing the identifiers of the sovereign data centers.
Next m lines: three integers u v w per line, representing a connection between data center u and data center v with a termination penalty of w.

## Output
If a valid termination plan exists within the budget, output `YES` on the first line. On the second line, output the number of terminated connections, denoted as c. Following this, output c lines, each containing two integers u v representing a terminated connection.
If no such plan exists within the budget, output `NO`.

## Example
**Input**
```
5 5 3 10
1 3 5
1 2 4
2 3 5
3 4 2
4 5 6
1 5 3
```

**Output**
```
YES
3
1 2
3 4
1 5
```
