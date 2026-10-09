# Problem B — Botanical Showcase Logistics

Time limit: 2 s   Memory limit: 256 MB

## Description
A botanical research institute is preparing a high-profile public showcase. The gallery features $q$ rare flora specimens, which are assigned catalog numbers $1$ through $q$, and $q$ climate-controlled display capsules, assigned catalog numbers $q+1$ through $2q$.

Because of precise atmospheric and soil requirements, a specimen can only survive in a capsule if their environmental profiles are mutually compatible. You are given a database of all known compatible specimen-capsule combinations.

The exhibition's design mandates that every single specimen must be placed on display, and simultaneously, every capsule must be utilized to maintain the gallery's architectural symmetry. Furthermore, to ensure plant health, a capsule can house no more than one specimen at a time, and a specimen cannot be split across multiple capsules.

Determine if an arrangement satisfying all these conditions is possible. If it can be achieved, provide the exact list of placements. Otherwise, state that the showcase cannot be fully assembled under the current compatibility constraints.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of specimens (which is also the number of capsules) and the number of known compatible combinations, respectively.
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that specimen $a$ can be safely housed in capsule $b$.

## Output
If a valid showcase arrangement is possible, print `YES` on the first line, followed by $q$ lines each containing the two catalog numbers of a paired specimen and capsule in your arrangement. If it is impossible, print `NO`.

## Example 1

### Input
```text
3 4
1 4
1 5
2 5
3 6
```

### Output
```text
YES
1 4
2 5
3 6
```

## Example 2

### Input
```text
2 2
1 3
2 3
```

### Output
```text
NO
```
