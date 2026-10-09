# Problem B — Chamber Alignment in the Manufacturing Pipeline

Time limit: 5 s   Memory limit: 256 MB

## Description
The automated setup of our chemical manufacturing pipeline is divided into three distinct stages: blueprint extraction, chamber alignment, and fluid dynamics simulation. You are responsible solely for the second stage: chamber alignment. 

**Stage 1: Blueprint Extraction (Completed)**
The system has already parsed the chemical blueprint, identifying $n$ distinct reaction stages and $m$ transfer pipes that must connect them. The blueprint analysis guarantees that the reaction stages form a unified, loop-free hierarchy: apart from a single final collector, every reaction stage feeds its output directly into exactly one other stage. 

**Stage 2: Chamber Alignment (Your Task)**
The factory features a single straight corridor containing $n$ empty chamber slots, numbered sequentially from $1$ to $n$. You must assign each of the $n$ reaction stages to a unique slot. 

When a transfer pipe connects a reaction stage placed in slot $x$ to a reaction stage placed in slot $y$, a physical tube of length $|x - y|$ must be installed, regardless of the direction of chemical flow. The factory has a total tube material budget of $B$. You must find a slot assignment where the sum of the lengths of all $m$ required tubes is at most $B$, or report that the budget cannot be met.

**Stage 3: Fluid Dynamics Simulation (Pending)**
If you find a valid slot assignment that respects the material budget, it will be passed to the physics engine to simulate pressure drops. If no such assignment exists, the blueprint is immediately scrapped.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that a transfer pipe connects reaction stage $u$ and reaction stage $v$. 
(As guaranteed by Stage 1, $m = n - 1$ and the connections form the hierarchy described).

## Output
If the blueprint can proceed to Stage 3, print `YES` on the first line. On the second line, print $n$ integers representing your assignment: the $i$-th integer must be the slot number (from $1$ to $n$) assigned to reaction stage $i$. This sequence must be a permutation of the integers from $1$ to $n$.
If the blueprint must be scrapped because no assignment meets the budget, print `NO`.

## Example

**Input**
```
5 4 5
1 2
1 3
3 4
3 5
```

**Output**
```
YES
2 1 3 4 5
```
