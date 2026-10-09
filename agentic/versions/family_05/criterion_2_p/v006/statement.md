# Problem B — Daily Production Schedule

Time limit: 2 s   Memory limit: 256 MB

## Description

A manufacturing plant must schedule its daily operations by assembling **k** complete production crews. The plant has three sets of resources, each with exactly **k** members:

- **k** operators, numbered 1..k,
- **k** assembly stations, numbered 1..k,
- **k** shifts, numbered 1..k.

A crew consists of exactly one operator, one assembly station, and one shift. You are given a list of permitted combinations `(x, y, z)` based on union rules and safety certifications.

Because of strict certification requirements, **each operator is certified on exactly one assembly station, and no two operators are certified on the same station** — so the operator-to-station pairing is predetermined. The only scheduling task left is to assign the shifts.

Choose exactly **k** permitted combinations so that every operator, every assembly station, and every shift is scheduled in **exactly one** chosen crew. Determine whether a valid daily schedule is possible, and if so report one valid set of crews.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the number of resources in each group and the number of permitted combinations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), a permitted combination. No combination is listed more than once. For each operator, every listed combination uses the same assembly station, and different operators use different stations.

## Output

If a valid selection of **k** crews exists, print `YES` on the first line, then print **k** lines, each containing the three members `x y z` of one chosen crew (in any order). Any valid selection is accepted.

If no valid schedule exists, print `NO`.

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

This is the same schedule-assembly problem as Problem A. The only difference is the promise that each operator's assembly station is fixed and all distinct, which leaves only the shift choice and makes an efficient exact schedule possible. In Example 2 both operators' only permitted shift is 1, so shift 2 can never be covered.
