# Problem B — Phase 2: Route Planning

Time limit: 2 s
Memory limit: 256 MB

## Description
The Interstellar Trade Commission processes shipping manifests in three distinct phases. 

In Phase 1 (Demand Aggregation), a central authority determines the necessary quota of goods to be shipped from a production facility to a distribution hub. They also compile a list of all active one-way shipping lanes between various locations. 

Phase 2 (Route Planning) is where your software module comes in. You are given the quota and the active shipping lanes, along with the maximum tonnage each lane can support. You must determine a valid distribution of the cargo across the lanes that fulfills the quota. All cargo units are indivisible. The distribution must adhere to two physical laws:
- Tonnage limits: A lane cannot carry a negative amount of cargo, nor can it carry more than its specified maximum tonnage. 
- Mass conservation: Transfer platforms (any location other than the production facility and the distribution hub) lack storage capabilities. Therefore, the total tonnage arriving at any transfer platform must exactly equal the total tonnage departing from it. For the production facility, the departing tonnage minus the arriving tonnage must exactly equal the required quota. For the distribution hub, the arriving tonnage minus the departing tonnage must exactly equal the required quota.

In Phase 3 (Execution), if your module produces a valid plan, it is fed to the navigation AI which schedules the physical freighters. If no valid plan can be formed, the request is rejected. 

Your task is to write the Phase 2 module to either generate the exact lane-by-lane tonnage assignments or conclude that the quota cannot be met.

## Input
The first line contains three integers: $n$ (the number of locations), $m$ (the number of shipping lanes), and the number $1$ (representing a single commodity type).
The second line contains three integers: $s$ (the production facility), $t$ (the distribution hub), and $d$ (the required quota).
The following $m$ lines describe the shipping lanes as determined in Phase 1. Each line contains three integers: $u$, $v$, and $cap$, representing a one-way shipping lane from location $u$ to location $v$ with a maximum tonnage of $cap$.
Locations are numbered from $1$ to $n$.

## Output
If Phase 3 can proceed, print `YES` on the first line. On the second line, print $m$ space-separated integers, where the $j$-th integer represents the tonnage assigned to the $j$-th shipping lane (in the exact order they were provided in the input).
If the quota cannot be met, print `NO`.

## Example

### Input
```text
4 5 1
1 4 10
1 2 5
1 3 10
2 3 5
2 4 5
3 4 5
```

### Output
```text
YES
5 5 0 5 5
```
