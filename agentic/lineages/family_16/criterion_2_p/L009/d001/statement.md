# Problem B — Visual Effects Pipeline

Time limit: 1 s   Memory limit: 256 MB

## Description

A studio is rendering **j** visual effects. Each effect consists of exactly 2 components: a geometry phase and a lighting phase. For each effect, you are given its required geometry time and its required lighting time.

You must arrange the **j** effects into a single sequence. Once you choose the sequence, an automated analyzer will evaluate the pipeline by selecting a split point **k** (where 1 ≤ k ≤ j). The total time for a specific split point **k** is calculated as the sum of:
- The geometry times of all effects from position 1 up to position **k** (inclusive).
- The lighting times of all effects from position **k** up to position **j** (inclusive).

The analyzer will always choose the split point **k** that results in the maximum possible total time for your sequence. 

Your goal is to order the effects such that this worst-case total time is minimized. Choose the sequence of effects optimally and report the minimum possible value of the analyzer's maximum total time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains exactly 2 integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the geometry time and the lighting time for an effect.

## Output

Print a single integer: the smallest possible worst-case total time.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 1, if we arrange the effects in the input order (let's call them A, B, C):
- For k = 1: geometry of A (3) + lighting of A, B, C (2 + 4 + 3) = 12.
- For k = 2: geometry of A, B (3 + 2) + lighting of B, C (4 + 3) = 12.
- For k = 3: geometry of A, B, C (3 + 2 + 1) + lighting of C (3) = 9.
The analyzer's maximum total time for this arrangement is 12. By optimally reordering the sequence, the worst-case total time is minimized to 10.

In Example 2, there is only 1 effect. The only valid split point is k = 1, giving a total time of 5 (geometry) + 3 (lighting) = 8.