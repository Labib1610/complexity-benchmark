# Problem B — Shared Motif of Two Samples

Time limit: 2 s   Memory limit: 256 MB

## Description

You are given **two** genetic sequences, each a string of lowercase letters. A **shared motif** is a string that appears in both sequences as a subsequence — its letters occur in that same order within each sequence, though not necessarily consecutively.

Find a longest shared motif: report its length and the motif itself.

## Input

The first line contains the first sequence.
The second line contains the second sequence.
Each sequence is a non-empty string of lowercase English letters of length at most 2000.

## Output

On the first line print the length of a longest shared motif.
On the second line print the longest shared motif; if several share the maximum length, print the lexicographically smallest one. If the maximum length is 0, the second line may be left blank.

## Examples

### Example 1

**Input**
```
abcde
ace
```

**Output**
```
3
ace
```

### Example 2

**Input**
```
abc
cba
```

**Output**
```
1
a
```

### Example 3

**Input**
```
hello
hello
```

**Output**
```
5
hello
```

## Note

In Example 2, each single letter is shared but no length-2 string appears in order in both; the lexicographically smallest single letter is `a`.
