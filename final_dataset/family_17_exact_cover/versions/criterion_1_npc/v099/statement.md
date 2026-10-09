# Problem A — Curing Fixture Allocation

Time limit: 5 s
Memory limit: 256 MB

## Description
A manufacturing facility must process a batch of components. The batch is defined by a production parameter $q$, and the components are assigned sequential integer IDs from $1$ up to $3q$.

The components are processed in a thermal chamber that requires specialized stabilizing frames to prevent warping. The engineering team has certified $t$ safe frame setups. Each setup specifies a group of components that can be safely loaded and cured together in a single operation. 

The facility requires a production schedule consisting of $q$ operations. For each operation, the operators must select one certified setup from the catalog. The schedule is considered complete if, at the end of the $q$ operations, every component in the batch has been successfully cured. 

Determine whether it is possible to formulate a complete schedule.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$). The highest component ID in the batch is $3q$. 

Each of the subsequent $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the IDs of the components in one certified setup.

## Output
If a complete schedule can be formulated, print `YES`. On the following $q$ lines, output the three component IDs of each setup used in the schedule. 
If no such schedule can be found, print `NO`.

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
