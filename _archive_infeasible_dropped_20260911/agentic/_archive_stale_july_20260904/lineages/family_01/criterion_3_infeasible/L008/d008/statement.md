# Problem C — Proof of Impossibility

Time limit: 2 s
Memory limit: 256 MB

Management insists on dividing the workforce into exactly two non-overlapping shifts. However, the HR department knows this plan is doomed. You must provide undeniable proof of this failure.

HR has a collection of incident files. Each file lists two specific workers who cannot be placed on the same shift. 

You can prove the plan is impossible by finding a specific combination of records. Specifically, you must identify a set of exactly three incident files such that the total number of unique workers mentioned across those three files is exactly three. 

It is guaranteed that at least one such set of three files exists. Your task is to deduce which three distinct workers are involved in this set and report their IDs to HR.

## Input
The first line provides the workforce size n and the total incident count m. The workforce size n is bounded below by 3 and bounded above by the facility capacity of 2000. The incident count m is at least 3, and is capped by either the theoretical maximum of n·(n−1)/2 distinct combinations, or the archival capacity of 2·10⁵, whichever is smaller. Workers are identified by integers from 1 to n.

Each of the next m lines contains two integers u and v (1 ≤ u, v ≤ n, u ≠ v), identifying the two workers involved in a single incident file. No two incident files list the exact same pair of workers.

It is guaranteed that at least one valid set of three files (and thus, three workers) exists.

## Output
Output three space-separated integers a, b, and c representing the IDs of the three workers involved. They must be printed such that a < b < c.

To ensure a unique valid response when multiple such groups of workers exist, you must select the group that minimizes the value of a. If there is a tie, minimize the value of b among the tied triplets, and if a tie still persists, minimize c.

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