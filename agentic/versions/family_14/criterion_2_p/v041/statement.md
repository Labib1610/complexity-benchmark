# Priority Site Connectivity

Time limit: 2 s   Memory limit: 256 MB

## Description

A campus manages **n** facilities (numbered 1 to n). You are provided with a list of **m** potential data conduits that can be activated between certain pairs of facilities. Each conduit has a known activation fee.

The architectural layout of these potential conduits is strictly minimal: there are exactly **m = n − 1** conduits available, and between any two facilities, there exists exactly one valid sequence of conduits to transit without traversing any facility more than once.

A specific group of **t** facilities are designated as **mandatory**. You must choose a subset of the available conduits to activate such that every mandatory facility can exchange data with every other mandatory facility. Data may be relayed through non-mandatory facilities.

Calculate the lowest possible total activation fee required to ensure all mandatory facilities are integrated into a single communicating group.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the identifiers of the mandatory facilities.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), meaning there is a potential conduit between facility **u** and facility **v** with an activation fee of **w**. The layout of the conduits is guaranteed to follow the properties described above.

## Output

Print a single integer: the lowest total activation fee to ensure all mandatory facilities can communicate with each other.

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

In Example 1, the mandatory facilities 1 and 4 must exchange data. This is only possible by routing through facilities 2 and 3, requiring all three conduits to be activated for a total fee of 5 + 1 + 2 = 8.
In Example 2, there is only one mandatory facility, so no conduits need to be activated.
