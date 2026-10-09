# Deep-Sea Observatory Deployment

Time limit: 5 s   Memory limit: 256 MB

## Description
A deep-sea observatory is deploying $n$ sensor modules into a vertical shaft. The shaft contains $n$ distinct docking slots, spaced equally and numbered 1 to $n$ from top to bottom. Each module must be assigned to exactly one distinct slot.

The modules must share information through a network of $m$ point-to-point data relays. The network is designed so that a message can be routed between any pair of modules, but removing any single relay would break this full communication.

A dedicated fiber-optic cord is required for each relay between two modules. If a module is placed in slot $x$ and another in slot $y$, the cord connecting them must be exactly $|x - y|$ units long.

The deployment team has a strict budget on the total amount of fiber-optic cord they can use. The sum of the lengths of all $m$ cords must not exceed the maximum allowed total length $B$.

Determine if there is an assignment of modules to slots that keeps the total cord length within this budget.

## Input
The first line contains three integers $n$, $m$, and $B$, representing the number of modules, the number of relays, and the total cord length limit.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating a relay between module $u$ and module $v$. The relays form the minimal fully-communicating network described above (thus $m = n - 1$).

## Output
If the modules can be assigned to the slots such that the total cord length is at most $B$, print `YES` on the first line. On the second line, print $n$ integers, where the $i$-th integer is the slot (from 1 to $n$) assigned to module $i$. If there are multiple valid assignments, any one is acceptable.
If no such assignment exists, print `NO`.

## Example

**Input:**
```text
5 4 6
1 2
1 3
3 4
3 5
```

**Output:**
```text
YES
3 2 4 1 5
```
