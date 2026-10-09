# Problem B — Linear Bay Assignment for Module Integration

Time limit: 5 s
Memory limit: 256 MB

## Description
An engineering team is deploying a system of $n$ modules. The deployment site features a straight rail with exactly $n$ mounting bays, numbered sequentially from $1$ to $n$. Each bay must house exactly one module.

The system relies on $m$ dedicated communication cables, each linking a specific pair of modules. The modules and cables are designed so that the entire system could be powered up sequentially: it is possible to start with any single module and then bring each remaining module online one by one, each time using exactly one cable to link the new module to an already-online module. As a result, the total number of cables $m$ is always exactly $n - 1$.

When a cable links a module placed in bay $x$ and a module placed in bay $y$, the physical length of that cable is $|x - y|$. The cables can overlap along the rail without interference. The installation has a strict total cable allowance of $B$, meaning the sum of the lengths of all $m$ cables cannot exceed $B$.

Determine an assignment of modules to bays such that the total cable length is at most $B$, or determine that the allowance is insufficient.

## Input
The first line provides three integers $n$, $m$, and $B$, representing the number of modules, the number of cables, and the maximum allowed total cable length.
Each of the following $m$ lines provides two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that a cable links module $u$ and module $v$.

## Output
If a valid assignment exists, print `YES` on the first line. On the second line, print $n$ integers. The $i$-th integer must be the bay number (from $1$ to $n$) where module $i$ is installed. Every bay number from $1$ to $n$ must appear exactly once.
If no such assignment is possible, print `NO`.

## Example
### Input
```text
5 4 6
1 2
1 3
3 4
3 5
```

### Output
```text
YES
3 2 4 1 5
```
