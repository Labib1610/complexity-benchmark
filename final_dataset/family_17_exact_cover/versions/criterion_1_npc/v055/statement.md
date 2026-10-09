# Problem A — Acoustic Resonance Suppression

Time limit: 5 s   Memory limit: 256 MB

## Description
During acoustic stress testing, a reverberation chamber exhibits a spectrum of **3q** distinct resonant frequencies, numbered sequentially from 1 through **3q**, which must all be suppressed to prevent structural damage.

To suppress the resonances, engineers install multi-frequency Helmholtz resonators from a catalog of **t** certified models. Each resonator model is factory-tuned to absorb exactly three specific frequencies. 

When a resonator is installed, it completely dampens its three target frequencies. However, if multiple installed resonators share a target frequency, their overlapping acoustic fields cause destructive interference that voids the test. Therefore, no frequency can be targeted by more than one selected resonator. At the same time, leaving any frequency unsuppressed will result in a failed test, meaning every single frequency must be targeted.

Your task is to determine if it is possible to select exactly **q** resonator models from the catalog such that all **3q** frequencies are successfully dampened. If a valid configuration exists, you must provide it. If the catalog does not contain a combination that satisfies all constraints, you must report that it is impossible.

## Input
The first line contains two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000).
Each of the following **t** lines contains three integers **a**, **b**, and **c** (1 ≤ a < b < c ≤ 3q), representing the three frequencies dampened by one certified resonator model.

## Output
If a valid selection exists, print `YES`, followed by **q** lines each containing the three frequencies of one selected resonator model.
Otherwise, print `NO`.

## Examples
### Example 1
Input:
```
2 3
1 2 3
4 5 6
1 4 5
```
Output:
```
YES
1 2 3
4 5 6
```
