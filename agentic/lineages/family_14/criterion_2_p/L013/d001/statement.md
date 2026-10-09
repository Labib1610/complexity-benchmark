# Problem B — Translation Consistency

Time limit: 2 s   Memory limit: 256 MB

## Description

A publisher is preparing a major international release. There are **n** distinct languages involved in their global operations (numbered 1 to **n**). 

To facilitate communication, the publisher can hire from a pool of **m** bilingual translators. Each translator works in both directions between exactly two specific languages and charges a fixed retainer fee. The pool of available translators is strictly non-redundant: it encompasses all languages, there are exactly **n − 1** translator options in total, and between any two languages, there is exactly one possible sequence of translators that can bridge them.

The upcoming book must be finalized in **t** specific target languages. To ensure editorial consistency, the publisher must hire a subset of translators such that a manuscript can be passed from any of the **t** target languages to any other of the **t** target languages, relying only on the hired translators (this may require passing through intermediate languages). 

Determine the minimum total retainer fee the publisher must pay to hire a valid subset of translators. Each hired translator's fee is paid exactly once, regardless of how many translation sequences they participate in.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the ids of the target languages.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): indicating a translator who bridges language **u** and language **v** for a fee of **w**. The available translators form the non-redundant structure described above.

## Output

Print a single integer: the minimum total retainer fee to ensure all target languages can inter-translate.

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

In Example 1, the target languages 1 and 4 can only be bridged through languages 2 and 3, so all three translators (fees 5+1+2 = 8) must be hired. In Example 2, there is only one target language, so no translators need to be hired.