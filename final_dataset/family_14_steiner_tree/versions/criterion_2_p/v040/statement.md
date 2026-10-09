# Problem B — Habitat Pressurization (Phase 2)

Time limit: 2 s   Memory limit: 256 MB

## Description

Establishing a planetary outpost requires multiple stages of infrastructure deployment. In Phase 1, the geological team mapped out **n** habitat pods (numbered 1 to **n**) and identified exactly **m** stable underground tubes that can connect them. The geology dictates that these tubes form a specific arrangement: between any two pods, there is exactly one valid sequence of tubes that links them without looping back.

You are responsible for Phase 2. Central command has designated **t** of these pods as *critical*. You must select a subset of the available tubes to pressurize so that all critical pods share a single breathable atmosphere. This means every critical pod must be able to exchange air with every other critical pod, either directly through a pressurized tube or via a chain of pressurized tubes passing through other pods (which may or may not be critical themselves).

Each tube has a known energy cost to pressurize. Your task is to determine the absolute minimum total energy cost required to achieve this shared atmosphere for all critical pods.

Once Phase 2 is complete, Phase 3 will begin, during which the life support system will circulate oxygen through the network you established.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the identifiers of the critical pods.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a tube exists between pod u and pod v, and it costs w energy units to pressurize it. The provided tubes connect all pods with exactly one valid sequence between any pair, as detailed in Phase 1.

## Output

Print a single integer: the minimum total energy cost to pressurize a valid set of tubes connecting all critical pods.

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
