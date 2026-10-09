# Problem B — Telemetry Bridge Initialization

Time limit: 2 s
Memory limit: 256 MB

## Description
The telemetry bridge initialization requires finalizing a configuration by selecting from $2^t$ possible combinations of links.

You are given a universe of $2q$ distinct communication nodes, assigned integer IDs from $1$ to $2q$. The diagnostic scanner has generated a collection of $t$ viable transmission pairs. Each pair contains exactly two nodes. 

Your task is to evaluate the $2^t$ possible subsets of these pairs to find a valid core allocation. A subset is valid if and only if it satisfies $2q$ exact-occurrence constraints: every single node from $1$ to $2q$ must appear in exactly one pair within your chosen subset. If any node appears zero times, or more than once, the entire subset is invalid. If a valid configuration exists, you must output it. If no valid subset exists, the system must abort.

For hardware compliance, nodes $1$ through $q$ are designated as ground arrays, and nodes $q+1$ through $2q$ are designated as orbital relays. The scanner guarantees that every viable pair consists of exactly one ground array and exactly one orbital relay.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing half the total number of nodes and the number of viable pairs.
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a pair containing node $a$ and node $b$.

## Output
If a valid subset of pairs can be found, print `YES` on the first line, followed by $q$ lines each containing the two nodes of a selected pair. If no such subset exists, print `NO`.

## Example

**Input**
```
3 4
1 4
2 5
2 6
3 6
```

**Output**
```
YES
1 4
2 5
3 6
```
