# Problem A — Harmonic Resonance

Time limit: 5 s   Memory limit: 256 MB

## Description

You are tuning a complex instrument that requires installing a set of harmonic resonators. The instrument operates on a fundamental capacity **k**.

You are provided with a catalog of **t** available resonator models. Each model is manufactured with three specific parameters: alpha, beta, and gamma. 

You must select exactly **k** resonator models from the catalog to install into the instrument. Once a set of **k** models is chosen, its *resonance score* is calculated by counting the unique parameter values across the selection. Specifically:
- Let **U_alpha** be the number of distinct alpha values present among the chosen models.
- Let **U_beta** be the number of distinct beta values present among the chosen models.
- Let **U_gamma** be the number of distinct gamma values present among the chosen models.

The resonance score of the selection is the sum **U_alpha** + **U_beta** + **U_gamma**. 

Your task is to determine whether it is possible to select exactly **k** resonator models such that their resonance score is exactly equal to **3k**.

## Input

The first line specifies the fundamental capacity **k** and the catalog size **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k).

The following **t** lines each contain three positive integers representing the alpha, beta, and gamma parameters of a resonator model. You are guaranteed that no parameter in the input is strictly greater than the fundamental capacity. No two resonator models in the catalog have the exact same combination of all three parameters.

## Output

If a successful installation of exactly **k** resonators achieving a resonance score of **3k** is possible, print `YES` on the first line. Following this, print **k** lines, each containing the three parameters of an installed resonator model. If multiple valid installations exist, any of them is acceptable, and the models may be printed in any order.

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

In Example 2, the fundamental capacity **k** is 2, so exactly 2 models must be installed. There are only two available models in the catalog, so both must be selected. The first model has parameters (1, 1, 1) and the second has parameters (2, 1, 2). 
Among these two chosen models:
- The alpha values are 1 and 2, so there are 2 distinct alpha values (**U_alpha** = 2).
- The beta values are 1 and 1, so there is only 1 distinct beta value (**U_beta** = 1).
- The gamma values are 1 and 2, so there are 2 distinct gamma values (**U_gamma** = 2).
The resonance score is **U_alpha** + **U_beta** + **U_gamma** = 2 + 1 + 2 = 5. Because the score is not equal to **3k** (which would be 6), the installation is not successful. Therefore, a successful installation is impossible.