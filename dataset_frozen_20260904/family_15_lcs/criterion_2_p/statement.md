# Problem B — Shared Motif of Two Samples

Time limit: 2 s   Memory limit: 256 MB

## Description

You are given **k** genetic sequences, each a string of lowercase letters. A **shared motif** is a string that appears in every one of the sequences as a subsequence — that is, its letters occur in that same order within each sequence, though not necessarily consecutively.

Find a longest shared motif: report its length and one motif of that length.

## Input

The first line contains a single integer **k** (k = 2).
Each of the next **k** lines contains one sequence: a non-empty string of lowercase English letters, length at most 2000.

## Output

On the first line print the length of a longest shared motif.
On the second line print one shared motif of that length (any motif achieving the maximum length is accepted). If the maximum length is 0, the second line may be left blank.

## Examples

### Example 1

**Input**
```
2
abcbdab
bdcaba
```

**Output**
```
4
bcba
```

### Example 2

**Input**
```
2
abc
def
```

**Output**
```
0

```

### Example 3

**Input**
```
2
axbyc
abc
```

**Output**
```
3
abc
```

## Note

This is the same shared-motif (longest common subsequence) problem as Problem A. The only difference is that here there are exactly **two** sequences, which makes an efficient exact solution possible. In Example 1, `bcba` appears in order in both sequences; several length-4 motifs exist and any of them is accepted.
