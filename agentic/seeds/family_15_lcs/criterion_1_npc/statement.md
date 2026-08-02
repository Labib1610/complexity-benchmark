# Problem A — Shared Motif Across Samples

Time limit: 5 s   Memory limit: 256 MB

## Description

You are given **k** genetic sequences, each a string of lowercase letters. A **shared motif** is a string that appears in every one of the sequences as a subsequence — that is, its letters occur in that same order within each sequence, though not necessarily consecutively.

Find a longest shared motif: report its length and one motif of that length.

## Input

The first line contains a single integer **k** (2 ≤ k ≤ 5).
Each of the next **k** lines contains one sequence: a non-empty string of lowercase English letters, length at most 20.

## Output

On the first line print the length of a longest shared motif.
On the second line print one shared motif of that length (any motif achieving the maximum length is accepted). If the maximum length is 0, the second line may be left blank.

## Examples

### Example 1

**Input**
```
3
abc
abc
abc
```

**Output**
```
3
abc
```

### Example 2

**Input**
```
3
abc
cab
bca
```

**Output**
```
1
a
```

### Example 3

**Input**
```
3
abc
a
dae
```

**Output**
```
1
a
```

## Note

In Example 2, no string of length 2 appears in order in all three sequences, but each single letter does; any one of them is a valid answer.
