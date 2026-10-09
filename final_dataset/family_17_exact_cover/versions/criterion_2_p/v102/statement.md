# Problem B — Combinatorial Protocol Selection

Time limit: 2 s   Memory limit: 256 MB

## Description
A complex communication protocol requires configuring a system of $2q$ independent modules. You are provided with a dictionary of $t$ compatible module pairs.

Your objective is to find a valid subset of these pairs to activate. To satisfy the protocol's strict assignment rules, every single module in the system (all $2q$ of them) must appear in exactly one activated pair. Leaving a module unassigned is a critical failure, as is assigning a module to multiple pairs. 

With $t$ reaching up to 400,000, the number of possible subsets is astronomically large. You must determine whether at least one valid configuration exists within this vast space of combinations. 

The modules have predefined roles: IDs $1$ through $q$ act as initiators, while IDs $q+1$ through $2q$ act as responders. Every pair in the provided dictionary exclusively links one initiator to one responder.

If a valid configuration of the modules can be formed, you must output it. Otherwise, report that it is impossible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100,000$, $0 \le t \le 400,000$), representing the number of initiators (which is also the number of responders) and the total number of compatible module pairs.
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), specifying a compatible pair comprising initiator $a$ and responder $b$.

## Output
If it is possible to satisfy the assignment requirements, print `YES` on the first line. Then, print $q$ lines, each containing the two module IDs of an activated pair. If no valid subset exists, print `NO`.

## Example

**Input**
```text
3 4
1 4
1 5
2 5
3 6
```

**Output**
```text
YES
1 4
2 5
3 6
```
