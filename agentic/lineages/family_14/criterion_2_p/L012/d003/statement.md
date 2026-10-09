# Document Routing Consolidation

Time limit: 2 s   Memory limit: 256 MB

## Description

A corporate headquarters consists of $n$ departments. Exactly $t$ of these departments are designated as **Auditing Offices**.

The headquarters has a legacy network of $m$ undirected pneumatic tube lines, each linking a pair of departments. The infrastructure of available lines spans the entire headquarters such that every department is reachable from any other. To minimize redundancy, the network was built with exactly $m = n - 1$ lines, ensuring there are no alternative routes between any pair of departments.

Each line requires a specific maintenance budget to remain operational. You must select a subset of these lines to keep active. In the infrastructure containing only your selected lines, all $t$ Auditing Offices must be able to route documents to each other (meaning any Auditing Office can send documents to any other Auditing Office, possibly passing through other intermediate departments). Lines that are not selected are decommissioned and provide no routing capabilities.

Your objective is to determine the minimum total maintenance budget required to select a valid subset of lines that interconnects all Auditing Offices.

## Input

The first line contains three integers: $n$, $m$, and $t$.
- $n$ is the total number of departments. The headquarters contains at least 1 department and at most 200000.
- $m$ is the number of available lines, which is exactly $n - 1$.
- $t$ is the number of Auditing Offices, which is at least 1 and at most $n$.

The second line contains $t$ distinct integers: the identifiers of the Auditing Offices (from 1 to $n$).

Each of the next $m$ lines details an available undirected line with three integers: $u$, $v$, and $w$.
- $u$ and $v$ are distinct department identifiers (from 1 to $n$) linked by the line.
- $w$ is the maintenance budget required to keep this line active. This cost is a positive integer not exceeding 1000000.

These $m$ lines form the exact layout described above, guaranteeing a single route between any two departments.

## Output

Print a single integer: the minimum total maintenance budget required to interconnect all Auditing Offices using only the selected lines.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```

## Note

In Example 1, the Auditing Offices 1 and 4 can only route documents to each other by passing through departments 2 and 3, so all three lines (5 + 1 + 2 = 8) must be selected. In Example 2, there is only one Auditing Office. With one required department, an empty set of lines is valid, so the minimum cost is 0.