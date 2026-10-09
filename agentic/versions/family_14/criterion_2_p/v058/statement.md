# Problem B — Subterranean Rescue Operations

Time limit: 2 s   Memory limit: 256 MB

## Description

Within a deep-crust geological formation, there are **n** enclosed chambers (numbered 1 to **n**) and **m** structural fissures that connect them. The layout of this formation is such that for any two chambers, there is exactly one sequence of fissures that allows travel between them without entering any chamber more than once.

Every fissure is entirely filled with dense rock and requires a specific number of labor hours to bore through and make passable.

Sensors have detected organic signatures in exactly **t** of these chambers. A continuous, secure transit network must be established among them. To achieve this, it must be possible to navigate from any chamber with an organic signature to any other chamber with an organic signature, traversing only fissures that have been bored through. It is acceptable to route this network through intermediate chambers lacking organic signatures.

Determine the absolute minimum total labor hours required to bore through a set of fissures that satisfies this connectivity requirement.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ **t** ≤ **n**, 1 ≤ **n** ≤ 200000, **m** = **n** − 1).

The second line provides **t** distinct integers: the identification numbers of the chambers containing organic signatures.

Each of the subsequent **m** lines contains three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000), indicating a fissure between chamber **u** and chamber **v** that requires **w** labor hours to bore through. The layout strictly follows the topological properties described above.

## Output

Print a single integer: the minimum total labor hours needed to establish the required transit network.

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
