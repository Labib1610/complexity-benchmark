# Thermal Stabilization Network

Time limit: 2 s   Memory limit: 256 MB

## Description

An orbital research station is composed of **n** distinct sectors, numbered 1 through **n**. A specific subset of **t** sectors are designated as critical and must be synchronized for thermal stability. The station's engineers have proposed **m** potential thermal conduits. Each conduit can bridge a specific pair of sectors and requires a certain amount of energy to keep active.

Your objective is to select a subset of these proposed conduits to activate such that every critical sector can exchange thermal energy with every other critical sector (this exchange can occur directly or be relayed through any number of intermediate sectors). You must find the absolute minimum total activation energy required to accomplish this.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ **n** ≤ 200000, **m** = **n** - 1, 1 ≤ **t** ≤ **n**).

The second line provides **t** distinct integers representing the identifiers of the critical sectors.

The subsequent **m** lines each contain three integers **u**, **v**, and **w**. These values describe a potential conduit between sector **u** and sector **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**) that costs **w** energy to activate (1 ≤ **w** ≤ 1000000). It is guaranteed that if all **m** proposed conduits were activated, all **n** sectors would be fully interconnected in a single thermal network.

## Output

Print a single integer indicating the minimum total energy required to ensure all critical sectors are thermally linked.

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

In Example 1 the critical sectors 1 and 4 are linked only through 2 and 3, so all three conduits (5+1+2 = 8) are needed. In Example 2 there is one critical sector, so no conduits are needed to link the critical sectors.