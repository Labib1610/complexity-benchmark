# Industrial Pipeline Flushing

Time limit: 2 s   Memory limit: 256 MB

## Description

An industrial chemical plant consists of **n** mixing vats and **m** bidirectional pipe segments connecting them. Each pipe segment has a specific volume, which determines the cost to fill it with a neutral purging agent. A specific chemical reaction has left dangerous residue in a subset of **t** vats. 

You must select a set of pipe segments to fill with the purging agent such that the agent can flow freely between all **t** contaminated vats. The agent can flow through uncontaminated intermediate vats if necessary. 

The plant's piping was designed such that **m** = **n** − 1 and there is exactly one sequence of pipe segments connecting any given pair of vats. 

Your objective is to determine the minimum total cost of purging agent required to connect all **t** contaminated vats.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the identifiers of the contaminated vats.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), representing a pipe segment between vat **u** and vat **v** requiring a purging agent cost of **w**. The pipe segments follow the structural property described above.

## Output

Print a single integer: the minimum total cost of purging agent required to connect all contaminated vats.

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

In Example 1, the contaminated vats are 1 and 4. The only way to connect them is to fill the pipe segments between 1 and 2, 2 and 3, and 3 and 4. The total cost is 5 + 1 + 2 = 8. In Example 2, there is only one contaminated vat, so no pipe segments need to be filled and the required cost is 0.
