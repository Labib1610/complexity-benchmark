# Problem A — Focus Group Selection

Time limit: 5 s   Memory limit: 256 MB

## Description

A market research agency is executing a multi-phase campaign to evaluate a new product. The campaign proceeds as follows:

**Phase 1: Relationship Mapping.** The agency surveys a pool of **n** candidates (identified by integers 1 through **n**) and compiles a list of **m** existing relationships. Each relationship indicates that two candidates already know each other.

**Phase 2: Unbiased Selection (Your Task).** The agency must isolate a focus group of exactly **k** candidates. To guarantee uninfluenced feedback and prevent participants from discussing the product outside the testing environment, the focus group must be strictly composed of individuals who have no prior relationship with one another. There cannot be a relationship between any two candidates chosen for the group.

**Phase 3: Deployment.** The chosen candidates are shipped the prototype, and their isolated reviews are synthesized into a final report.

You are responsible for implementing Phase 2. Given the relationship map from Phase 1 and the required group size **k**, determine if a valid focus group can be formed, and if so, identify the candidates to be passed to Phase 3.

## Input

The first line provides three integers: **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
The following **m** lines each contain two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a relationship between candidate **u** and candidate **v**. No relationship is provided more than once.

## Output

If it is possible to form the required focus group, output `YES` on the first line. On the second line, output the **k** distinct candidate identifiers that make up the group, separated by spaces. If multiple valid groups exist, any one is acceptable.

If no such group of exactly **k** candidates can be formed, output `NO`.

## Examples

### Example 1

**Input**
```
4 4 3
1 2
1 3
2 3
3 4
```

**Output**
```
NO
```

### Example 2

**Input**
```
5 2 3
1 2
3 4
```

**Output**
```
YES
1 3 5
```

### Example 3

**Input**
```
3 3 1
1 2
2 3
1 3
```

**Output**
```
YES
1
```
