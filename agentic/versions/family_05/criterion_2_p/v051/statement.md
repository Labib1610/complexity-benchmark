# Problem B — Translation Grants

Time limit: 2 s
Memory limit: 256 MB

## Description

An institute of antiquity is organizing a massive translation project. There are $k$ scholars, $k$ private archives, and $k$ ancient manuscripts to be translated. The institute has a list of $t$ funding proposals. Each proposal specifies a scholar, an archive, and a manuscript.

By long-standing decree, each scholar holds the exclusive key to exactly one private archive. Consequently, any proposal submitted by a specific scholar always lists their uniquely assigned archive. No two scholars have access to the same archive.

The institute must approve exactly $k$ proposals so that every scholar, every archive, and every manuscript is included exactly once. Determine if a valid selection of proposals exists, and if so, output the approved proposals.

## Input

The first line contains two integers $k$ and $t$ ($1 \le k \le 1200$, $0 \le t \le k \cdot k$): the number of each resource (scholars, archives, manuscripts) and the number of funding proposals.

Each of the following $t$ lines contains three integers $x$, $y$, and $z$ ($1 \le x, y, z \le k$) representing a proposal consisting of scholar $x$, archive $y$, and manuscript $z$. No proposal is listed more than once. For each scholar, every listed proposal specifies the same archive, and different scholars specify different archives.

## Output

If a valid set of $k$ proposals exists, print `YES` on the first line, then print $k$ lines, each containing the three integers $x$ $y$ $z$ of one approved proposal. The proposals may be printed in any order. Any valid set is accepted.

If no valid set exists, print `NO`.

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
