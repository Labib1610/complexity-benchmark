# Problem A — Complete Cell Deployment for the Regional Drill

Time limit: 5 s   Memory limit: 256 MB

## Description
The emergency directorate maintains an active roster of certified operators. Each operator holds a unique badge number from 1 up to a total roster size of 3q.

When deploying personnel, standing policy requires that operators are fielded in cells of exactly three individuals. Furthermore, a cell can only be formed if the specific trio has completed joint certification together. A pre-cleared list of these certified trios is provided by command. An operator may appear in multiple different cleared trios on this list, but ad-hoc combinations not on the list are strictly forbidden.

During an activation, command selects a subset of these pre-cleared trios to form a deployment plan. A plan is considered acceptable under two strict conditions: first, no operator may be assigned to more than one activated cell simultaneously; second, leadership has mandated that no operator may sit idle during a full-scale readiness drill.

Your task is to evaluate the pre-cleared list and determine if it is possible to construct an acceptable deployment plan that assigns the entire roster. If such a plan can be formed, you must output the chosen subset of trios. If the constraints cannot be met, you must report the failure.

## Input
The first line contains two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000). The total number of operators on the roster is 3q.
Each of the next **t** lines contains three integers **a** **b** **c** (1 ≤ a < b < c ≤ 3q), representing a pre-cleared trio of operators.

## Output
If an acceptable deployment plan exists, print `YES` on the first line, followed by **q** lines each containing the three badge numbers of an activated trio in the plan.
If no such plan is possible, print `NO`.

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
