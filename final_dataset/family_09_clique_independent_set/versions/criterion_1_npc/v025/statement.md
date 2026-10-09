# Orbital Deconfliction

Time limit: 5 s
Memory limit: 256 MB

## Description

A space agency is planning to launch a cluster of satellites. There are **n** candidate orbital trajectories (numbered 1 to **n**). Due to the geometry of the orbits, certain pairs of trajectories intersect at altitudes that pose a risk of collision. There are **m** such colliding pairs.

Your task is to select exactly **k** trajectories to be used for the launch, such that the chosen set is completely collision-free. That is, no two trajectories in your selected set may pose a risk of collision with each other.

To assist with trajectory calculations, the orbital mechanics governing the candidates guarantee the following structural invariants for the input data:
- **Bounded Density:** The maximum size of any subset of candidate trajectories where every trajectory collides with every other trajectory in that subset is strictly less than 47.
- **Bounded Chain Length:** If we trace chains of collision risks (a sequence of distinct trajectories where each consecutive pair poses a collision risk), the maximum number of links (risk connections) in any such chain is at most 45.

Given **n**, **m**, **k**, and the list of collision risks, determine if a completely collision-free set of exactly **k** trajectories exists, and if so, identify one such set.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ **n** ≤ 46, 0 ≤ **m** ≤ **n**·(**n**−1)/2, 1 ≤ **k** ≤ **n**).
Each of the following **m** lines contains two integers **u** and **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), representing a collision risk between trajectory **u** and trajectory **v**. No collision risk is listed more than once.

## Output

If a collision-free set of exactly **k** trajectories exists, print `YES` on the first line. On the second line, print **k** distinct trajectory numbers forming your set, separated by spaces. If there are multiple valid sets, any one of them will be accepted.

If no such set exists, print `NO`.

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
