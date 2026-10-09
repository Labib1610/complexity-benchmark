# Problem B — Bulkhead Installation

Time limit: 2 s   Memory limit: 256 MB

## Description
A specialized laboratory consists of various work areas linked by bidirectional transit tubes. Each tube requires a specific amount of labor hours to permanently block with a bulkhead. A blocked tube permits no passage in either direction.

Two designated work areas handle incompatible materials. You must select a set of tubes to permanently block so that it is impossible to travel from the first designated area to the second designated area through any sequence of unblocked tubes. The total labor hours required to install all selected bulkheads cannot exceed a given maximum allowance. The accessibility of any other work area does not matter, provided the two designated areas cannot reach each other.

Determine if such a selection is possible within the allowance, and if so, provide the list of tubes to block.

## Input
The first line contains five integers: $n$ (the number of work areas), $m$ (the number of transit tubes), $s$ and $t$ (the identifiers of the two designated areas), and $B$ (the maximum labor allowance). Work areas are numbered from 1 to $n$.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$, indicating a transit tube between work areas $u$ and $v$ that requires $w$ labor hours to block.

## Output
If the requirement can be met without exceeding the allowance, print `YES`.
On the next line, print the number $c$ of tubes to block.
Then, print $c$ lines, each containing two integers $u$ and $v$, representing a blocked tube.
If the requirement cannot be met within the allowance, print `NO`.

## Example

**Input**
```text
4 4 1 4 10
1 2 5
1 3 6
2 4 4
3 4 7
```

**Output**
```text
YES
2
2 4
1 3
```
