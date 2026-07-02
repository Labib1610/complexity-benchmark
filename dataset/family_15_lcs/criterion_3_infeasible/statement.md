# Problem C — No Shared Motif

Time limit: 1 s   Memory limit: 256 MB

## Description

You are given **k** genetic sequences, each a string of lowercase letters. A **shared motif** is a non-empty string that appears in every one of the sequences as a subsequence (its letters occur in that same order within each sequence, not necessarily consecutively).

In the input you are given, the sequences use **mutually disjoint sets of letters**: no letter occurs in more than one sequence. Because no single letter is present in all of them, there is no non-empty string that is a subsequence of every sequence.

Determine whether any non-empty shared motif exists.

## Input

The first line contains a single integer **k** (2 ≤ k ≤ 5).
Each of the next **k** lines contains one sequence: a non-empty string of lowercase English letters, length at most 2000. No letter appears in two different sequences.

## Output

Print a single line containing `NONE`, since no non-empty shared motif exists.

## Examples

### Example 1

**Input**
```
2
abc
def
```

**Output**
```
NONE
```

### Example 2

**Input**
```
3
ab
cd
ef
```

**Output**
```
NONE
```

## Note

Since the sequences share no letters at all, not even a single-letter motif can appear in all of them.
