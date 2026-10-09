# Problem B — Fiber Interlink for Priority Facilities

Time limit: 2 s   Memory limit: 256 MB

## Description

A sprawling technology park consists of $n$ facilities, indexed $1$ through $n$. The park's central database allocates exactly 200,000 rows for facility records, meaning the number of facilities $n$ is a positive integer that will not exceed this capacity.

To facilitate high-speed data transfer, certain pairs of facilities can be joined by a fiber link. The park's topography dictates that the total number of available fiber links $m$ is exactly one less than the number of facilities. Furthermore, the network design ensures that between any two facilities, there exists exactly one sequence of fiber links that joins them without passing through any facility more than once.

The administration has designated $t$ priority facilities. The number of priority facilities $t$ is at least a single facility, up to a maximum of $n$. All priority facilities must be able to communicate with one another, either directly or by passing through intermediate relay facilities. 

You must select a subset of the available fiber links to install such that all priority facilities are interconnected (non-priority facilities may be used as relays if needed, but do not otherwise have to be connected). Each fiber link has an installation cost $w$, given as an integer number of cents. By law, no single link can cost less than 1 cent, nor can it exceed a maximum of 10,000 dollars. Determine the minimum total cost required to achieve this connectivity.

## Input

The first line provides three integers: $n$, $m$, and $t$. Their respective limits are derived from the physical and database constraints described above.
The second line contains $t$ distinct integers representing the indices of the priority facilities.
This is followed by $m$ lines, each containing three integers $u$, $v$, and $w$. These values indicate an available fiber link between distinct facilities $u$ and $v$ with an installation cost of $w$ cents. The layout of these links matches the topographical constraints detailed earlier.

## Output

Output a single integer representing the minimum total cost, in cents, to interconnect all priority facilities.

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
