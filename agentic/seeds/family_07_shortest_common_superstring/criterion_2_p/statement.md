# Problem B — Two-Fragment Merge

Time limit: 1 s   Memory limit: 256 MB

## Description

You are given exactly **two** fragments, each a string of lowercase letters. Reconstruct the shortest possible single string **S** such that both fragments appear in **S** as contiguous substrings.

Among all strings of the shortest possible length that contain both fragments, output the one that is lexicographically smallest.

## Input

The first line contains the first fragment.
The second line contains the second fragment.
Each fragment is a non-empty string of lowercase English letters of length at most 500000.

## Output

Print the shortest string that contains both fragments as contiguous substrings. If both possible lengths are equal, print the lexicographically smallest such string.

## Examples

### Example 1

**Input**
```
abcde
cdefg
```

**Output**
```
abcdefg
```

### Example 2

**Input**
```
abc
xyz
```

**Output**
```
abcxyz
```

### Example 3

**Input**
```
hello
hello
```

**Output**
```
hello
```

## Note

In Example 1, the end of `abcde` and the start of `cdefg` share `cde`, so they can be merged into `abcdefg`.
