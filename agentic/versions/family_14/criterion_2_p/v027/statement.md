# Problem B — Subterranean Rescue Operations

Time limit: 2 s   Memory limit: 256 MB

## Description

Deep beneath the surface lies a vast network of **n** subterranean caverns (numbered 1 to **n**). These caverns are linked by **m** natural tunnels. The geological layout is such that between any two caverns, there exists exactly one sequence of tunnels connecting them without visiting the same cavern twice.

Each tunnel is currently blocked by debris and requires a specific number of labor hours to excavate and make passable.

A recent sensor scan has detected life signs in exactly **t** of these caverns. These specific locations must be integrated into a unified rescue network. This means that an explorer must be able to travel from any cavern with life signs to any other cavern with life signs, passing only through excavated tunnels. (They may pass through other caverns along the way, whether those have life signs or not).

Determine the absolute minimum total hours of labor required to excavate a set of tunnels that successfully links all the caverns containing life signs.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the identification numbers of the caverns with life signs.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a tunnel between cavern u and cavern v requiring w hours of labor to excavate. The layout of the tunnels strictly follows the properties described above.

## Output

Print a single integer: the minimum total hours of labor needed to connect all caverns with life signs.

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
