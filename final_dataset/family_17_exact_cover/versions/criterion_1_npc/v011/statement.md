# Problem A — Archival Display Logistics

Time limit: 5 s   Memory limit: 256 MB

## Description
The national museum is planning a comprehensive retrospective. The archives contain a collection of historical artifacts, and the curators have mandated that the entire collection must be put on display. No artifact may be left in storage, and naturally, no artifact can be in two places at once. 

Over the decades, the museum has commissioned various custom-built display cases. Because of strict climate-control and structural requirements, each available case was designed to house a specific set of exactly three artifacts. A case cannot be used unless it holds the exact three artifacts it was crafted for—leaving a slot empty or substituting a different artifact would compromise the internal humidity balance. 

The museum has kept a catalog of all these custom cases. Your task is to determine whether it is possible to select a subset of the existing display cases such that every single artifact in the collection is exhibited exactly once. In a successful arrangement, the chosen cases will perfectly accommodate the entire collection with no empty slots and no artifacts left behind.

## Input
The first line contains two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000). The total number of artifacts in the collection is exactly 3q, and they are identified by integers from 1 to 3q.
Each of the following **t** lines contains three integers a, b, and c (1 ≤ a < b < c ≤ 3q), representing the ID numbers of the three artifacts that a particular display case is designed to hold.

## Output
If a valid arrangement of display cases exists, print `YES` on the first line. Then, output q lines, each containing the three artifact IDs of a chosen display case.
If it is impossible to display the collection under these rules, print `NO`.

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
