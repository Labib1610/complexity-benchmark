# Component Assembly

Time limit: 2 s
Memory limit: 256 MB

## Description

You are managing the assembly of a complex product consisting of **n** atomic parts (numbered 1 to **n**). Initially, each part is completely separate.

You have a list of **m** possible fusion procedures. Each procedure can merge the component containing part **u** with the component containing part **v**. Executing a procedure consumes a specific amount of energy, **w**. The list of procedures is minimal and complete: there are exactly **m** = **n** − 1 procedures available, and if you were to execute all of them, all **n** parts would be merged into a single massive component.

Quality control has identified **t** critical parts that must be fused together. Your task is to select a subset of the available fusion procedures such that, when executed, all **t** critical parts end up in the same component. You do not care about the other parts, though they may end up in the same component as a byproduct.

What is the minimum total energy (the sum of the costs of the selected procedures) required to achieve this?

## Input

The first line contains three integers **n**, **m**, and **t**. The number of parts **n** (1 ≤ **n** ≤ 200000). The number of available procedures **m** is always exactly **n** − 1. The number of critical parts **t** (1 ≤ **t** ≤ **n**).
The second line contains **t** distinct integers: the identifiers of the critical parts.
Each of the next **m** lines contains three integers **u**, **v**, and **w**. These denote a fusion procedure between parts **u** and **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**) requiring **w** energy (1 ≤ **w** ≤ 1000000).

## Output

Print a single integer: the minimum total energy required.

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