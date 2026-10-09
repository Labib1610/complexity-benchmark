# Problem A — Full-Coverage Asteroid Extraction for the Regional Sector

Time limit: 5 s   Memory limit: 256 MB

## Description
The planetary mining consortium is preparing a full-scale extraction sweep. Every tracked asteroid in the local cluster must be committed to the harvest — leadership has been explicit that a sweep in which any asteroid sits idle is treated as a planning failure, and equally that no asteroid may be claimed by more than one drone at the same moment. The cluster is fixed for the duration of the sweep and consists of a field of asteroids, each with a unique catalog number running consecutively from 1.

Asteroids are only ever harvested in **batches of exactly three**. Over the years, particular trios have had their gravitational interactions modeled together, and standing policy permits command to harvest a batch if and only if that precise three-asteroid trio appears on the pre-cleared list; ad-hoc trios, however sensible they look, are not permitted. The pre-cleared list has been assembled from historical simulation records, so a single asteroid may well appear in many different cleared trios, and some cleared trios may overlap heavily while others are disjoint — none of that matters except through which trios are cleared.

An extraction schedule is an activation of some subset of the cleared trios. The schedule is acceptable only when the activated trios together account for the **entire** cluster with **every** asteroid appearing in **exactly one** activated batch: no asteroid omitted, no asteroid shared between two activated batches. In other words, the activated trios must tile the whole cluster perfectly — no gaps and no overlaps.

Your task is to decide whether the cleared trios admit such a perfect tiling of the cluster, and if they do, to produce one acceptable extraction schedule. If the cleared list cannot cover the cluster under these rules, report that no acceptable schedule exists. (Note that the mere count of cleared trios says nothing: plenty of cleared trios can still fail to tile the cluster, and a bare-minimum list can still succeed.)

## Input
The first line contains two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000).
Each of the next **t** lines contains three integers a b c (1 ≤ a < b < c ≤ 3q): an allowed triple.

## Output
If a valid selection exists, print `YES`, then q lines each with the three items of one chosen triple.
Otherwise print `NO`.

## Examples
### Example 1
Input:
```
2 3
1 2 3
4 5 6
1 4 5
```
Output:
```
YES
1 2 3
4 5 6
```
