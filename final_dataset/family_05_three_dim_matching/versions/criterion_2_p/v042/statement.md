# Problem B — CRISPR Gene Editing

Time limit: 2 s   Memory limit: 256 MB

## Description

A genetic engineering lab must run **k** independent gene-editing trials. There are three groups of components, each containing exactly **k** items:

- **k** protein enzymes (group X), numbered 1..k,
- **k** guide RNAs (group Y), numbered 1..k,
- **k** cell cultures (group Z), numbered 1..k.

A trial consists of exactly one protein enzyme, one guide RNA, and one cell culture. You are given a list of viable combinations `(x, y, z)`.

In this phase of the experiment, **each protein enzyme is already irreversibly bonded to exactly one guide RNA, and no two protein enzymes share the same guide RNA** — so the enzyme-to-RNA pairing is already fixed. The only thing left to decide is the cell cultures.

Choose exactly **k** viable combinations so that every protein enzyme, every guide RNA, and every cell culture is used in **exactly one** chosen trial. Determine whether this is possible, and if so report one valid set of trials.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the group size and the number of viable combinations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), a viable combination. No combination is listed more than once. For each protein enzyme, every listed combination uses the same guide RNA, and different protein enzymes use different guide RNAs.

## Output

If a valid selection of **k** trials exists, print `YES` on the first line, then print **k** lines, each containing the three components `x y z` of one chosen trial (in any order). Any valid selection is accepted.

If no valid selection exists, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 1 2
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
2 2 1
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

In Example 2, both protein enzymes' only viable cell culture is 1, so cell culture 2 can never be covered.
