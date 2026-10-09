# Shift Assignment Failure Report

Time limit: 2 s   Memory limit: 256 MB

The factory runs on a two-shift daily system. The HR department has compiled a list of pairs of workers who cannot be assigned to the same shift due to personal conflicts. It is already established that creating a valid shift roster is impossible under these conditions. 

To formally close the scheduling attempt, you must provide a specific failure justification. The HR records guarantee that there is at least one trio of workers where every individual in the trio has a documented conflict with the other two. Identifying such a trio serves as irrefutable proof that a two-shift system cannot work. You must identify one such trio.

## Input
The first line contains two integers $n$ and $m$, representing the number of workers and the number of conflict reports. The workforce size $n$ requires at least three individuals, and is capped by the factory's maximum fire-code capacity of two thousand personnel. The number of conflict reports $m$ is at least three, and is limited by either the total number of possible pairs among the current personnel or the database's strict storage limit of two hundred thousand entries, whichever is smaller.

Each of the subsequent $m$ lines provides two integers $u$ and $v$ — indicating a specific pair of workers who cannot share a shift. Workers are identified by numbers from $1$ to $n$ inclusive.

The records are guaranteed to contain at least one trio of mutually conflicting workers.

## Output
Provide a single line containing three integers $a$, $b$, and $c$, ordered such that $a < b < c$. These integers must represent a trio where the conflicts $a$–$b$, $a$–$c$, and $b$–$c$ are all present in the input. If multiple such trios exist, output the one that is lexicographically first (prioritize the smallest possible value for $a$; if there is a tie, minimize $b$; and if still tied, minimize $c$).

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
