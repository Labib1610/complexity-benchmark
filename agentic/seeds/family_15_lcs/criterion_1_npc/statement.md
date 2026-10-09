# Problem A — Shared Motif Across Samples

Time limit: 5 s   Memory limit: 256 MB

## Description

An archivist compares **k** transcripts, each a string of lowercase letters, and must find the longest sequence of letters that appears — in the same relative order, though not necessarily contiguously — inside **every** transcript. A common ordered thread of length L must be embeddable as a subsequence of all k transcripts at once. Formatting and letter frequencies are irrelevant; only the ordered content shared across all transcripts matters. Aligning any two transcripts is easy, but a thread common to all k at once is the hard part, since extending it to satisfy one transcript can break another. Report a longest such common ordered thread (or its length, per the output format).

## Input

The first line contains a single integer **k** (3 ≤ k ≤ 5).
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
