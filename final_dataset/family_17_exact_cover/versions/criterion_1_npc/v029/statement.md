# Problem A — Full-Coverage Cell Deployment for the Regional Drill

Time limit: 5 s   Memory limit: 256 MB

## Description
The regional emergency directorate is preparing a full-scale readiness drill. Every certified operator on
the active roster must be committed to the exercise — leadership has been explicit that a drill in which
any operator sits idle is treated as a planning failure, and equally that no operator may be counted in
more than one place at the same moment. The roster is fixed for the duration of the drill and consists
of a pool of operators, each with a unique badge number running consecutively from the first badge.

Operators are only ever fielded in standardised response units. Over the years, particular groups of operators have
completed joint certification together, and standing policy permits command to field a unit if and only
if that precise group appears on the pre-cleared list; ad-hoc groups, however sensible they
look, are not permitted. The pre-cleared list has been assembled from historical training records, so a
single operator may well appear in many different cleared groups, and some cleared groups may share members
heavily while others share none — none of that matters except through which groups are cleared.

A deployment plan is an activation of some subset of the cleared groups. The plan is acceptable only when
the activated groups together account for the entire roster with every operator appearing in
exactly one activated unit: no operator omitted, no operator shared between two activated units. In
other words, the activated groups must form a comprehensive assignment over the whole roster — no omissions and no redundancies.

Your task is to decide whether the cleared groups admit such a comprehensive assignment of the roster, and if they
do, to produce one acceptable deployment plan. If the cleared list cannot arrange the roster under these
rules, report that no acceptable plan exists. (Note that the mere count of cleared groups says nothing:
plenty of cleared groups can still fail to arrange the roster, and a bare-minimum list can still succeed.)

## Input
The first line contains two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000).
Each of the next **t** lines contains three integers a b c (1 ≤ a < b < c ≤ 3q): a cleared group.

## Output
If a valid selection exists, print `YES`, then q lines each with the three members of one chosen group.
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
