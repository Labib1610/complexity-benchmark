# Problem B — System Configuration

Time limit: 2 s   Memory limit: 256 MB

## Description

A system must assemble **k** complete configurations. A configuration requires components from the following categories, each containing exactly **k** members:

- **k** primary modules (category X), numbered 1..k,
- **k** secondary modules (category Y), numbered 1..k,
- **k** access tokens (category Z), numbered 1..k.

A configuration consists of exactly one primary module, one secondary module, and one access token. You are given a list of allowed combinations `(x, y, z)`.

In this system **each primary module is bound to exactly one secondary module, and no two primary modules are bound to the same secondary module** — so the primary-to-secondary pairing is inherently fixed. The only thing left to decide is the access tokens.

Choose exactly **k** allowed combinations so that every primary module, every secondary module, and every access token is used in **exactly one** chosen configuration. Determine whether this is possible, and if so report one valid set of configurations.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the category size and the number of allowed combinations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), an allowed combination. No combination is listed more than once. For each primary module, every listed combination uses the same secondary module, and different primary modules use different secondary modules.

## Output

If a valid selection of **k** configurations exists, print `YES` on the first line, then print **k** lines, each containing the three members `x y z` of one chosen configuration (in any order). Any valid selection is accepted.

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

In Example 2 both primary modules' only allowed access token is 1, so token 2 can never be covered.
