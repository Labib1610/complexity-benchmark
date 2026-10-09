# Problem A — Full-Coverage Cell Deployment for the Regional Drill

Time limit: 5 s   Memory limit: 256 MB

## Description
The regional emergency directorate is executing a comprehensive mobilization exercise. The primary directive from leadership is total participation: every single certified operator currently on the active roster must be assigned to the field. Furthermore, an operator is a physical person and cannot be present in multiple places simultaneously. 

Field operations are strictly conducted by units of precisely three operators. Due to safety regulations, command cannot simply group any three operators together. A unit can only be authorized if its specific three-person combination is explicitly listed in the pre-cleared training archive. These cleared trios are based on past joint certifications. An operator might be part of several different cleared trios, and some trios might share operators, but the only combinations that can be fielded are the ones explicitly listed in the archive.

A valid mobilization strategy consists of authorizing a specific set of cleared trios. This strategy is considered successful if and only if the chosen trios collectively include every operator on the roster exactly once. No operator can be left behind, and no operator can be assigned to more than one authorized unit. 

Your objective is to determine if it is possible to achieve a successful mobilization strategy using the available cleared trios. If it is possible, you must output one such strategy. If the given cleared trios cannot perfectly cover the roster under these constraints, you must report that no such strategy exists.

The staging facility is built with exactly 200 dispatch bays. Since each deployed unit occupies exactly one bay, the number of units to form cannot exceed this physical limit, though a minimum of one unit is always mobilized. The central training archive is provisioned to store up to 20,000 historical certification records, meaning the number of pre-cleared trios can range from zero up to this maximum capacity.

## Input
The first line contains two integers **q** and **t**, representing the required number of units and the number of pre-cleared trios, respectively. Their bounds are determined by the facility and archive capacities described above.

Each of the subsequent **t** lines contains three integers **a**, **b**, and **c**, representing the badge numbers of a pre-cleared trio. The operators on the active roster are identified by sequential badge numbers starting from 1 up to the exact total headcount required to fully staff **q** units. The badges in each trio are provided in strictly ascending order.

## Output
If a successful mobilization strategy exists, output `YES` on the first line. Then, output **q** lines, each containing the three badge numbers of an authorized unit from your strategy.
If no such strategy is possible, output `NO`.

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
