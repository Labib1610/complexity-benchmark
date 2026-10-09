# System Architecture Validation

Time limit: 2 s   Memory limit: 256 MB

## Description
The engineering team must finalize the system architecture by selecting a subset of potential integrations. The facility contains $2q$ distinct modules, numbered $1$ through $2q$. You are provided with a list of $t$ potential integrations, each specifying two modules that can be linked.

With up to 400,000 potential integrations available, the number of possible subsets is astronomical. You must search this massive space of combinations to find a valid architecture. An architecture is deemed valid if and only if every single module, from $1$ to $2q$, is included in exactly one selected integration. If any module is left isolated, or if it is assigned to multiple integrations, the entire architecture fails. 

The potential integrations provided to you are restricted by the hardware layout: each potential integration will always link a module from the first half ($1 \le a \le q$) with a module from the second half ($q < b \le 2q$). 

Your task is to explore these combinations to determine if at least one valid architecture exists. If it does, output the selected integrations. Otherwise, report that no such architecture is possible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating an allowed integration between module $a$ and module $b$.

## Output
If a valid architecture can be formed, print `YES` on the first line, followed by $q$ lines, each containing the two modules of a selected integration. If no valid architecture exists, print `NO`.

## Example

**Input**
```
3 5
1 4
1 5
2 5
3 5
3 6
```

**Output**
```
YES
1 4
2 5
3 6
```
