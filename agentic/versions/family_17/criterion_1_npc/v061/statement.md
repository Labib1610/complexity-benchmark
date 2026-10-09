# Problem A — Curing Fixture Allocation

Time limit: 5 s
Memory limit: 256 MB

## Description
A manufacturing facility is processing a batch of components, which are numbered consecutively from 1 to $3q$. 

The components are processed by a curing machine that operates in discrete cycles. For each cycle, the machine's robotic loaders must grasp exactly three components. Due to physical clearances between the loaders, the machine can only be programmed with specific grasping configurations. A catalog of $t$ safe configurations is provided, each listing three components that can be processed together in a single cycle.

Your task is to program the machine for a continuous run of exactly $q$ cycles. In each cycle, the machine will use one configuration from the catalog. For the run to be successful, by the end of the $q$ cycles, the machine must have processed all $3q$ components in the batch. Determine if it is possible to select a sequence of configurations for the run that achieves this.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$). The highest-numbered component in the batch is $3q$. 
Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing one safe configuration of three components.

## Output
If a successful run can be programmed, print `YES`. Then, output $q$ lines, each containing the three components of one chosen configuration.
If no such run is possible, print `NO`.

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
