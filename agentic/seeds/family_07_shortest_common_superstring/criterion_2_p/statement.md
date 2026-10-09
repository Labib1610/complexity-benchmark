# Problem B — Two-Fragment Merge

Time limit: 1 s   Memory limit: 256 MB

## Description

A reassembly stage receives **k** fragments of lowercase letters and must produce the shortest single text containing every fragment as a contiguous block. Here the instance is small in the number of fragments, so the best way to overlap them can be resolved directly rather than by weighing exponentially many orderings. Output any shortest text that contains all fragments as substrings.

## Input

The first line contains a single integer **k** (k = 2).
Each of the next **k** lines contains one fragment: a non-empty string of lowercase English letters of length at most 500000.

## Output

Print a shortest string that contains every fragment as a contiguous substring. Any string of the minimum possible length that contains all fragments is accepted.

## Examples

### Example 1

**Input**
```
2
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
2
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
2
abcdef
cde
```

**Output**
```
abcdef
```

## Note

This is the same shortest-superstring problem as Problem A. The only difference is that there are exactly **two** fragments, which makes an efficient exact solution possible. In Example 1 the end of `abcde` overlaps the start of `cdefg` on `cde`, giving `abcdefg`. In Example 3 the second fragment already occurs inside the first, so the first fragment alone is the answer.
