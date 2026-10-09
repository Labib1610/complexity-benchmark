# Problem B — Secure Communications (Fixed Aliases)

Time limit: 2 s   Memory limit: 256 MB

## Description

A mission must establish **k** complete transmission protocols. There are three groups, each with exactly **k** elements:

- **k** agents (group X), numbered 1..k,
- **k** aliases (group Y), numbered 1..k,
- **k** frequencies (group Z), numbered 1..k.

A protocol consists of exactly one agent, one alias, and one frequency. You are given a list of allowed combinations `(x, y, z)`.

In this mission **each agent is assigned exactly one alias, and no two agents share the same alias** — so the agent-to-alias pairing is already fixed. The only thing left to decide is the frequencies.

Choose exactly **k** allowed combinations so that every agent, every alias, and every frequency is used in **exactly one** chosen protocol. Determine whether this is possible, and if so report one valid set of protocols.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the group size and the number of allowed combinations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), an allowed combination. No combination is listed more than once. For each agent, every listed combination uses the same alias, and different agents use different aliases.

## Output

If a valid selection of **k** protocols exists, print `YES` on the first line, then print **k** lines, each containing the three elements `x y z` of one chosen protocol (in any order). Any valid selection is accepted.

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

This is the same protocol-establishment problem as Problem A. The only difference is the promise that each agent's alias is fixed and all distinct, which leaves only the frequency choice. In Example 2 both agents' only allowed frequency is 1, so frequency 2 can never be used.
