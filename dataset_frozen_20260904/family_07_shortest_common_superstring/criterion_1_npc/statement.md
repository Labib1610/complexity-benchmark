# Problem A — Fragment Reassembly

Time limit: 5 s   Memory limit: 256 MB

## Description

A sequencing run produced **k** fragments, each a string of lowercase letters. You must reconstruct the shortest possible single string **S** such that **every** fragment appears in **S** as a contiguous substring.

Output any string of the shortest possible length that contains every fragment.

## Input

The first line contains a single integer **k** (1 ≤ k ≤ 16).
Each of the next **k** lines contains one fragment: a non-empty string of lowercase English letters, length at most 20. Fragments may repeat and one fragment may appear inside another.

## Output

Print a shortest string that contains every fragment as a contiguous substring. Any string of the minimum possible length that contains all fragments is accepted.

## Examples

### Example 1

**Input**
```
3
abc
bcd
cde
```

**Output**
```
abcde
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
abcdef
```

### Example 3

**Input**
```
1
hello
```

**Output**
```
hello
```

## Note

In Example 1, `abc`, `bcd`, and `cde` all occur inside `abcde`, which is the shortest such string. In Example 2 the fragments share no letters at their ends, so they must be concatenated; `abcdef` is the lexicographically smallest length-6 arrangement.
