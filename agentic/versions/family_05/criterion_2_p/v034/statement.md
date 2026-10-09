# Compound Synthesis

Time limit: 2 s
Memory limit: 256 MB

## Description

A laboratory is planning a large-scale synthesis process consisting of $k$ parallel reactions. The laboratory's inventory contains exactly $k$ distinct catalysts (labeled 1 to $k$), $k$ distinct reagents (labeled 1 to $k$), and $k$ distinct solvents (labeled 1 to $k$).

Every catalyst has a strict chemical affinity, meaning it can only bind with exactly one specific reagent. Furthermore, no two catalysts share an affinity for the same reagent.

The research team has a database of $t$ documented successful reaction triads. Each triad consists of one catalyst, one reagent, and one solvent.

Your task is to select exactly $k$ reaction triads from the database so that every catalyst, every reagent, and every solvent from the inventory is consumed in exactly one chosen reaction.

## Input

The first line contains the target number of reactions $k$ and the number of documented triads $t$. The target $k$ is at least 1 and is physically limited by the lab's maximum parallel capacity of 1200. The number of triads $t$ can be as low as 0 and will not exceed the maximum possible combinations of catalysts and solvents ($k \times k$).

Each of the subsequent $t$ lines contains three integers $x$, $y$, and $z$, representing the labels for the catalyst, reagent, and solvent in a documented triad. All labels are positive integers bounded by the target $k$.

No triad is duplicated in the input. For any given catalyst, every triad in the database lists the exact same reagent, and no two catalysts are ever listed with the same reagent.

## Output

If a complete synthesis schedule can be formed, print `YES` on the first line. Then, print $k$ lines, each containing the three integers `x y z` of a chosen reaction triad. The triads may be printed in any order. If multiple schedules are valid, any of them is accepted.

If it is impossible to consume all ingredients exactly once, print `NO`.

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
