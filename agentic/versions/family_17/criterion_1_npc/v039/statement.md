# Problem A — Full-Batch Component Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description
You manage an assembly line that has received a batch of unique components. There are exactly $3q$ components, each stamped with a unique serial number from $1$ to $3q$. Every component must be committed to an assembly — leaving a component unused is treated as a batch failure, and equally, no component can be physically placed into more than one assembly at the same time.

Components are only ever assembled into **modules of exactly three**. Due to strict engineering tolerances, you must select from a pre-approved catalog of tested module designs; ad-hoc combinations are strictly prohibited. The catalog lists all combinations that pass safety checks, so a single component serial number might appear in many different approved designs, and some designs may overlap heavily while others are disjoint — none of that matters except which designs are approved.

A production plan is a selection of some subset of the approved designs. The plan is acceptable only when the chosen designs together account for the **entire** batch with **every** component appearing in **exactly one** chosen module: no component omitted, no component shared between two chosen modules. In other words, the chosen designs must consume the whole batch perfectly — no leftovers and no duplicates.

Your task is to decide whether the approved catalog admits such a perfect consumption of the batch, and if they do, to produce one acceptable production plan. If the catalog cannot cover the batch under these rules, report that no acceptable plan exists. (Note that the mere count of approved designs says nothing: plenty of designs can still fail to consume the batch, and a bare-minimum catalog can still succeed.)

## Input
The first line contains two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000).
Each of the next **t** lines contains three integers a b c (1 ≤ a < b < c ≤ 3q): an approved design.

## Output
If a valid selection exists, print `YES`, then q lines each with the three items of one chosen design.
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
