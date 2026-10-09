# Chemical Synthesis Selection

Time limit: 2 s
Memory limit: 256 MB

## Description

A research facility is finalizing a set of $k$ synthesis procedures. The procedures involve three types of components, each indexed by integers from $1$ to $k$: reagents, reaction vessels, and pressure settings.

You are given a record of $t$ successful trial runs. Your task is to choose exactly $k$ trial runs from this record to form a complete synthesis protocol. A valid protocol must use every reagent exactly once, every reaction vessel exactly once, and every pressure setting exactly once across the $k$ chosen runs.

The trial runs were conducted according to a strict laboratory preparation protocol:
- Prior to any testing, the chemists distributed the $k$ reagents among the $k$ reaction vessels.
- They placed each reagent entirely into a vessel, ensuring that every vessel received exactly one reagent.
- Because the reagents could not be transferred once distributed, any trial run that tested a particular reagent necessarily took place in the specific reaction vessel that held it.
- Various pressure settings were then applied to these prepared vessels, and the successful outcomes were logged.

Determine whether a valid protocol of $k$ trial runs exists, and if so, output one such combination.

## Input

The first line contains two integers $k$ and $t$ ($1 \le k \le 1200$, $0 \le t \le k \cdot k$): the number of distinct indices per component type and the total number of logged trial runs.
Each of the next $t$ lines contains three integers $x$, $y$, and $z$ ($1 \le x, y, z \le k$), representing a successful trial run using reagent $x$, reaction vessel $y$, and pressure setting $z$. No specific $(x, y, z)$ combination appears more than once. The input is guaranteed to be consistent with the preparation protocol described above.

## Output

If a valid protocol of $k$ trial runs exists, print `YES` on the first line. Following this, print $k$ lines, each containing the three integers `x y z` of one chosen trial run. The $k$ lines can be printed in any order. Any valid protocol is accepted.

If no valid protocol exists, print `NO`.

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
