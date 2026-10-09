# Reassembling the Incantation

Time limit: 2 s   Memory limit: 256 MB

## Description

An ancient papyrus scroll has shattered into **n** fragments, numbered 1 through **n**. Researchers have identified exactly **m** possible alignments where a specific pair of fragments can be permanently fused back together. Fusing a pair requires a certain amount of magical resin.

You are tasked with selecting a subset of fusions to execute. With $2^m$ possible subsets of fusions to consider, you must carefully optimize your choice. Your objective is to minimize the total resin consumed, while satisfying a strict connectivity requirement.

Among the fragments, exactly **t** specific fragments contain the scattered syllables of a critical incantation. Your chosen subset of fusions must physically join all **t** of these fragments into a single contiguous assembly. They do not need to be fused directly to one another; they may be linked indirectly through any number of other fragments in your assembly.

The identified alignments possess a specific structural property: if all **m** possible fusions were performed, all **n** fragments would form a single intact scroll, and there would be exactly one sequence of fusions physically linking any two fragments.

Evaluate the space of possible fusion subsets and output the minimum total amount of resin required to form a valid assembly.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the numbers of the fragments that contain the incantation.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that fragments **u** and **v** can be joined for a cost of **w** milligrams of resin. The valid alignments follow the structural property described above.

## Output

Print a single integer: the minimum total amount of resin required to fuse a valid subset of fragments.

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

In Example 1, out of the $2^3 = 8$ possible subsets of fusions, the only subset that successfully connects the incantation fragments 1 and 4 is the one containing all three fusions. Therefore, all three fusions must be performed, requiring 5 + 1 + 2 = 8 milligrams of resin. 

In Example 2, there is only one incantation fragment. The empty subset of fusions is valid, requiring 0 resin.
