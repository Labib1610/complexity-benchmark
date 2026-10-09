# Problem A — Full-Coverage Cell Deployment for the Regional Drill

Time limit: 5 s   Memory limit: 256 MB

## Description
The regional emergency directorate is preparing a full-scale readiness drill. Every certified operator on
the active roster must be committed to the exercise — leadership has been explicit that a drill in which
any operator sits idle is treated as a planning failure, and equally that no operator may be counted in
more than one place at the same moment. The roster is fixed for the duration of the drill and consists
of a pool of operators, each with a unique badge number running consecutively from the first badge.

Operators are only ever fielded in **cells of exactly three**. Over the years, particular trios have
completed joint certification together, and standing policy permits command to field a cell if and only
if that precise three-person trio appears on the pre-cleared list; ad-hoc trios, however sensible they
look, are not permitted. The pre-cleared list has been assembled from historical training records, so a
single operator may well appear in many different cleared trios, and some cleared trios may overlap
heavily while others are disjoint — none of that matters except through which trios are cleared.

A deployment plan is an activation of some subset of the cleared trios. The plan is acceptable only when
the activated trios together account for the **entire** roster with **every** operator appearing in
**exactly one** activated cell: no operator omitted, no operator shared between two activated cells. In
other words, the activated trios must tile the whole roster perfectly — no gaps and no overlaps.

Your task is to decide whether the cleared trios admit such a perfect tiling of the roster, and if they
do, to produce one acceptable deployment plan. If the cleared list cannot cover the roster under these
rules, report that no acceptable plan exists. (Note that the mere count of cleared trios says nothing:
plenty of cleared trios can still fail to tile the roster, and a bare-minimum list can still succeed.)

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
