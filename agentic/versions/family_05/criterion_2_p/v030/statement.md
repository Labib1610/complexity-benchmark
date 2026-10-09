# Chemical Synthesis Selection

Time limit: 2 s
Memory limit: 256 MB

## Description

A laboratory is finalizing a set of $k$ chemical reactions. Each reaction is defined by a triplet of parameters: a catalyst ($x$), a solvent ($y$), and a temperature setting ($z$). All three parameters are indexed by integers from $1$ to $k$.

You are provided a log of $t$ successful test reactions. You must select exactly $k$ reactions from this log such that each of the $k$ catalysts, each of the $k$ solvents, and each of the $k$ temperature settings is utilized in exactly one chosen reaction.

The test log was generated under the following strict laboratory procedures:
- Each catalyst was permanently dissolved into a specific solvent before testing began. Therefore, any test reaction involving a particular catalyst will always involve that exact same solvent.
- The preparation process ensured that no two catalysts were dissolved into the same solvent.
- Various temperature settings were then tested on these mixtures, and any stable reactions were recorded in the log.

Determine whether a valid selection of $k$ reactions exists, and if so, report one such selection.

## Input

The first line contains two integers $k$ and $t$ ($1 \le k \le 1200$, $0 \le t \le k \cdot k$): the number of parameter indices and the number of logged test reactions.
Each of the next $t$ lines contains three integers $x$, $y$, and $z$ ($1 \le x, y, z \le k$), representing a stable reaction involving catalyst $x$, solvent $y$, and temperature setting $z$. No triplet is listed more than once. The input is guaranteed to follow the laboratory procedures described above.

## Output

If a valid selection of $k$ reactions exists, print `YES` on the first line. Then, print $k$ lines, each containing the three integers `x y z` of one selected reaction. The $k$ lines may be printed in any order. Any valid selection is accepted.

If no valid selection exists, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 1 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 2 1
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```
