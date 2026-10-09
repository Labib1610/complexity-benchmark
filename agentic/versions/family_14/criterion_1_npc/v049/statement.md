# Universal Translation

Time limit: 5 s   Memory limit: 256 MB

## Description
A galactic federation catalogs **n** distinct languages, numbered 1 to **n**. Across the galaxy, there are **m** freelance interpreters. Every interpreter has mastered exactly two languages and requires a specific, one-time retainer fee to join your staff. Once on staff, an interpreter can facilitate any number of conversations between their two mastered languages. Furthermore, chains of interpreters can be formed. If one interpreter bridges language A and language X, and another bridges X and B, then a message originally in A can be understood by someone speaking B.

You are organizing an interstellar summit. A specific set of **t** languages has been designated as the official summit dialects. 

Your task is to select and hire a subset of the available interpreters such that any delegate speaking one of the official dialects can communicate with delegates speaking any of the other official dialects. Determine the lowest possible total sum of retainer fees required to achieve this.

## Input
The first line contains three integers **n**, **m**, and **t** (1 ≤ **t** ≤ 10, 1 ≤ **n** ≤ 100, 0 ≤ **m** ≤ **n**·(**n**−1)/2).
The second line contains **t** distinct integers: the IDs of the official dialects.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000) detailing an available interpreter who bridges languages **u** and **v** for a retainer fee of **w**.
It is guaranteed that the available pool of interpreters is capable of mutually connecting all official dialects.

## Output
Output a single integer representing the minimum total retainer fee required to establish mutual intelligibility among all official dialects.

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
In Example 1, using language 4 as an intermediate pivot (hiring interpreters for 1-4, 2-4, and 3-4 at a total cost of 1+1+1 = 3) is cheaper than hiring interpreters to directly connect the three official dialects (which would cost 4). In Example 3, there is only one official dialect, so no interpreters need to be hired.
