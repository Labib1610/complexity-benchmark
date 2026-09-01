# Problem C — Proof of Impossibility

Time limit: 2 s
Memory limit: 256 MB

Management insists on dividing the workforce into exactly two non-overlapping shifts. However, the HR department knows this plan is doomed. You must provide undeniable proof of this failure.

HR has a collection of incident files. Each file lists two specific workers who cannot be placed on the same shift. 

You can prove the plan is impossible by finding a specific combination of records. To do this, you must identify a core group of exactly three distinct workers that satisfies a specific structural condition.

For any group of three workers, we define two metrics based on the incident files:
- $T$: The sum of the individual incident file counts for each of the three workers. (For example, if the chosen workers are $x, y,$ and $z$, $T$ is the total number of files listing $x$, plus the total number of files listing $y$, plus the total number of files listing $z$).
- $E$: The number of incident files that list exactly one worker from this core group of three (and one worker outside this core group).

You must find a group of exactly three distinct workers such that $T = E + 6$.

## Input
The first line provides the workforce size $n$ and the total incident count $m$. The workforce size $n$ is bounded below by 3 and bounded above by the facility capacity of 2000. The incident count $m$ is at least 3, and is capped by either the theoretical maximum of $n(n-1)/2$ distinct combinations, or the archival capacity of $2 \cdot 10^5$, whichever is smaller. Workers are identified by integers from 1 to $n$.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), identifying the two workers involved in a single incident file. All $m$ incident files represent unique pairs of workers (no two files list the exact same pair).

It is guaranteed that at least one valid group of three workers satisfying the condition exists.

## Output
Output three space-separated integers $a$, $b$, and $c$ representing the IDs of the three workers in the group. They must be printed such that $a < b < c$.

To ensure a unique valid response when multiple such groups of workers exist, you must select the group that minimizes the value of $a$. If there is a tie, minimize the value of $b$ among the tied triplets, and if a tie still persists, minimize $c$.

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