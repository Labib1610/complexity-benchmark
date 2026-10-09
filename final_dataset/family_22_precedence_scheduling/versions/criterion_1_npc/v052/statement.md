# Problem A — Assembly Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description
A production plant has to execute a set of operations. The plant floor contains identical workstations. The plant operates in discrete time blocks called shifts. Each workstation can perform at most one operation per shift. Every operation requires exactly one full shift. Consequently, if there are $M$ workstations, at most $M$ operations can be conducted during any given shift.

Operations are linked by material flow. You are given a set of transfer requirements, each specified as a pair of operations $(a, b)$. This indicates that the physical output of operation $a$ is a necessary input for operation $b$. Since materials can only be relocated between shifts, operation $b$ must take place in a shift that occurs strictly later than the shift assigned to operation $a$. 

The facility must complete the entire set of operations within a strict limit of $T$ shifts. Your task is to assign every operation to a shift number such that no shift is assigned more operations than there are workstations, and all transfer requirements are satisfied. If no such assignment is possible, you must report the failure.

## Input
The first line provides four integers $n$, $M$, $T$, and $m$. 
- $n$: the number of operations (numbered $1$ through $n$).
- $M$: the number of workstations available per shift.
- $T$: the maximum number of shifts allowed.
- $m$: the number of transfer requirements.

The next $m$ lines each contain two integers $a$ and $b$ ($1 \le a, b \le n$), representing a transfer requirement where operation $a$ must be assigned to an earlier shift than operation $b$.

## Output
If a valid assignment exists, output `YES` on the first line, followed by a second line containing $n$ space-separated integers. The $i$-th integer must be the shift number assigned to operation $i$ (an integer from $1$ to $T$).
If no such assignment is possible, output `NO`.

## Example

### Input
```
5 2 3 4
1 3
2 3
3 4
3 5
```

### Output
```
YES
1 1 2 3 3
```
