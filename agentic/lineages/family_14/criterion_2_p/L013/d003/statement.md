# Problem B — Translation Consistency

Time limit: 2 s   Memory limit: 256 MB

## Description

An international publisher operates across **n** distinct languages (numbered 1 through **n**). 

The publisher can retain professionals from a pool of **m** bilingual translators. Each translator provides bidirectional conversion between a specific pair of languages for a fixed retainer fee. The pool of available translators connects all **n** languages together. To prevent redundancy, the pool is minimally connected: the removal of any single translator from the pool would isolate some languages from others.

A forthcoming publication must be prepared in **t** priority languages. The publisher needs to retain a subset of translators such that a text can be converted from any of the **t** priority languages to any other of the **t** priority languages using exclusively the retained professionals. Note that these conversions may route through intermediate languages, which do not themselves need to be priority languages.

Calculate the minimum total retainer fee required to retain a valid subset of translators. The fee for each retained translator is paid exactly once, independent of the number of conversion routes they support.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the identifiers of the priority languages.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): indicating a translator who bridges language **u** and language **v** for a fee of **w**. The listed translators form the minimally connected network described above.

## Output

Print a single integer: the minimum total retainer fee to ensure all priority languages can inter-translate.

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

In Example 1, the priority languages 1 and 4 can only be bridged through languages 2 and 3, so all three translators (fees 5+1+2 = 8) must be retained. In Example 2, there is only one priority language, so no translators need to be retained.