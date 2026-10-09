# Problem C — Shared Motif: Certify Impossibility

Time limit: 2 s   Memory limit: 256 MB

## Description

You are given **k** genetic sequences, each a string of lowercase letters. A **shared motif** is a non-empty string that appears in every one of the sequences as a subsequence.

For every input in this problem it is **guaranteed that no non-empty shared motif exists**. Your job is not to search; it is to **prove** the impossibility with a certificate that can be checked directly against the input.

A non-empty shared motif would have to start with some single letter that appears in *all* k sequences. So it is enough to show that **no single letter is common to every sequence**. Because any such letter would in particular have to appear in the **first** sequence, you only need to account for the distinct letters of sequence 1: for each of them, name a sequence that does **not** contain it.

Print the certificate as follows:

- First line: the word `BLOCK`.
- Then one line for each **distinct letter `c` that appears in sequence 1**: print `c j`, where **j** (2 ≤ j ≤ k) is the index of a sequence that does not contain the letter `c`.

This proves that every letter of sequence 1 is missing from some sequence, so no letter is shared by all, and therefore no non-empty shared motif exists.

## Input

The first line contains a single integer **k** (2 ≤ k ≤ 5).
Each of the next **k** lines contains one sequence: a non-empty string of lowercase English letters, length at most 2000.

## Output

Print `BLOCK` on the first line, then, for every distinct letter of sequence 1, a line `c j` naming a sequence j (2 ≤ j ≤ k) that does not contain letter c.

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
BLOCK
a 2
b 2
c 2
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
BLOCK
a 2
b 2
```

## Note

In Example 1 sequence 1 is `abc`; none of `a`, `b`, `c` appears in sequence 2 (`def`), so pairing each with sequence 2 proves no letter is shared. In Example 2 letters `a` and `b` are both absent from sequence 2 (`cd`).
