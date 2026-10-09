# Problem A — Meal Deals

Time limit: 5 s   Memory limit: 256 MB

## Description

A restaurant must design **k** complete meal deals. There are three categories, each with exactly **k** dishes:

- **k** appetizers (category X), numbered 1..k,
- **k** main courses (category Y), numbered 1..k,
- **k** desserts (category Z), numbered 1..k.

A meal deal consists of exactly one appetizer, one main course, and one dessert. Only certain combinations taste good together; you are given a list of approved combinations `(x, y, z)`.

Choose exactly **k** approved combinations so that every appetizer, every main course, and every dessert is used in **exactly one** chosen meal deal.

Determine whether this is possible, and if so report one valid set of meal deals.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the category size and the number of approved combinations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), an approved combination. No combination is listed more than once.

## Output

If a valid selection of **k** meal deals exists, print `YES` on the first line, then print **k** lines, each containing the three dishes `x y z` of one chosen meal deal. Any selection in which every appetizer, main course, and dessert is used exactly once is accepted; the meal deals may be printed in any order.

If no valid selection exists, print `NO`.

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

In Example 2, both approved combinations use main course 1, so main course 2 can never be covered.
