# Problem A — Synthetic Organism Protocol

Time limit: 5 s   Memory limit: 256 MB

## Description

A laboratory is designing a protocol for a synthetic biology experiment. The protocol requires executing exactly **k** distinct parallel reactions. The laboratory has prepared three distinct categories of resources, each containing exactly **k** items:

- **k** enzyme variants (identified by integers 1 through k)
- **k** substrate compounds (identified by integers 1 through k)
- **k** thermal profiles (identified by integers 1 through k)

A single reaction consumes exactly one enzyme variant, one substrate compound, and one thermal profile. However, due to complex biochemical dependencies, only specific combinations of these three resources will successfully react. You have a catalog of all viable resource combinations `(e, s, p)`.

To ensure the integrity of the experimental data, the overall protocol must utilize every single enzyme variant, every substrate compound, and every thermal profile in **exactly one** reaction. This means you must select exactly **k** viable combinations from the catalog such that no resource from any category is left unused or used more than once.

Determine whether it is possible to formulate a valid protocol, and if so, report the combinations to be used.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of items in each resource category, and the total number of viable combinations in the catalog.
Each of the next **t** lines contains three integers **e**, **s**, **p** (1 ≤ e, s, p ≤ k), representing a viable combination of enzyme **e**, substrate **s**, and thermal profile **p**. No combination is listed more than once in the catalog.

## Output

If a valid protocol of **k** reactions exists, print `YES` on the first line. Then, print **k** lines, each containing the three integers `e s p` of a chosen combination. Any selection that uses every enzyme, substrate, and thermal profile exactly once will be accepted. You may print the chosen combinations in any order.

If no valid protocol exists, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 1 2
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```

## Note

In Example 2, both viable combinations require substrate 1. Consequently, substrate 2 can never be utilized, making a valid protocol impossible.
