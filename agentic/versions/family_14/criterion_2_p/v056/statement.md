# Heavy Cargo Routing

Time limit: 2 s   Memory limit: 256 MB

## Description

A national rail grid consists of **n** transit yards. The grid is constructed such that any yard can be reached from any other yard, and there is exactly one sequence of direct rail links connecting any given pair of yards. 

To support a new class of heavy cargo locomotives, the rail authority has designated **t** specific yards as primary logistics centers. The authority must reinforce a set of rail links so that heavy cargo can travel between any two logistics centers using exclusively reinforced links. Each rail link has a known reinforcement cost.

Additionally, the rail grid guarantees the following operational constraints:
- The total number of rail links **m** is strictly less than the number of yards **n**.
- The sum of the reinforcement costs for all **m** rail links in the grid is guaranteed not to exceed 200,000,000,000.

Determine the minimum total cost required to reinforce the necessary rail links to interconnect all logistics centers.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200,000, m = n − 1).
The second line provides **t** distinct integers: the identifiers of the transit yards chosen as logistics centers.
Each of the subsequent **m** lines provides three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1,000,000), indicating a direct rail link between yard **u** and yard **v** that costs **w** to reinforce.

## Output

Output a single integer representing the minimum total cost to reinforce rail links such that all logistics centers can reach each other via reinforced links.

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
