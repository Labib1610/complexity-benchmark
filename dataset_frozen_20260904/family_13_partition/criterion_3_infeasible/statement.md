# Problem C — Balanced Machines: Certify Impossibility

Time limit: 2 s   Memory limit: 256 MB

## Description

There are **n** tasks; task **i** takes **d[i]** units of time. Two identical machines are available, and each task must be assigned to exactly one of them. You would like to split the tasks so that the **total time on each machine is equal**.

For every input in this problem it is **guaranteed that no equal split exists**. Your job is not to search for a split; it is to **prove why one is impossible** by printing a short certificate that can be checked directly against the input.

Exactly one of the following three reasons always applies. Print the one that holds:

- **The total is odd.** Two equal whole-number totals must sum to an even number, so an odd total can never be split.
  Print a single line: `ODD`

- **A common divisor rules it out.** If there is an integer d ≥ 2 that divides every duration but does **not** divide half of the total, then every possible machine total is a multiple of d while the required half is not, so no equal split can exist.
  Print a single line: `MOD d` (replace `d` with such a divisor).

- **One task is too long.** If some single task takes strictly more than half of the total time, the machine holding it already exceeds half and can never be balanced.
  Print a single line: `MAX`

If more than one reason applies, any valid certificate is accepted.

## Input

The first line contains a single integer **n** (1 ≤ n ≤ 100000).
The second line contains **n** integers **d[1] … d[n]** (1 ≤ d[i] ≤ 1 000 000 000), the task durations.

## Output

Print exactly one certificate line: `ODD`, or `MOD d` (with an integer d ≥ 2 that divides every duration but not half the total), or `MAX`.

## Examples

### Example 1

**Input**
```
3
1 2 4
```

**Output**
```
ODD
```

### Example 2

**Input**
```
3
1 1 10
```

**Output**
```
MAX
```

## Note

In Example 1 the total is 7, which is odd, so `ODD` is the certificate. In Example 2 the total is 12, so half is 6; task 3 alone takes 10, which is more than 6, so the machine holding it can never be balanced and `MAX` is the certificate. Any single valid certificate is accepted.
