# Synthesis Protocol Validation

Time limit: 5 s   Memory limit: 256 MB

## Description
A chemical laboratory is preparing a series of experimental batches. The lab inventory contains a set of distinct reagent vials, sequentially numbered starting from 1. The total count of these vials is exactly three times the target number of batches ($3q$).

To ensure stability, a batch must be synthesized using a specific combination of three vials. The research team has provided a catalog of historically stable combinations. A vial can appear in multiple stable combinations in the catalog, but untested combinations are strictly prohibited.

The lab director requires a daily production schedule that selects combinations from the catalog. A valid schedule must satisfy two strict safety requirements: first, a vial can only be consumed once, meaning no vial may be assigned to more than one scheduled batch; second, to prevent degradation, every single vial in the inventory must be utilized by the end of the day.

You must analyze the catalog and determine if a valid daily schedule can be formed. If successful, you must output the chosen combinations. Otherwise, report that the schedule is impossible.

## Input
The first line contains two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000). The target number of batches is **q**, and the total number of distinct reagent vials is 3**q**.
Each of the following **t** lines contains three integers **a**, **b**, and **c** (1 ≤ a < b < c ≤ 3q), representing a stable combination of three vials from the catalog.

## Output
If a valid schedule exists, print `YES` on the first line. Then, output **q** lines, each containing the three vial numbers of a scheduled batch.
If no such schedule can be formed, print `NO`.

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
