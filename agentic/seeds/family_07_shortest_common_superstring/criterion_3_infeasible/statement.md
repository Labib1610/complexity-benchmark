# Problem C — Forbidden Pattern

Time limit: 1 s   Memory limit: 256 MB

## Description

You are given **k** fragments, each a string of lowercase letters, and a forbidden string **F**. The goal would be to build a single string that contains every fragment as a contiguous substring but does **not** contain **F** anywhere.

In the input you are given, **at least one fragment already contains F as a contiguous substring**. Any string that contains that fragment must also contain F, so no valid result can exist.

Report the smallest index of a fragment that contains **F** as a contiguous substring.

## Input

The first line contains a single integer **k** (1 ≤ k ≤ 100000).
Each of the next **k** lines contains one fragment: a non-empty string of lowercase English letters.
The final line contains the forbidden string **F** (lowercase letters, non-empty).
The total length of all fragments is at most 1000000. It is guaranteed that at least one fragment contains F.

## Output

Print a single integer: the smallest index **i** (1-based) such that fragment **i** contains **F** as a contiguous substring.

## Examples

### Example 1

**Input**
```
3
world
hello
abcde
ell
```

**Output**
```
2
```

### Example 2

**Input**
```
2
programming
testing
gram
```

**Output**
```
1
```

## Note

In Example 1, `ell` appears inside `hello` (fragment 2), so fragment 2 forces the forbidden pattern to appear.
