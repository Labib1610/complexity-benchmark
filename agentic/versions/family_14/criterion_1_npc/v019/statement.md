# Problem A — Harmonic Convergence

Time limit: 5 s   Memory limit: 256 MB

## Description

An artificer works with **n** tuning crystals (numbered 1 to **n**). The crystals naturally vibrate at different frequencies. The artificer can choose to harmonize certain pairs of crystals so that they vibrate together. 

The artificer knows of **m** specific pairs of crystals that can be harmonized, and each pair requires a specific amount of latent energy to process. The artificer chooses a set of pairs to harmonize, and the total energy expended is the sum of the latent energies of the chosen pairs. 

Crystals share the same collective frequency if they are part of the same harmonized group. Two crystals belong to the same group if they are directly harmonized with each other, or if they are linked through a sequence of intermediate harmonized crystals.

Among the collection, **t** crystals are designated as *focal* crystals. The artificer's goal is to select a set of pairs to harmonize such that all **t** focal crystals end up sharing the same collective frequency. The artificer may harmonize any of the non-focal crystals as part of the process if doing so requires less total latent energy.

Determine the minimum total latent energy required to ensure all focal crystals share a single collective frequency.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the identifiers of the focal crystals.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): indicating that crystal u and crystal v can be harmonized using w units of latent energy.
It is guaranteed that it is possible to make all focal crystals share the same collective frequency using some combination of the available pairs.

## Output

Print a single integer: the minimum total latent energy required.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, harmonizing the focal crystals 1, 2, and 3 by pairing each of them with the non-focal crystal 4 requires 1 + 1 + 1 = 3 units of energy. This is more efficient than harmonizing the focal crystals directly with each other (which would cost at least 4 units). In Example 3, there is only 1 focal crystal, so it already shares its own frequency and no harmonizations are needed, costing 0.
