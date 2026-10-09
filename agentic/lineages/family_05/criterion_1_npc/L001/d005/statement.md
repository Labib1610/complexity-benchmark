# Problem A — Harmonic Resonance

Time limit: 5 s   Memory limit: 256 MB

## Description

You are tuning a complex instrument that requires installing a set of harmonic resonators. You have a catalog of **t** available resonator models. The instrument operates on a fundamental frequency index **k**.

Each resonator model is characterized by three integer parameters: a frequency multiplier, a phase shift, and an amplitude scale. For each available model, these three parameters are integers between 1 and **k** inclusive.

Your goal is to install exactly **k** resonator models from the catalog into the instrument. 

To achieve perfect harmonic resonance, the installed set must maximize the diversity of its parameters. Specifically, let $U_f$ be the set of distinct frequency multipliers present among the installed resonators, $U_p$ be the set of distinct phase shifts present, and $U_a$ be the set of distinct amplitude scales present. The installation is successful if and only if the sum of the sizes of these three sets reaches its theoretical maximum:

$|U_f| + |U_p| + |U_a| = 3k$

Determine if it is possible to select exactly **k** resonators to achieve this. If it is, output the parameters of the chosen resonators.

## Input

The first line specifies the fundamental index **k** and the catalog size **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k).

The following **t** lines each contain three integers representing the frequency multiplier, phase shift, and amplitude scale of a resonator model. All parameter values are between 1 and **k**. No two resonator models in the catalog have the exact same combination of all three parameters.

## Output

If a successful installation of exactly **k** resonators is possible, print `YES` on the first line. Following this, print **k** lines, each containing the three parameters of an installed resonator model. If multiple valid installations exist, any of them is acceptable, and the models may be printed in any order.

If no such installation is possible, print `NO`.

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

In Example 2, there are only two available resonator models, so both must be selected to install exactly 2. The set of distinct frequency multipliers is $\{1, 2\}$ ($|U_f| = 2$), the set of distinct phase shifts is $\{1\}$ ($|U_p| = 1$), and the set of distinct amplitude scales is $\{1, 2\}$ ($|U_a| = 2$). The sum of these sizes is $2 + 1 + 2 = 5$, which is less than the required $3k = 6$. Therefore, a successful installation is impossible.