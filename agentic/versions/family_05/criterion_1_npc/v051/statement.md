# Problem A — Archival Translation Initiative

Time limit: 5 s   Memory limit: 256 MB

## Description

A research institute has recovered **k** ancient manuscripts. To decipher them, they have hired **k** expert linguists and leased access to **k** specialized decoding algorithms. The linguists, manuscripts, and algorithms are all indexed from 1 to **k**.

A translation session requires exactly one linguist, one manuscript, and one algorithm. However, due to the varying dialects in the texts, the specific expertise of the linguists, and the parameters of the algorithms, only certain combinations will successfully produce a translation. The institute has completed preliminary testing and compiled a list of viable translation trios.

Your task is to determine if it is possible to form exactly **k** translation sessions such that every linguist is assigned to exactly one session, every manuscript is assigned to exactly one session, and every algorithm is utilized in exactly one session. If such a schedule is possible, you must also provide the assignments.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of entities of each type (linguists, manuscripts, and algorithms), and the total number of viable translation trios.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing a viable trio consisting of linguist **x**, manuscript **y**, and algorithm **z**. No trio is listed more than once.

## Output

If it is possible to form **k** valid translation sessions, print `YES` on the first line. Then, print **k** lines, each containing three integers `x y z` representing the linguist, manuscript, and algorithm for one chosen session. If there are multiple valid schedules, any one that uses every linguist, manuscript, and algorithm exactly once will be accepted. The sessions may be printed in any order.

If no such schedule is possible, print `NO`.

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

In Example 2, both viable trios require manuscript 1. This leaves manuscript 2 untranslated, so it is impossible to form 2 valid sessions.
