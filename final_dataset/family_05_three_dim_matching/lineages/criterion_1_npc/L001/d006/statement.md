# Problem A — Harmonic Resonance

Time limit: 5 s   Memory limit: 256 MB

## Description

You are tuning a complex instrument that requires installing a set of harmonic resonators. The instrument operates on a fundamental resonance order **k**.

You are provided with a catalog of **t** available resonator models. Each model is manufactured with three specific integer parameters: a frequency multiplier, a phase shift, and an amplitude scale. For every available model, these three parameters are values between 1 and **k** inclusive.

To avoid destructive interference, the installed components must be completely isolated from one another. Two resonator models are considered *isolated* if they differ in their frequency multiplier, and they differ in their phase shift, and they differ in their amplitude scale. 

Your task is to determine whether it is possible to select exactly **k** resonator models from the catalog to install into the instrument such that every pair of selected models is isolated.

## Input

The first line specifies the resonance order **k** and the catalog size **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k).

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

In Example 2, the resonance order **k** is 2, so exactly 2 models must be installed. There are only two available models in the catalog, so both must be selected. The first model has parameters (1, 1, 1) and the second has parameters (2, 1, 2). These two models share the same phase shift (both are 1). Because they do not differ in all three of their parameters, they are not isolated from each other. Therefore, a successful installation is impossible.