# Linear Production Facility

Time limit: 5 s   Memory limit: 256 MB

## Description
A manufacturing plant is setting up $n$ production modules along a single straight corridor. The corridor contains a sequence of distinct installation bays. These bays are numbered consecutively, starting at 1 and ending exactly at the total headcount of modules. Each module must be assigned to one bay, and no two modules may occupy the same bay.

The modules exchange materials using $m$ dedicated conveyor belts, each directly linking a specific pair of modules. The belt system is designed so that materials can successfully travel between any two modules, possibly passing through intermediate modules. To save on hardware, the total count of belts $m$ is exactly the minimum quantity necessary to ensure this full reachability.

The mechanical strain on a belt connecting a module installed at bay $x$ and another module installed at bay $y$ is determined by the physical gap between them, calculated as $|x - y|$. The plant has a strict strain tolerance $B$ for the sum of the strains across all $m$ belts in the system.

Determine an assignment of modules to installation bays such that the total mechanical strain does not exceed $B$, or report that no such assignment is possible.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the following $m$ lines contains two integers $u$ and $v$, indicating a conveyor belt between module $u$ and module $v$. (The network structure guarantees that all modules are reachable from each other, and $m$ is exactly the minimum number of connections required to achieve this).

## Output
If the tolerance $B$ can be met, print `YES` on the first line. On the second line, print $n$ integers separated by spaces, where the $i$-th integer represents the bay number (from 1 to $n$) assigned to module $i$. If multiple valid assignments exist, you may output any of them.
If the tolerance cannot be met, print `NO`.

## Example

### Input
```text
5 4 6
1 2
1 3
1 4
1 5
```

### Output
```text
YES
3 1 2 4 5
```
