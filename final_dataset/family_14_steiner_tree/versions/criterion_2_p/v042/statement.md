# Problem B — Repressurizing the Habitat

Time limit: 2 s   Memory limit: 256 MB

## Description

An underwater research station consists of **n** structural modules (numbered 1 to n). These modules are linked by **m** reinforced transit tubes. The station's architecture guarantees that for any two modules, there is exactly one sequence of transit tubes connecting them.

Due to a facility-wide lockdown, all transit tubes are currently depressurized. You have been tasked with repressurizing a subset of the tubes. Each tube requires a specific amount of energy to repressurize.

There are **t** modules designated as primary life-support centers. To ensure the safety of the crew, all primary life-support centers must be integrated into a single accessible zone. This means that any primary life-support center must be reachable from any other primary life-support center by traveling exclusively through repressurized transit tubes (potentially passing through other non-primary modules along the way).

Determine the minimum total energy required to repressurize a valid subset of transit tubes.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the IDs of the primary life-support centers.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a transit tube links module u and module v and requires w units of energy to repressurize. The tubes form the unique-path layout described above.

## Output

Print a single integer: the minimum total energy required to repressurize a set of tubes that integrates all primary life-support centers.

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

In Example 1, the primary life-support centers 1 and 4 can only reach each other by passing through modules 2 and 3. Therefore, all three tubes in the sequence must be repressurized, using 5 + 1 + 2 = 8 units of energy. In Example 2, there is only one primary life-support center, so no tubes need to be repressurized.
