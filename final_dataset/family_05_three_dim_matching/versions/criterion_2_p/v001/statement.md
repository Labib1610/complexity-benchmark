# Problem B — Flight Roster

Time limit: 2 s   Memory limit: 256 MB

## Description

A project must assemble **k** complete flight missions. There are three categories, each with exactly **k** elements:

- **k** pilots, numbered 1..k,
- **k** aircraft, numbered 1..k,
- **k** routes, numbered 1..k.

A mission consists of exactly one pilot, one aircraft, and one route. You are given a list of allowed combinations `(x, y, z)`.

In this project **each pilot is certified on exactly one aircraft, and no two pilots share the same aircraft** — so the pilot-to-aircraft pairing is already fixed. The only thing left to decide is the routes.

Choose exactly **k** allowed combinations so that every pilot, every aircraft, and every route is used in **exactly one** chosen mission. Determine whether this is possible, and if so report one valid set of missions.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the category size and the number of allowed combinations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), an allowed combination. No combination is listed more than once. For each pilot, every listed combination uses the same aircraft, and different pilots use different aircraft.

## Output

If a valid selection of **k** missions exists, print `YES` on the first line, then print **k** lines, each containing the three members `x y z` of one chosen mission (in any order). Any valid selection is accepted.

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

In Example 2 both pilots' only allowed route is 1, so route 2 can never be covered.
