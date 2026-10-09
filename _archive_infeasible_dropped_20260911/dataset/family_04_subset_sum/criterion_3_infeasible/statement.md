# Problem C — Budget Selection: Certify Impossibility

Time limit: 2 s   Memory limit: 256 MB

## Description

A store offers **n** items for purchase. Item **i** has a positive cost. You are given a target budget **T**.

For every input in this problem it is **guaranteed that no group of items has a total cost of exactly T** — the target is impossible to hit. Your job is not to search for a group; it is to **prove why it is impossible** by printing a short certificate that can be checked directly against the input.

Exactly one of the following two reasons always applies. Print the one that holds:

- **The target is larger than everything combined.** If T is strictly greater than the sum of all item costs, then no group (not even all items together) can reach it.
  Print a single line: `SUM`

- **A common divisor rules it out.** If there is an integer d ≥ 2 that divides every item cost but does **not** divide T, then every possible group total is a multiple of d while T is not, so T can never be reached.
  Print a single line: `MOD d` (replace `d` with such a divisor).

If both happen to apply, either certificate is accepted.

## Input

The first line contains a single integer **n** (1 ≤ n ≤ 60).
The second line contains **n** integers, the item costs, each between 1 and 1 000 000 000.
The third line contains a single integer **T** (0 ≤ T ≤ 100 000 000 000).

## Output

Print exactly one certificate line, either

```
SUM
```

or

```
MOD d
```

where `d` is an integer ≥ 2 that divides every cost but not T.

## Examples

### Example 1

**Input**
```
3
2 4 6
9
```

**Output**
```
MOD 2
```

### Example 2

**Input**
```
3
5 10 15
100
```

**Output**
```
SUM
```

## Note

In Example 1 every cost is even but 9 is odd, so no group of even numbers can total 9; `d = 2` is a valid certificate. In Example 2 the three costs total 30, which is less than the target 100, so the target is unreachable and `SUM` is the certificate.
