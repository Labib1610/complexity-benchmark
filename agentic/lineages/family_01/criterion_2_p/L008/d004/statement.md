# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

A factory employs $n$ workers, with $m$ synchronization links established among them. You must assign a shift code $s_i \in \{1, 2\}$ to each worker $i$. 

To maintain proper timing, each worker's machine is configured with two gears: a primary gear and a secondary gear. The sizes of these gears are entirely determined by the assigned shift code:
- If a worker is assigned shift code 1, their primary gear has 5 teeth and their secondary gear has 10 teeth.
- If a worker is assigned shift code 2, their primary gear has 10 teeth and their secondary gear has 5 teeth.

A synchronization link between two workers $u$ and $v$ is only stable if their machines are compatible. Specifically, the primary gear of worker $u$ must have the exact same number of teeth as the secondary gear of worker $v$. 
(Note: Due to the gear sizes for the two shifts, if $u$'s primary gear matches $v$'s secondary gear, then $v$'s primary gear will automatically match $u$'s secondary gear. Therefore, this compatibility condition is symmetric and does not depend on the order of the two connected workers.)

Determine if there is a valid assignment of shift codes for all workers such that every synchronization link in the factory is stable.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of workers connected by a synchronization link.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \ldots, s_n$ (each in $\{1,2\}$) representing the valid assignment. If there are multiple valid assignments, output the one that is lexicographically smallest as a full sequence of $n$ integers.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```