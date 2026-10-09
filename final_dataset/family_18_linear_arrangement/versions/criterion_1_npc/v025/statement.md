# Orbital Constellation Power Budget

Time limit: 5 s
Memory limit: 256 MB

## Description
A constellation of $n$ observation satellites is being deployed into a single linear orbital array. The array contains exactly $n$ equally spaced orbital slots, numbered sequentially from 1 to $n$. Each satellite (identified by a unique manufacturing ID from 1 to $n$) must be assigned to exactly one orbital slot, such that every slot contains exactly one satellite.

The satellites must maintain continuous laser communication links with specific partners. The power required to maintain a link between two satellites depends entirely on the difference between their assigned slot numbers. Specifically, if a satellite is placed in slot $p_i$ and its partner is in slot $p_j$, the link consumes exactly $|p_i - p_j|$ megawatts of power. 

The constellation has a fixed total power budget of $B$ megawatts for all active links combined. You are given the list of $m$ required laser links. 

To ensure orbital stability, the engineering team has verified two constellation properties:
1. For every required link between satellite $u$ and satellite $v$, the absolute difference between their manufacturing IDs satisfies $|u - v| < n$.
2. The sum of the manufacturing IDs of any two linked satellites is strictly greater than 1 ($u + v > 1$).

These stability guarantees are mathematically assured for this deployment and may be utilized to optimize your assignment strategy.

Determine if there exists a valid assignment of satellites to orbital slots such that the sum of the power consumed by all required links is at most $B$. If such an assignment exists, provide the slot assignments. Otherwise, report that it is impossible.

## Input
The first line contains three integers $n$, $m$, and $B$ — the number of satellites (and slots), the number of required laser links, and the total power budget.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that a laser link must be maintained between the satellite with ID $u$ and the satellite with ID $v$.

## Output
If a valid assignment exists, print `YES` on the first line. On the second line, print $n$ integers, where the $i$-th integer is the slot number (from 1 to $n$) assigned to the satellite with ID $i$. The $n$ integers must be a permutation of 1 to $n$. The total power of all links under this assignment must be $\le B$.
If no such assignment is possible, print `NO`.

## Example 1

### Input
```
3 2 2
1 2
2 3
```

### Output
```
YES
1 2 3
```
