# Problem A — Full-Coverage Module Assembly for the Regional Run

Time limit: 5 s   Memory limit: 256 MB

## Description
The regional manufacturing directorate is preparing a full-scale production run. Every certified component in the active inventory must be committed to the assembly — leadership has been explicit that a run in which any component sits idle is treated as a planning failure, and equally that no component may be used in more than one place at the same moment. The inventory is fixed for the duration of the run and consists of a pool of components, each with a unique serial number running consecutively from the first serial.

Components are only ever assembled into **modules of exactly three**. Over the years, particular combinations have completed compatibility testing together, and standing policy permits engineering to build a module if and only if that precise three-part combination appears on the approved list; ad-hoc combinations, however sensible they look, are not permitted. The approved list has been assembled from historical testing records, so a single component may well appear in many different approved combinations, and some approved combinations may overlap heavily while others are disjoint — none of that matters except through which combinations are approved.

An assembly plan is a selection of some subset of the approved combinations. The plan is acceptable only when the selected combinations together account for the **entire** inventory with **every** component appearing in **exactly one** assembled module: no component omitted, no component shared between two assembled modules. In other words, the selected combinations must consume the whole inventory perfectly — no leftovers and no duplicates.

Your task is to decide whether the approved combinations admit such a perfect consumption of the inventory, and if they do, to produce one acceptable assembly plan. If the approved list cannot cover the inventory under these rules, report that no acceptable plan exists. (Note that the mere count of approved combinations says nothing: plenty of approved combinations can still fail to consume the inventory, and a bare-minimum list can still succeed.)

## Input
The first line contains two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000).
Each of the next **t** lines contains three integers a b c (1 ≤ a < b < c ≤ 3q): an approved combination.

## Output
If a valid selection exists, print `YES`, then q lines each with the three items of one chosen combination.
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
