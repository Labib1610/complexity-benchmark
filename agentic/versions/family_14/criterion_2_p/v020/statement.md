# Reassembling the Incantation

Time limit: 2 s   Memory limit: 256 MB

## Description

An ancient papyrus scroll has shattered into **n** fragments, numbered 1 through **n**. Researchers have identified exactly **m** valid alignments where a specific pair of fragments can be permanently fused back together. Fusing a given pair requires a certain amount of magical resin.

The identified alignments possess a strict structural property: if all **m** possible fusions were performed, all **n** fragments would form a single intact scroll, and there would be exactly one sequence of fusions physically linking any two fragments. 

Among the fragments, **t** specific fragments contain the scattered syllables of a critical incantation. To safely read the incantation, all **t** of these fragments must end up in the same contiguous fused piece. They do not need to be fused directly to one another; they may be linked through other fragments that do not contain parts of the incantation.

Find the minimum total amount of resin required to perform a chosen set of these fusions so that all **t** incantation fragments are physically joined together in a single assembly.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the numbers of the fragments that contain the incantation.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), meaning that fragments **u** and **v** can be fused using **w** milligrams of resin. The valid alignments follow the structural property described above.

## Output

Print a single integer: the minimum total amount of resin required to fuse the necessary fragments.

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

In Example 1, the incantation fragments 1 and 4 can only be joined by fusing 1 to 2, 2 to 3, and 3 to 4. Therefore, all three fusions must be performed, requiring 5 + 1 + 2 = 8 milligrams of resin. In Example 2, there is only one incantation fragment, so no fusions are needed.
